import datetime
from statistics import mean

import db
import language as lg


class CreateData(db.DataBase):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(self.LANGUAGE)

    def take_period(self, interval):
        """Optimise dates for create_data method"""

        self.connect()

        while True:
            if interval == 1:
                self.periods = list(input(lg.enter_years_lang[self.LANGUAGE]).split())
                if len(self.periods) < 1:
                    self.periods.append(datetime.datetime.now().strftime('%Y'))
                    break
                else:
                    Flag = self._check_period()
                    if Flag:
                        print(lg.incorrect_year_lang[self.LANGUAGE])
                        continue
                    else:
                        break
            elif interval == 2:
                self.periods = list(input(lg.enter_years_lang[self.LANGUAGE]).split())
                if len(self.periods) < 1:
                    self.periods.append(datetime.datetime.now().strftime('%Y'))
                    break
                else:
                    Flag = self._check_period()
                    if Flag:
                        print(lg.incorrect_year_lang[self.LANGUAGE])
                        continue
                    else:
                        break
            else:
                self.periods = list(input(lg.enter_month_lang[self.LANGUAGE]).split())
                if len(self.periods) < 1:
                    self.periods.append(datetime.datetime.now().strftime('%Y-%m'))
                    break
                else:
                    Flag = self._check_period(interval)
                    if Flag:
                        print(lg.incorrect_year_month_lang[self.LANGUAGE])
                        continue
                    else:
                        break
        return self.periods

    def _check_period(self, interval=0):
        """Check if period is period, not anything else"""

        Flag = False
        for period in self.periods:
            try:
                if interval == 3:
                    datetime.date(int(period[:4]), int(period[5:7]), 1)
                else:
                    datetime.date(int(period), 1, 1)
            except ValueError:
                Flag = True
                break
        return Flag

    def create_data(self, interval, overall, mode):
        """Create data for create_graph bar"""

        if interval == 1:
            format_data, label = self._collect_years(mode)
        elif interval == 2:
            format_data, label = self._collect_months(mode)
        else:
            format_data, label = self._collect_days(mode)

        if overall == 1:
            format_data = self._overall_sum(format_data, interval)

        legend_name, maxval, minval = self._legend_name(self.periods, format_data, interval, mode, overall)
        return format_data, label, legend_name, maxval, minval

    def _overall_sum(self, data, interval):
        """Making data overall by year/month/day"""

        overall_list = []

        for idx, values in enumerate(data):
            temp = []
            if interval == 1:
                if idx == 0:
                    overall_list.append(values)
                else:
                    if values > 0:
                        overall_list.append([overall_list[idx - 1][0] + data[idx][0]])
                    else:
                        overall_list.append(0)
            else:
                for index, value in enumerate(values):
                    if index == 0:
                        temp.append(value)
                    else:
                        if value > 0:
                            temp.append(round(temp[index - 1] + values[index], 2))
                        else:
                            temp.append(0)
                overall_list.append(temp)
        return overall_list

    def _collect_years(self, mode):
        """Collecting and formatting data by years"""

        format_data = []
        label = []

        for period in self.periods:
            temp = []
            year = int(period[:4])
            raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                FROM days 
                                JOIN years 
                                JOIN months 
                                ON days.month_id == months.id 
                                AND days.year_id == years.id
                                AND years.year == ?""", (year, ))
            prepare_data = 0
            for date in raw_data:
                if year == date[2]:
                    if mode == 2:
                        prepare_data += date[5]
                    else:
                        prepare_data += round(date[3] + date[4], 2)
            temp.append(round(prepare_data, 2))
            label.append(str(year))
            format_data.append(temp)
        return format_data, label

    def _collect_months(self, mode):
        """Collecting and formatting data by months"""

        format_data = []

        for period in self.periods:
            temp = []
            label = []            
            year = period[:4]
            for month in range(1, 13):
                raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                FROM days 
                                JOIN years 
                                JOIN months 
                                ON days.month_id == months.id 
                                AND days.year_id == years.id 
                                AND months.id == ? 
                                AND years.year == ?""", (month, year))
                prepare_data = 0
                for date in raw_data:
                    if month == date[1] and int(year) == date[2]:
                        if mode == 2:
                            prepare_data += date[5]
                        else:
                            prepare_data += round(date[3] + date[4], 2)
                label.append(str(month))
                temp.append(round(prepare_data, 2))
            format_data.append(temp)
        return format_data, label

    def _collect_days(self, mode):
        """Collecting and formatting data by days"""

        format_data = []

        for period in self.periods:
            temp = []
            label = []
            year = period[:4]
            month = period[5:7]
            raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                FROM days 
                                JOIN years 
                                JOIN months 
                                ON days.month_id == months.id 
                                AND days.year_id == years.id 
                                AND months.id == ? 
                                AND years.year == ?""", (month, year))
            for date in raw_data:
                prepare_data = 0
                if int(month) == date[1] and int(year) == date[2]:
                    if mode == 2:
                        prepare_data += date[5]
                    else:
                        prepare_data += date[3] + date[4]
                temp.append(round(prepare_data, 2))
            format_data.append(temp)

            # Format days for a proper comparsion in graph
            for l in format_data:
                if len(l) < 31:
                    for _ in range(len(l), 31):
                        l.append(0)
        
        # Create ax labels
        for day in range(1, 32):
            label.append(str(day))
        return format_data, label

    def _average(self, format_data):
        """Return average profit or purchases to label"""
        ctr = 0
        allsum = 0
        for value in format_data:
            if value > 0:
                allsum += value
                ctr += 1
        try:
            avg = allsum / ctr
        except ZeroDivisionError:
            avg = 0
        return round(avg, 2)
    
    def _max_min_value(self, format_data, periods, interval, mode):
        """Finding max value in formatted data"""

        maxval = 1
        minval = mean(format_data[0])
        best_period = ['1970', '1', '1']
        worst_period = ['1970', '1', '1']
        if interval == 3:
            for periods in self.periods:
                period_year = periods[:4]
                period_month = periods[5:7]
                raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                    FROM days 
                                    JOIN years 
                                    JOIN months 
                                    ON days.month_id == months.id 
                                    AND days.year_id == years.id 
                                    AND months.id == ? 
                                    AND years.year == ?""", (period_month, period_year))
                for data in raw_data:
                    day, month, year = data[0], data[1], data[2]
                    cash, cashless, purchases = data[3], data[4], data[5]
                    if mode == 2:
                        if maxval < purchases:
                            maxval = purchases
                            best_period = [year, month, day]
                        if minval >= purchases and purchases > 0:
                            minval = purchases
                            worst_period = [year, month, day]
                    else:
                        if maxval < cash + cashless:
                            maxval = round(cash + cashless, 2)
                            best_period = [year, month, day]
                        if minval >= cash + cashless and cash + cashless > 0:
                            minval = round(cash + cashless, 2)
                            worst_period = [year, month, day]
        else:
            for index, data in enumerate(format_data):
                for minmax in data:
                    if maxval <= minmax:
                        maxval = round(minmax, 2)
                        best_period = [periods[index], data.index(maxval) + 1]
                    if minval >= minmax and minmax > 0:
                        minval = round(minmax, 2)
                        worst_period = [periods[index], data.index(minval) + 1]
        return maxval, best_period, minval, worst_period
    
    def _legend_name(self, periods, format_data, interval, mode, overall):
        """Creates legend names for graph"""

        maxval, minval = 0, 0
        legend_list = []

        for index, period in enumerate(periods):
            if overall == 2:
                maxval, best_period, minval, worst_period = self._max_min_value(format_data, periods, interval, mode)
            if interval == 1:
                legend = f"{datetime.date(int(period[:4]), 1, 1).strftime('%Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self._average(format_data[index])}"
                if overall == 2:
                    best_period = datetime.date(int(best_period[0]), 1, 1).strftime('%Y')
                    worst_period = datetime.datetime(int(worst_period[0]), 1, 1).strftime('%Y')
            elif interval == 2:
                legend = f"{datetime.date(int(period[:4]), 1, 1).strftime('%Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self._average(format_data[index])}"
                if overall == 2:
                    best_period = datetime.date(int(best_period[0]), int(best_period[1]), 1).strftime('%B %Y')
                    worst_period = datetime.date(int(worst_period[0]), int(worst_period[1]), 1).strftime('%B %Y')
            else:
                legend = f"{datetime.date(int(period[:4]), int(period[5:7]), 1).strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self._average(format_data[index])}"
                if overall == 2:
                    best_period = datetime.date(int(best_period[0]), int(best_period[1]), best_period[2])
                    worst_period = datetime.date(int(worst_period[0]), int(worst_period[1]), int(worst_period[2]))
            legend_list.append(legend)
        if overall == 2:
            legend_list.append('{0} {1} {2} {3}'.format(lg.max_value_lang[self.LANGUAGE], 
                                                        maxval,
                                                        lg.max_min_period_lang[self.LANGUAGE], 
                                                        best_period))
            legend_list.append('{0} {1} {2} {3}'.format(lg.min_value_lang[self.LANGUAGE], 
                                                        minval,
                                                        lg.max_min_period_lang[self.LANGUAGE], 
                                                        worst_period))
        return legend_list, maxval, minval
