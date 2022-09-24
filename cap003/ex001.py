dia = str(input('Qual dia da semana é hoje? '))
dia = dia.lower()
if dia == 'sabado' or dia == 'domingo':
    print('Hoje é dia de descanso')
else:
    print('Hoje é dia de trabalho!')
