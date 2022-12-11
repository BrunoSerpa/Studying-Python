from datetime import date
Hoje = date.today()
DiaAtual= int(Hoje.strftime("%d"))
MesAtual= int(Hoje.strftime("%m"))
AnoAtual= int(Hoje.strftime("%Y"))

DiaNascimento= int(input('Digite o dia que você nasceu?\nResposta:'))
MesNascimento=int(input('Digite o mes que você nasceu?\nResposta:'))
AnoNascimento=int(input('Digite o ano que você nasceu?\nResposta:'))

DiasTotaisVida = ((AnoAtual-AnoNascimento) * 365) + ((MesAtual-MesNascimento) * 30) + (DiaAtual-DiaNascimento)
AnosTotaisVida = int(DiasTotaisVida / 365)
MesesTotaisVida = int((DiasTotaisVida - AnosTotaisVida * 365) / 30)
DiasTotaisVida = DiasTotaisVida - AnosTotaisVida * 365 - MesesTotaisVida * 30

print('Você tem aproximadamente', AnosTotaisVida,'ano(s),', MesesTotaisVida,'meses/mes e', DiasTotaisVida,'dia(s) de vida')