# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milimetros.

valor1 = float(input('Digite um valor em metros: '))
mm = valor1*1000
cm = valor1*100

print('O valor digitado convertido de metros para: \nmilimetros: {} mm \ncentímetros: {} cm'.format(mm,cm))

