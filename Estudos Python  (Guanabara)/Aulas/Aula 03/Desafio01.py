PrimeiroNumero = int(input ('Digite um número:\nResposta:'))
SegundoNumero = int(input ('Digite um número:\nResposta:'))
if (PrimeiroNumero>SegundoNumero):
    if (PrimeiroNumero-SegundoNumero==1):
        print('Visto que {0} é o número sucessor de {1}, e {1} o número sucessor de {0}, o número sucessor de {0} é {2} e o número antecessor de {1} é {3}'.format(PrimeiroNumero, SegundoNumero, PrimeiroNumero+1, SegundoNumero-1))
    else:
        print('O número antecessor de sucessor dos números escolhidos ({0} e {1}), é:\n{0}: sucessor de {2} e antecessor de {3}; \n{1}: sucessor de {4} e antecessor de {5};\n A distância desses números é {6}, sendo {0} o maior deles'.format(PrimeiroNumero, SegundoNumero, PrimeiroNumero-1, PrimeiroNumero+1, SegundoNumero-1, SegundoNumero+1, PrimeiroNumero-SegundoNumero))
elif (PrimeiroNumero<SegundoNumero):
    if (SegundoNumero-PrimeiroNumero==1):
        print('Visto que {0} é o número antecessor de {1}, e {1} o número sucessor de {0}, o número antecessor de {0} é {2} e o número sucessor de {1} é {3}'.format(PrimeiroNumero, SegundoNumero, PrimeiroNumero-1, SegundoNumero+1))
    else:
        print('O número antecessor de sucessor dos números escolhidos ({0} e {1}), é:\n{0}: sucessor de {2} e antecessor de {3}; \n{1}: sucessor de {4} e antecessor de {5};\n A distância desses números é {6}, sendo {1} o maior deles'.format(PrimeiroNumero, SegundoNumero, PrimeiroNumero-1, PrimeiroNumero+1, SegundoNumero-1, SegundoNumero+1, SegundoNumero-PrimeiroNumero))
else:
    print('Foram digitados dois números iguais a {0}, sendo seu antecessor {1} e seu sucessor {2}'.format(PrimeiroNumero,PrimeiroNumero-1,PrimeiroNumero+1))