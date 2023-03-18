import datetime
from statistics import mean

from . import db 
from . import language as lg


class CreateData(db.DataBase):

    def __init__(self, LANGUAGE: str) -> None:
        self.LANGUAGE = LANGUAGE
        super().__init__(self.LANGUAGE)

    def take_period(self, interval: int) -> list[str]:
        """Optimise dates for create_data method"""

        self.connect()

        while True:
            if interval == 3:
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
            else:
                self.periods = list(input(lg.enter_years_lang[self.LANGUAGE]).split())
                if len(self.periods) < 1:
                    self.periods.append(datetime.datetime.now().strftime('%Y'))
                    break
                else:
                    Flag = self._check_period(interval)
                    if Flag:
                        print(lg.incorrect_year_lang[self.LANGUAGE])
                        continue
                    else:
                        break
        return self.periods

    def _check_period(self, interval: int) -> bool:
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

    def create_data(self, interval: int, overall: int, mode: int) -> tuple[list, list, list, float, float]:
        """Create data for create_graph bar"""

        if interval == 1:
            format_data, label = self._collect_years(mode)
        elif interval == 2:
            format_data, label = self._collect_months(mode)
        else:
            format_data, label = self._collect_days(mode)

        overall_dif = []
        if overall == 1:
            format_data, overall_dif = self._overall_sum(format_data, interval)

        legend_name, maxval, minval = self._legend_text(format_data, interval, mode, overall, overall_dif)
        return format_data, label, legend_name, maxval, minval

    @staticmethod
    def _overall_sum(format_data: list, interval: int) -> tuple[list, list]:
        """Makes data overall by year/month/day"""

        overall_list = []
        overall_dif = []
        for idx, values in enumerate(format_data):
            temp = []
            temp_dif = []
            if interval == 1:
                if idx == 0:
                    overall_list.append(values)
                    overall_dif.append(values)
                else:
                    if values[0] > 0:
                        overall_list.append([round(overall_list[idx - 1][0] + format_data[idx][0], 2)])
                        overall_dif.append(values)
                    else:
                        overall_list.append([0])
                        overall_dif.append([0])
            else:
                for index, value in enumerate(values):
                    if index == 0:
                        temp.append(value)
                        temp_dif.append(value)
                    else:
                        if value > 0:
                            temp.append(round(temp[index - 1] + values[index], 2))
                            temp_dif.append(round(temp[index] - temp[index - 1], 2))
                        else:
                            temp.append(0)
                            temp_dif.append(0)
                overall_dif.append(temp_dif)
                overall_list.append(temp)
        return overall_list, overall_dif

    def _collect_years(self, mode: int) -> tuple[list, list]:
        """Collects and formats data by years"""

        format_data = []
        label = []

        for period in self.periods:
            temp = []
            year = int(period)
            raw_data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                FROM days 
                                JOIN years 
                                JOIN months 
                                ON days.month_id == months.id 
                                AND days.year_id == years.id
                                AND years.year == ?""", (year, ))
            prepare_data = 0
            for date in raw_data:
                cash, cashless, purchases = date[3], date[4], date[5]
                if year == date[2]:
                    if mode == 2:
                        prepare_data += purchases
                    else:
                        prepare_data += cash + cashless
            temp.append(round(prepare_data, 2))
            label.append(str(year))
            format_data.append(temp)
        return format_data, label

    def _collect_months(self, mode: int) -> tuple[list, list]:
        """Collects and formats data by months"""

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
                    cash, cashless, purchases = date[3], date[4], date[5]
                    if month == date[1] and int(year) == date[2]:
                        if mode == 2:
                            prepare_data += purchases
                        else:
                            prepare_data += round(cash + cashless, 2)
                label.append(str(month))
                temp.append(round(prepare_data, 2))
            format_data.append(temp)
        return format_data, label

    def _collect_days(self, mode: int) -> tuple[list, list]:
        """Collects and formats data by days"""

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

    @staticmethod
    def _average(data: list, interval: int) -> float:
        """Return average profit or purchases to label"""
        if interval == 1:
            return round(sum(data) / 12, 2)
        else:
            ctr = 0
            allsum = 0
            for value in data:
                if value > 0:
                    allsum += value
                    ctr += 1
            try:
                avg = allsum / ctr
            except ZeroDivisionError:
                avg = 0
            return round(avg, 2)
    
    def _max_min_value(self, format_data: list, interval: int, mode: int) -> tuple[float, list, float, list]:
        """Finding max and min value in data"""

        maxval = 1
        minval = round(sum(format_data[0]), 2)
        best_period = ['1970', '1', '1']
        worst_period = ['1970', '1', '1']
        if interval == 3:
            for period in self.periods:
                period_year = period[:4]
                period_month = period[5:7]
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
                            best_period = datetime.date(year, month, day).strftime("%Y-%m-%d")
                        if minval >= purchases > 0:
                            minval = purchases
                            worst_period = datetime.date(year, month, day).strftime("%Y-%m-%d")
                    else:
                        if maxval < cash + cashless:
                            maxval = round(cash + cashless, 2)
                            best_period = datetime.date(year, month, day).strftime("%Y-%m-%d")
                        if minval >= cash + cashless > 0:
                            minval = round(cash + cashless, 2)
                            worst_period = datetime.date(year, month, day).strftime("%Y-%m-%d")
        else:
            for index, data in enumerate(format_data):
                year = int(self.periods[index])
                for value in data:
                    if maxval <= value:
                        maxval = round(value, 2)
                        best_period = datetime.date(year, data.index(value) + 1, 1).strftime("%B-%Y") if interval == 2 else \
                                      datetime.date(year, 1, 1).strftime("%Y")
                    if minval >= value > 0:
                        minval = round(value, 2)
                        worst_period = datetime.date(year, data.index(value) + 1, 1).strftime("%B-%Y") if interval == 2 else \
                                       datetime.date(year, 1, 1).strftime("%Y")
        return maxval, best_period, minval, worst_period
    
    def _legend_text(self, format_data: list, interval: int, mode: int, overall: int, overall_dif: list) -> tuple[list, float, float]:
        """Creates legend text for graph"""

        maxval, minval = 0, 0
        legend_list = []
        average = []

        for index, period in enumerate(self.periods):
            if overall == 1:
                average.append(self._average(overall_dif[index], interval))
            else:
                average.append(self._average(format_data[index], interval))

            if overall == 2:
                maxval, best_period, minval, worst_period = self._max_min_value(format_data, interval, mode)

            if interval == 3:
                legend = f"{datetime.date(int(period[:4]), int(period[5:7]), 1).strftime('%B %Y')}, " \
                         f"{lg.average_purchases_lang[self.LANGUAGE]} {average[index]}" \
                         f"{self._percent_change(average[0], average[index])}"
            else:
                legend = f"{datetime.date(int(period[:4]), 1, 1).strftime('%Y')}, " \
                         f"{lg.average_purchases_lang[self.LANGUAGE]} {average[index]}" \
                         f"{self._percent_change(average[0], average[index])}"

            legend_list.append(legend)

        if overall == 2:
            legend_list.append('{0} {1}\n{2} {3}'.format(lg.max_value_lang[self.LANGUAGE], 
                                                        maxval,
                                                        lg.max_min_period_lang[self.LANGUAGE], 
                                                        best_period))
            legend_list.append('{0} {1}\n{2} {3}'.format(lg.min_value_lang[self.LANGUAGE], 
                                                        minval,
                                                        lg.max_min_period_lang[self.LANGUAGE], 
                                                        worst_period))
        return legend_list, maxval, minval

    def _percent_change(self, first: float, second: float) -> str:
        """Return a percent value compare to first period"""

        if first < second:
            return f"\n(+{str(round(((second - first) / first) * 100, 2))}% {lg.compare_to_first_period_lang[self.LANGUAGE]})"
        elif first > second:
            return f"\n({str(round(((second - first) / first) * 100, 2))}% {lg.compare_to_first_period_lang[self.LANGUAGE]})"
        else:
            return ''

    def _color_schema(self, cm, length):
        if length <= 8:
            return [cm.tab10(i) for i in range(length + 2)]
        else:
            return [cm.tab20(i) for i in range(length + 2)]
