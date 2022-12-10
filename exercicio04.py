# Ler 3 valores (considere que não serão informados valores iguais) e
# escrever o maior deles.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite mais um número: '))

if num1 == num2 or num1 == num3 or num2 == num3:
    print('Valor Invalido!\nRecomece e digite valores diferentes.')

else:
    if num1 > num2 and num1 > num3:
        print('O maior valor digitado é {}'.format(num1))
    elif num2 > num1 and num2 > num3:
        print('O maior valor digitado é {}'.format(num2))
    elif num3 > num2 and num3 > num2:
        print('O maior valor digitado é {}'.format(num3))
