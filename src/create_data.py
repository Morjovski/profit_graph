import datetime
from statistics import mean

import db
import language as lg


class CreateData(db.DataBase):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(self.LANGUAGE)
        self.format_data = []
        self.label = []

    def take_period(self, interval):
        """Optimise dates for create_data method"""

        db.DataBase.connect(self)

        if interval == 1:
            self.periods = list(input(lg.enter_years_lang[self.LANGUAGE]).split())
            if len(self.periods) <= 3:
                self.periods = list(datetime.datetime.now().strftime('%Y'))
                print(f'Выбран период за {self.periods[0]} год')
        elif interval == 2:
            self.periods = list(input(lg.enter_years_lang[self.LANGUAGE]).split())
            if len(self.periods) <= 3:
                self.periods = list(datetime.datetime.now().strftime('%Y'))
                print(f'Выбран период за {self.periods[0]} год')
        else:
            self.periods = list(input(lg.enter_month_lang[self.LANGUAGE]).split())
            if len(self.periods) <= 6:
                self.periods = list(datetime.datetime.now().strftime('%Y-%m'))
                print(f'Выбран период за {self.periods[0]} год')
        return self.periods

    def create_data(self, interval, overall, mode):
        """Create data for create_graph bar"""

        if interval == 1:
            format_data, label = self.collect_years(mode)
        elif interval == 2:
            format_data, label = self.collect_months(mode)
        else:
            format_data, label = self.collect_days(mode)

        if overall:
            format_data = self.overall_sum(format_data, interval)

        legend_name, maxval, minval = self.legend_name(self.periods, format_data, interval, mode)

        return format_data, label, legend_name, maxval, minval

    def overall_sum(self, data, interval):
        """Making data overall by year/month/day"""

        overall_list = []

        for idx, values in enumerate(data):
            temp = []
            if interval == 1:
                if idx == 0:
                    overall_list.append(values)
                else:
                    overall_list.append([overall_list[idx - 1][0] + data[idx][0]])
            else:
                for index, value in enumerate(values):
                    if index == 0:
                        temp.append(value)
                    else:
                        temp.append(temp[index - 1] + values[index])
                overall_list.append(temp)

        return overall_list

    def collect_years(self, mode):
        """Collecting and formatting data by years"""

        format_data = []
        label = []

        for period in self.periods:
            temp = []
            year = period[:4]
            raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                FROM days 
                                JOIN years 
                                JOIN months 
                                ON days.month_id == months.id 
                                AND days.year_id == years.id
                                AND years.year == ?""", (year, ))  
            prepare_data = 0
            for date in raw_data:
                if int(period[:4]) == date[2]:
                    if mode:
                        prepare_data += date[5]
                    else:
                        prepare_data += round(date[3] + date[4], 2)
            temp.append(prepare_data)
            label.append(str(year))
            format_data.append(temp)
        return format_data, label

    def collect_months(self, mode):
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
                        if mode:
                            prepare_data += date[5]
                        else:
                            prepare_data += round(date[3] + date[4], 2)
                label.append(str(month))
                temp.append(prepare_data)
            format_data.append(temp)
        return format_data, label

    def collect_days(self, mode):
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
                    if mode:
                        prepare_data += date[5]
                    else:
                        prepare_data += round(date[3] + date[4], 2)
                temp.append(prepare_data)
            format_data.append(temp)

            # Format days for a proper comparsion in graph
            for l in format_data:
                if len(l) < 31:
                    for _ in range(len(l), 32):
                        l.append(0)
        
        # Create ax labels
        for day in range(1, 32):
            label.append(str(day))

        return format_data, label

    def average(self, data):
        """Return average profit or purchases to label"""
        return round(mean(data), 2)
    
    def max_min_value(self, format_data, periods, interval, mode):
        """Finding max value in formatted data"""

        maxval = 0
        minval = format_data[0][0]
        if interval == 3:
            for periods in self.periods:
                year = periods[:4]
                month = periods[5:7]
                raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                    FROM days 
                                    JOIN years 
                                    JOIN months 
                                    ON days.month_id == months.id 
                                    AND days.year_id == years.id 
                                    AND months.id == ? 
                                    AND years.year == ?""", (month, year))
                for data in raw_data:
                    if mode:
                        if maxval < data[5]:
                            maxval = data[5]
                            max_period = [data[2], data[1], data[0]]
                        if minval > data[5]:
                            minval = data[5]
                            min_period = [data[2], data[1], data[0]]
                    else:
                        if maxval < float(data[3] + data[4]):
                            maxval = float(data[3] + data[4])
                            max_period = [data[2], data[1], data[0]]
                        if minval > float(data[3] + data[4]):
                            minval = float(data[3] + data[4])
                            min_period = [data[2], data[1], data[0]]
        else:
            for index, data in enumerate(format_data):
                if max(data) >= maxval:
                    maxval = max(data)
                    max_period = [periods[index], data.index(maxval) + 1]
                if min(data) <= minval:
                    minval = min(data)
                    min_period = [periods[index], data.index(minval) + 1]
        return maxval, max_period, minval, min_period
    
    def legend_name(self, periods, format_data, interval, mode):
        """Creates legend names for graph"""

        legend_list = []
        for index, period in enumerate(periods):
            maxval, best_period, minval, worst_period = self.max_min_value(format_data, periods, interval, mode)
            if interval == 1:
                legend = f"{datetime.date(int(period[:4]), 1, 1).strftime('%Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(format_data[index])}"
                best_period = datetime.date(int(best_period[0]), 1, 1).strftime('%Y')
                worst_period = datetime.datetime(int(worst_period[0]), 1, 1).strftime('%Y')
            elif interval == 2:
                legend = f"{datetime.date(int(period[:4]), 1, 1).strftime('%Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(format_data[index])}"
                best_period = datetime.date(int(best_period[0]), int(best_period[1]), 1).strftime('%B %Y')
                worst_period = datetime.date(int(worst_period[0]), int(worst_period[1]), 1).strftime('%B %Y')
            else:
                legend = f"{datetime.date(int(period[:4]), int(period[5:7]), 1).strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(format_data[index])}"
                best_period = datetime.date(int(best_period[0]), int(best_period[1]), best_period[2])
                worst_period = datetime.date(int(worst_period[0]), int(worst_period[1]), int(worst_period[2]))
            legend_list.append(legend)
        legend_list.append('{0} {1} {2} {3}'.format(lg.max_value_lang[self.LANGUAGE], maxval, lg.max_min_period_lang[self.LANGUAGE], best_period))
        legend_list.append('{0} {1} {2} {3}'.format(lg.min_value_lang[self.LANGUAGE], minval, lg.max_min_period_lang[self.LANGUAGE], worst_period))

        return legend_list, maxval, minval
