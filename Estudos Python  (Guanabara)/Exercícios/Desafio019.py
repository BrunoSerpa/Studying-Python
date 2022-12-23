from random import choice
Student1 = input('Insert the name from the first student:\n')
Student2 = input('Insert the name from the second student:\n')
Student3 = input('Insert the name from the third student:\n')
Student4 = input('Insert the name from the fourth student:\n')
ChosenStudent= choice([Student1, Student2, Student3, Student4])
print('The chosen student was {}'.format(ChosenStudent))