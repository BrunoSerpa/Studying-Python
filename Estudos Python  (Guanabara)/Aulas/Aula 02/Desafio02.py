Variavel1 = input('Digite algo:\n')

if (Variavel1.isalpha() == True):
        print('{} é uma palavra com {} caractéres'.format(Variavel1, len(Variavel1)))
elif (Variavel1.isalnum() == True):
        print('{} é uma número inteiro com {} caractéres'.format(Variavel1, len(Variavel1)))
else:
        print('{} é uma número decimal com {} caractéres'.format(Variavel1, len(Variavel1)))