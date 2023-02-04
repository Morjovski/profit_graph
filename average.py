import json
from statistics import mean
from create_data import CreateData

class Average:

    def __init__(self):
        self.createdata = CreateData()
        self.average = 0
        self.period = []

    def average_sum(self, period):
        self.average = mean(self.createdata.profit)