"""LP-A03] Crie um algoritmo que recebe como entrada o dia e o mês de nascimento e retorna o signo, seguindo as faixas de valores informados:

- Áries: de 21 março a 20 abril;

- Touro: de 21 abril a 20 maio;

- Gêmeos: de 21 maio a 20 junho;

- Câncer: de 21 junho a 22 julho;

- Leão: de 23 julho a 22 agosto;

- Virgem: de 23 agosto a 22 setembro;

- Libra: de 23 setembro a 22 outubro;

- Escorpião: de 23 outubro a 21 novembro;

- Sagitário: de 22 novembro a 21 dezembro;

- Capricórnio: de 22 dezembro a 20 janeiro;

- Aquário: de 21 janeiro a 18 fevereiro;

- Peixes: de 19 fevereiro a 20 março."""

dia = int(input('Qual o dia do seu nascimento?'))
mes = (input('Qual o mês do seu nascimento? '))

if dia>=19 and mes == 'fevereiro' or dia<=20 and mes == 'março':
    print('Seu signo é peixes.')

elif dia>=21 and mes == 'janeiro' or dia<=18 and mes == 'fevereiro':
    print('Seu signo é aquário')

elif dia>= 21 and  mes == 'abril' or dia<=20 and mes == 'maio':
    print('Seu signo é touro.')

elif dia>=21 and mes == 'maio' or dia<=20 and mes == 'junho':
    print('Seu signo é gêmeos.')

elif dia>=21 and mes == 'junho' or dia<=22 and mes == 'julho':
    print('Seu signo é Câncer')

elif dia>=23 and mes == 'julho' or dia<=22 and mes == 'agosto':
    print('Seu signo é leão.')

elif dia>=23 and mes == 'agosto' or dia<=22 and mes == 'setembro':
    print('Seu signo é virgem.')

elif dia>=23 and mes == 'setembro' or dia<=22 and mes == 'outubro':
    print('Seu signo é libra.')

elif dia>=23 and mes == 'outubro' or dia<=21 and mes == 'novembro':
    print('Seu signo é escorpião.')

elif dia>=22 and mes == 'novembro' or dia<=21 and mes == 'dezembro':
    print('Seu signo é sagitário')

elif dia>22 and mes == 'dezembro' or dia<=20 and mes == 'janeiro':
    print('Seu signo é capricórnio')

else:
    print('Valores não correspondem há nenhum signo.')