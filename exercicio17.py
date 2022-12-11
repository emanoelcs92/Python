num = int(input('Digite um número: '))
tot = 0

for C in range(1, num + 1):
    if num % C == 0:
        print('\033[33m',end='')
        tot += 1
    else:
        print('\033[31m',end='')

    print('{}'.format(C),end='')

print('\n\033[m0 O número {} foi divísível {} vezes'.format(num,tot))

if tot == 2:
    print('Por isso ele é um número PRIMO!')
else:
    print('NÃO é um número PRIMO!')