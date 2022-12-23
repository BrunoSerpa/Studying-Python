from math import modf, exp
Number = float(input('Insert a real number:\n'))
IntNumber = int(Number)
DecimalNumber = Number - IntNumber
print('The integer portion of {} is {} and the decimal portion is {}'.format(Number, IntNumber, DecimalNumber))