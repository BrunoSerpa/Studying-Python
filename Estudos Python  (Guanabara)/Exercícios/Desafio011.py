Height = int(input('Input the height of the wall:\n'))
Width = int(input('Input the width of the wall:\n'))
Area = Height * Width
print('You will need {} liters of paint to paint a wall of {} m²'.format(Area/2, Area))