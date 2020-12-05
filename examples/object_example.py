import datetime


class Day:
    def __init__(self, month, year, day_of_week):
        self.month = month
        self.year = year
        self.day_of_week = day_of_week

    def tomorrow(self):
        if self.day_of_week == 'Wednesday':
            return Day(self.month, self.year, 'Thursday')


if __name__ == '__main__':
    day = Day('March', 1993, 'Wednesday')
    day2 = Day('June', 1920, 'Wednesday')

    print(day2.tomorrow().tomorrow().tomorrow())
    print(datetime.now())
