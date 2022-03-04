# task5.py
#
# Weekend or Weekday?
#
# Author: Elaine Tynan

import datetime

day = datetime.datetime.today().weekday()

if day < 5:
    print ("Unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")