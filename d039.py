from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
    print('Seu Alistamento será em {}'.format(atual+(18-idade)))
elif idade > 18:
    print('Você ja deveria ter se alisatado a {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(atual-(idade-18)))
    