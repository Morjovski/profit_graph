import datetime
from statistics import mean

import db
import language as lg


class CreateData(db.DataBase):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__()
        self.format_data = []
        self.label = []

    def take_period(self, interval):
        """Optimise dates for create_data method"""

        db.DataBase.connect(self)

        if interval == 1:
            self.periods = list(input('Введите годы (Формат YYYY): ').split())
        elif interval == 2:
            self.periods = list(input('Введите год в формате "yyyy": ').split())
        else:
            self.periods = list(input('Введите год и месяц в формате "yyyy-mm": ').split())
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

        legend_name = self.legend_name(self.periods, format_data, interval)

        return format_data, label, legend_name

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
        """Collect data by years"""

        format_data = []
        label = []

        for period in self.periods:
            year = period[:4]
            temp = []
            data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                                            FROM days 
                                            JOIN years 
                                            JOIN months 
                                            ON days.month_id == months.id 
                                            AND days.year_id == years.id
                                            AND years.year == ?""", (year, ))
            prepare_data = 0
            for date in data:
                if int(period[:4]) == date[2]:
                    if mode:
                        prepare_data += date[5]
                    else:
                        prepare_data += round(date[3] + date[4], 2)
            temp.append(prepare_data)
            label.append(str(year))
            format_data.append(temp)
        print(label)
        return format_data, label
 

    def collect_months(self, mode):
        """Collect data by months"""

        format_data = []

        for period in self.periods:
            temp = []
            label = []            
            year = period[:4]
            for month in range(1, 13):
                data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                            FROM days 
                            JOIN years 
                            JOIN months 
                            ON days.month_id == months.id 
                            AND days.year_id == years.id
                            AND months.id == ?
                            AND years.year == ?""", (month, year))
                prepare_data = 0
                for date in data:
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
        """Collect data by days"""

        format_data = []

        for period in self.periods:
            temp = []
            label = []
            year = period[:4]
            month = period[5:7]
            data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                        FROM days 
                        JOIN years 
                        JOIN months 
                        ON days.month_id == months.id 
                        AND days.year_id == years.id
                        AND months.id == ?
                        AND years.year == ?""", (month, year))

            for date in data:
                prepare_data = 0
                if int(period[5:7]) == date[1] and int(period[:4]) == date[2]:
                    if mode:
                        prepare_data += date[5]
                    else:
                        prepare_data += round(date[3] + date[4], 2)
                temp.append(prepare_data)
            format_data.append(temp)

            for l in format_data:
                if len(l) < 31:
                    for _ in range(len(l), 32):
                        l.append(0)

        for day in range(1, 32):
            label.append(str(day))

        return format_data, label

    def average(self, data):
        """Return average profit or purchases to label"""
        return round(mean(data), 2)
    
    def max_data(self, data):
        """Finding max value in formatted data"""

        maxval = 0
        for date in data:
            if max(date) > maxval:
                maxval = max(date)
        return maxval
    
    def legend_name(self, periods, data, interval):
        """Creates legend names for graph"""

        label_list = []
        for index, period in enumerate(periods):
            if interval == 1:
                label = f"{datetime.date(int(period[:4]), 1, 1).strftime('%Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(data[index])}"
            else:
                label = f"{datetime.date(int(period[:4]), index + 1, 1).strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(data[index])}"
            label_list.append(label)
        return label_list
    
    def periods_save(self, periods):
        string = ''
        for period in periods:
            string = ' '.join(periods)


            