# import sys
# locatoin = sys.path
# print(locatoin)

import calendar

# leapdays = calendar.leapdays(2000,2050)

# print(leapdays)

# check range of year for leapyear

for i in range(2000,2050):
    if calendar.isleap(i):
        print(i)
    else:
        continue