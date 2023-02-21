import json
import datetime
from statistics import mean, StatisticsError

import db
import language as lg

class CreateData(db.DataBase):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__()
        self.format_data = []

    def take_period(self, interval):
        db.DataBase.connect(self)
        '''Optimise dates for create_data method'''
        if interval == 1:
            self.periods = list(input('Введите года через запятую (Формат YYYY): ').split())
        elif interval == 2:
            self.periods = list(input('Введите год в формате "yyyy": ').split())
        else:
            self.periods = list(input('Введите год и месяц в формате "yyyy-mm": ').split())

    def create_data(self, interval, overall, mode):
        """Create data for create_graph bar"""

        if interval == 1:
            self.collect_years(mode)
        elif interval == 2:
            self.collect_months(mode)
        elif interval == 3:
            self.collect_days(mode)

        if overall:
            self.format_data = self.overall_sum(self.format_data)
        return self.format_data, self.periods

    def overall_sum(self, data):
        """Making data overall by year/month/day"""

        overall_list = []
        for index in range(data):
            if index == 0:
                overall_list.append(data[index])
            else:
                overall_list.append(data[index-1] + data[index])
        return overall_list

    def collect_years(self, mode):
        """Collect data by years"""

        for period in self.periods:
            year = period[:4]
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
                        prepare_data += date[3] + date[4]
            self.format_data.append(prepare_data)
    
    def collect_months(self, mode):
        """Collect data by months"""

        for period in self.periods:
            year = period[:4]
            for month in range(1, 13):
                data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                            FROM days 
                            JOIN years 
                            JOIN months 
                            ON days.month_id == months.id 
                            AND days.year_id == years.id
                            AND month.id == ?
                            AND years.year == ?""", (month, year))
                prepare_data = 0
                for date in data:
                    if month == int(period[5:7]) and int(period[:4]) == date[2]:
                        if mode:
                            prepare_data += date[5]
                        else:
                            prepare_data += date[3] + date[4]
                self.format_data.append(prepare_data)

    def collect_days(self, mode):
        """Collect data by days"""

        for period in self.periods:
            year = period[:4]
            month = period[5:7]
            data = self.cur.execute("""SELECT days.day, months.id, years.year, days.cash, days.cashless, days.purchases 
                        FROM days 
                        JOIN years 
                        JOIN months 
                        ON days.month_id == months.id 
                        AND days.year_id == years.id
                        AND month.id == ?
                        AND years.year == ?""", (month, year))
            prepare_data = 0
            for date in data:
                if month == int(period[5:7]) and int(period[:4]) == date[2]:
                    if mode:
                        prepare_data += date[5]
                    else:
                        prepare_data += date[3] + date[4]
            self.format_data.append(prepare_data)
            if len(self.format_data) < 31:
                for _ in range(len(self.format_data), 31):
                    self.format_data.append(0)

    def average(self, data):
        '''Return average profit or purchases to label'''
        return round(mean(data), 2)
    
    def max_data(self, data):
        """Finding max value in formatted data"""

        max = 0
        for date in data:
            if max(date) > max:
                max = max(date)
        return max
    
    def label_name(self, periods, data):
        label = f"{self.graph_period_start.strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(data)}"
        return label

            