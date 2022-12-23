from math import sqrt
AdjaC = float(input('Insert a value in the adjacent collared peccary:\n'))
PoseC = float(input('Insert a value in the pose collared peccary:\n'))
Hypotenuse = sqrt(AdjaC**2 + PoseC**2)
print('The hypotenuse of the triangle with sides {} and {} is approximately {:.3f}'.format(AdjaC, PoseC, Hypotenuse))