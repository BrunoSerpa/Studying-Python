degreeCelsius = int(input("Insert a temperature in degrees Celsius:\n"))
degreesFahrenheit = degreeCelsius / 5 * 9 + 32
print('{}°C equals {:.2f}°F'.format(degreeCelsius, degreesFahrenheit))