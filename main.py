# Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias: infantil A = 5 - 7 ano; infantil B = 8-10 anos; juvenil A = 11-13 anos; juvenil B = 14-17 anos; adulto = maiores de 18 anos

print('Nadador, saiba qual é a sua classificação: \n')

print ('Digite o número que corresponde ao grupo da sua idade:\n'
      'Caso tenha entre 5 e 7 anos, digite 1.\n'
      'Caso tenha entre 8 e 10 anos, digite 2.\n'
      'Caso tenha entre 11 e 13 anos, digite 3.\n'
      'Caso tenha entre 14 e 17 anos, digite 4.\n'
      'Caso tenha 18 anos ou mais, digite 5. \n')

num = int(input('Digite o número correspondente ao seu grupo: '))

if num == 1:
    print('Sua classificação é Infantil A.')
elif num == 2:
    print('Sua classificação é Infantil B.')
elif num == 3:
    print('Sua classificação é Juvenil A.')
elif num == 4:
    print('Sua classificação é Juvenil B.')
elif num == 5:
    print('Sua classificação é Adulto.')
else:
  print('Sem Classificação.')
