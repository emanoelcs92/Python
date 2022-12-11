"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros
vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule
e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$
2,50 o preço do litro do álcool é R$ 1,90. """

combustivel = input('Qual o combustivel será usado para abastecer? ')
litros = float(input('Quantos litros irá abastecer? '))
preco_por_litro_alcool = 1.90
preco_porlitro_gasolina = 2.50


if combustivel == 'A':
        if litros <= 20:
            valor = preco_por_litro_alcool*litros
            desconto = (valor*3)/100
            valor_com_desconto = valor - desconto
        else:
            valor = preco_por_litro_alcool * litros
            desconto = (valor*5)/100
            valor_com_desconto = valor - desconto
        print('O valor a ser pago é R${}'.format(valor_com_desconto))
elif combustivel == 'G':
        if litros <= 20:
            valor = preco_porlitro_gasolina * litros
            desconto = (valor*4)/100
            valor_com_desconto = valor - desconto
        else:
            valor = preco_porlitro_gasolina * litros
            desconto = (valor*6)/100
            valor_com_desconto = valor - desconto
        print('O valor a ser pago é R${}'.format(valor_com_desconto))
else:
     print('Não temos outro tipo de combustivel.')