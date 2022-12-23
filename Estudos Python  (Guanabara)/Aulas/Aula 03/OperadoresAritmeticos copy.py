'+, -, *, /, **, //, %'
'Ordem de Precedência: "()", "**", "*, /, // ou %" e "+ ou -"'
PrimeiroNumero = int(input('Um valor:'))
SegundoNumero = int(input('Outro valor:'))
Soma = PrimeiroNumero + SegundoNumero
Subtracao = PrimeiroNumero - SegundoNumero
Multiplicacao = PrimeiroNumero * SegundoNumero
Exponenciacao = PrimeiroNumero ** SegundoNumero
Divisao = PrimeiroNumero / SegundoNumero
InteiroDivisao = PrimeiroNumero // SegundoNumero
RestoDivisao = PrimeiroNumero % SegundoNumero
print('A soma é {}; \nA subtração é {}; A multiplicação é {}; A divisão é {:.3f};'.format(Soma, Subtracao, Multiplicacao, Divisao), end='. ')
print('Já a divisão inteira é {}; o resto é {}; e a potenciação é {};'.format(InteiroDivisao, RestoDivisao, Exponenciacao))
