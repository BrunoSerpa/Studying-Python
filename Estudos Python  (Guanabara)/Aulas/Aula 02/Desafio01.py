Variavel1 = input('Digite algo:\n')
Variavel2 = input('Digite outra coisa:\n')

if (Variavel1.isalpha() == True):
    if (Variavel2.isalpha() == True):
        print('{} e {} são palavras'.format(Variavel1, Variavel2))
    elif (Variavel2.isalnum() == True):
        print('{} é uma palavra, mas {} é um número inteiro'.format(Variavel1, Variavel2))
    else:
        print('{} é uma palavra, mas {} é um número decimal'.format(Variavel1, Variavel2))
elif (Variavel1.isalnum() == True):
    if (Variavel2.isalpha() == True):
        print('{} é um decimal, mas {} é uma palavra'.format(Variavel1, Variavel2))
    elif (Variavel2.isalnum() == True):
        Numero1=int(Variavel1)
        Numero2=int(Variavel2)
        Soma=Numero1 + Numero2
        print('{} e {} são números inteiros. A soma deles dará {}'.format(Numero1, Numero2, Soma))
    else:
        Numero1=int(Variavel1)
        Numero2=float(Variavel2)
        Soma=Numero1 + Numero2
        print('{} é um número inteiro, mas {} é um número decimal. A soma deles dará {}'.format(Numero1, Numero2, Soma))
else:
    if (Variavel2.isalpha() == True):
        print('{} é um decimal, mas {} é uma palavra'.format(Variavel1, Variavel2))
    elif (Variavel2.isalnum() == True):
        Numero1=float(Variavel1)
        Numero2=int(Variavel2)
        Soma=Numero1 + Numero2
        print('{} é um número decimal, mas {} é um número inteiro. A soma deles dará {}'.format(Numero1, Numero2, Soma))
    else:
        Numero1=float(Variavel1)
        Numero2=float(Variavel2)
        Soma=Numero1 + Numero2
        print('{} e {} são números decimais. A soma deles dará {}'.format(Numero1, Numero2, Soma))