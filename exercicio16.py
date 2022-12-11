"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido;"""

dia = int(input('Digite um número referente ao dia da semana: '))

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-Feira')
    case 3:
        print('Terça-Feira')
    case 4:
        print('Quarta-Feira')
    case 5:
        print('Quinta-Feira')
    case 6:
        print('Sexta-Feira')
    case 7:
        print('Sabado')
    case _:
        print('Não é um dia da semana')
