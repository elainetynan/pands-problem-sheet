# employee.py
#
# Class that has one attribute called timesheets ( set to an empty list) 
# and an __init__ function that takes in a first and last name.
#
# Author: Andrew Beatty

import datetime as dt
from timesheetentry import *

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + " " + self.last

    def logminutes(self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)

    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes


if __name__ == '__main__':
    test = Employee('Some', 'One')
    print(test)
    assert(str(test) == 'Some One')

    test.logminutes('p1', 30)
    test.logminutes('p2', 60)
    mins = test.gettotaltime()
    print(mins)
    assert(mins == 90)

    print('All good')