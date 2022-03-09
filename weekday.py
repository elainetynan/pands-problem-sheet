# weekday.py
#
# Weekend or Weekday?
#
# Author: Elaine Tynan
#
# Updated: 09/03/2022
# By: Elaine Tynan
# Changes after feedback from Andrew
# I changed the import statement as it makes writing the code using the date class shorter
# I have done a little research on which is more efficient and according to
# softwareengineering.stackexchange.com there is no performance difference:
# https://softwareengineering.stackexchange.com/questions/187403/import-module-vs-from-module-import-function

#import datetime
from datetime import date # Changed this from import datetime as it makes call

day = date.today().weekday()
#day = datetime.date.today().weekday()

if day < 5:
    print ("Unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")