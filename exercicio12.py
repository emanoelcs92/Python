# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelo os quais
# ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado.

dias = float(input('Para quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros foram rodados: '))
valor = dias * 60 + (km * 0.15)
print('O Valor do total do aluguel do carro saiu por R${:.2f}.\n Total de dias {};\n Total de Km rodados{}Km'.format(valor,dias,km))