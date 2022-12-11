PrimeiroNumero=int(input('Digite um número:\nResposta:'))
SegundoNumero=int(input('Digite outro número:\nResposta:'))
Operacao=int(input('Escolha a operação simples que deseja realizar neles:\nSoma:1\nSubtração:2\nMultiplicação:3\nDivisão:4\nResposta:'))
if (Operacao==1):
    print('O resultado dará:', PrimeiroNumero+SegundoNumero)
elif (Operacao==2):
    print('O resultado dará:', PrimeiroNumero-SegundoNumero)
elif (Operacao==3):
    print('O resultado dará:', PrimeiroNumero*SegundoNumero)
elif (Operacao==4):
    print('O resultado dará:', PrimeiroNumero/SegundoNumero)