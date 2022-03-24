# timesheetentry.py
#
# Class called Timesheetentry that has three attributes that are all 
# set by an __init__ function
#
# Author: Andrew Beatty

import datetime as dt

class Timesheetentry:
    # __init__ is the constructor (one of the dunder methods)
    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration

    def __str__(self):
        return self.project + " " + str(self.start) + " " + str(self.duration)

if __name__ == '__main__':
    dt1 = dt.datetime(2022,3,23,15,36)
    tse1 = Timesheetentry("project1",dt1, 5)
    dt2 = dt.datetime(2022,1,1)
    tse2 = Timesheetentry("project2",dt2, 3)
    print(tse1)
    print(tse2)
