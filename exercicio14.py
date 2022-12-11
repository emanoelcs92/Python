"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
contrário, ele será classificado como "Inocente"."""

print('Vamos começar as perguntas')

pergunta_um = input('Telefonou para a vítima? ')
pergunta_dois = input('Esteve no local do crime? ')
pergunta_tres = input('Mora perto da vítima? ')
pergunta_quatro = input('Devia para a vítima? ')
pergunta_cinco = input('Já trabalhou com a vítima? ')

if pergunta_um == 'S' or 's':
        pontos = 1
else:
        pontos = 0
if pergunta_dois == 'S'or 's':
        pontos = pontos +1
else:
        pontos= pontos+0
if pergunta_tres == 'S'or 's':
        pontos = pontos +1
else:
        pontos = pontos+0
if pergunta_quatro == 'S'or 's':
        pontos = pontos +1
else:
        pontos = pontos + 0
if pergunta_cinco == 'S'or 's':
        pontos = pontos+1
else:
        pontos = pontos+0

if pontos == 2:
        print('Foram detectados em investigação {} respostas positivas. Você é considerada SUSPEITA, estamos de olho em você.'.format(pontos))

elif pontos == 3 or pontos == 4:
        print('Foram detectados em investigação {} respostas positivas. Você é considerada CÚMPLICE, estamos de olho em você.'.format(pontos))

elif pontos == 5:
        print('Foram detectados em investigação {} respostas positivas. Você é ASSASSINO.Está preso.'.format(pontos))

else:
        print('Você é INOCENTE')