
#Faça um Programa que receba 2 números e em seguida pergunte ao usuário qual operação ele
#deseja realizar. O resultado da operação deve aparecer com uma frase que diga se o número é:
#a. par ou ímpar;
#b. positivo ou negativo;
#c. inteiro ou decimal.

A = float(input('Digite um valor: '))
B = float(input('Digite mais um valor: '))
operador = input('Qual a operação que vocÊ deseja fazer? ')
result = 0

if operador == '+':
    result = A + B
    print('O resultado da soma é {}'.format(result))
    if result > 0:
        print('Número Negativo')
    else:
        print('Número Positivo')
    if result % 2 == 0:
        print('Número par')
    else:
        print('Número impar')
    if result % 1 == 0:
        print('Número inteiro')
    else:
        print('Número decimal')
elif operador == '*':
     result = A*B
     print('O resultado da multiplicação é {}'.format(result))
     if result > 0:
         print('Número Negativo')
     else:
         print('Número Positivo')
     if result % 2 == 0:
         print('Número par')
     else:
         print('Número impar')
     if result % 1 == 0:
        print('Número inteiro')
     else:
        print('Número decimal')
elif operador == '-':
     result = A-B
     print('O resultado da subtração é {}'.format(result))
     if result > 0:
         print('Número Negativo')
     else:
         print('Número Positivo')
     if result % 2 == 0:
         print('Número par')
     else:
         print('Número impar')
     if result % 1 == 0:
        print('Número inteiro')
     else:
        print('Número decimal')
elif operador == '/':
      result = A/B
      print('O resultado da divisão é {}'.format(result))
      if result > 0:
          print('Número Negativo')
      else:
          print('Número Positivo')
      if result % 2 == 0:
          print('Número par')
      else:
          print('Número impar')
      if result % 1 == 0:
          print('Número inteiro')
      else:
          print('Número decimal')
else:
    print('Impossivel executar a operação')




