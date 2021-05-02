# CHAPTER 6 Exercises

import math
# exercise number 1
"""
a = math.floor(-2.8)
print(a)
b = abs(round(-4.3,0))
print(b)
c = math.ceil(math.sin(34.5))
print(c)
"""

# excercise 2

"""
import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2024))
print(calendar.isleap(2019))

dir(calendar)

print(calendar.leapdays(2021, 2050))
print(calendar.weekday(2016, 7, 29))
"""

# excercise 3

def average(num1, num2):

    """ (number, number) -> number

    Return the average of num1 and num 2

    >>> average(10, 20)
    15.0

    >>> average(2.5, 3.0)
    2.75

    """

    return (num1 + num2) / 2
