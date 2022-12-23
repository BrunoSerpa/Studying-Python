from random import sample
Student1 = input('Insert the name from the first student:\n')
Student2 = input('Insert the name from the second student:\n')
Student3 = input('Insert the name from the third student:\n')
Student4 = input('Insert the name from the fourth student:\n')
ChosenStudents= [Student1, Student2, Student3, Student4]
ChosenStudents= sample(ChosenStudents, k=len(ChosenStudents))
print('The chosen order of presentation of the students will be: {}, {}, {} and {}.'.format(ChosenStudents[0], ChosenStudents[1], ChosenStudents[2], ChosenStudents[3]))