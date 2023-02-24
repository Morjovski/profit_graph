import sqlite3
import calendar

import language as lg


class DataBase:

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        self.year_id = 0

    def connect(self):
        self.conn = sqlite3.connect('entries.sqlite')
        self.cur = self.conn.cursor()

    def create(self):
        """Create tables in database if they not exists"""
        self.cur.executescript("""
            CREATE TABLE IF NOT EXISTS years (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            year INTEGER NOT NULL UNIQUE
            );
            
            CREATE TABLE IF NOT EXISTS months (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            month TEXT UNIQUE
            );
            
            CREATE TABLE IF NOT EXISTS days (
            id INTEGER NOT NULL PRIMARY KEY UNIQUE,
            day INTEGER,
            cash REAL,
            cashless REAL,
            purchases INTEGER,
            month_id INTEGER,
            year_id INTEGER
            );
        """)

    def insert_day(self, day, month, cash, cashless, purchases, year):
        """Inserts day, month, year_id, cash, cashless and purchases to "days" table"""
        year_data = self.cur.execute("SELECT years.id, years.year FROM years WHERE years.year = ?", (year, ))
        for year in year_data:
            year_id = year[0]
        self.cur.execute("""INSERT INTO days (day, cash, cashless, purchases, month_id, year_id) 
                            VALUES (?, ?, ?, ?, ?, ?)""",
                            (day, cash, cashless, purchases, month, year_id))

    def insert_month(self, month):
        """Inserts month id and month name in "months" table"""
        month_name = calendar.month_name[int(month)]
        self.cur.execute('INSERT OR IGNORE INTO months (id, month) VALUES (?, ?)', (month, month_name))

    def insert_year(self, year):
        """Inserts year in "years" table"""
        self.cur.execute('INSERT OR IGNORE INTO years (year) VALUES (?)', (year, ))
    #     self.check_year_id(year)

    # def check_year_id(self, year):
    #     """Takes year_id to "days" table"""
    #     years_db = self.cur.execute('SELECT years.id, years.year FROM years')
    #     for year_db in years_db:
    #         if year_db[1] == int(year):
    #             self.year_id = year_db[0]

    def duplicate_check(self, period):
        """Check if current period is not in Database"""
        duplicate = self.cur.execute("""SELECT days.day, days.month_id, days.year_id 
                                        FROM days 
                                        JOIN years 
                                        WHERE days.day = ? AND days.month_id = ?""", (period[8:], period[5:7]))
        for date in duplicate:
            if date[0] == int(period[8:]) and date[1] == int(period[5:7]) and date[2] == self.year_id:
                print(lg.date_already_in_DB[self.LANGUAGE])
                return True
        else:
            return False

    def commit(self):
        """Commits changes to Database"""
        self.conn.commit()

    def close(self):
        """Close connection with Database"""
        self.cur.close()
        