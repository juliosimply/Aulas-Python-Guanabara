# Estruturas if e else

#calculando media do aluno
'''n1 = float(input('Qual a primeira nota?'))
n2 = float(input('Qual a segunda nota?'))
M = (n1 + n2)/2
print('A sua media foi{:.2f}:'.format(M))
if M>= 6:
    print('Parabens vc foi aprovado')
else:
    print('você não foi aprovado. Precisa estudar um pouco mais!')'''


# joguinho acertando numero aleatorio

'''from random import randint
from time import sleep
num = int(input('Digite um numero de 0 a 5:'))
num1 = randint(0,5)
if num1 == num:
    print('PROSESSANDO...')
    sleep(3)
    print("parabens vc acertou")
else:
    print('PROSESSANDO...')
    sleep(3)
    print('que pena vc errou! Eu pensei {}'.format(num1))'''


#multa por excesso de velocidade
'''vel = int(input('qual a velocidade'))
limite = 80
if vel >80:
    print('vc foi multado. Sua multa é de {}'.format((vel - limite)*7))
else:
    print('Tenha um bom dia e dirija com segurança')'''


#saber se numero é par ou impar

'''n = int(input('Digite um numero'))
if n % 2== 0:
    print('Esse numero {} é par'.format(n))
else:
    print('Esse numero {} é impar'.format(n))'''



# calculando preço de uma viagem pela distancia


'''v = int (input('Quantos km de distancia?'))
km1 = float = 0.50
km2 = float = 0.45
if v <= 200:
    print('A sua viagem vai custar {:.2f}'.format(v * km1))
else:
    print('A sua viagem vai custar {:.2f}'.format(v * km2))'''

# Ano bissexto


'''from datetime import date
ano = int(input('que ano quer analisar ou Digite "0" para o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('o ano {} é Bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))'''

# Maiores e menores valores

'''a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))
menor = a
if b < a and b<c:
    menor = b
if c<a and c < b:
    menor = c
maior = a
if b> a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o maior valor digitado foi {}'.format(maior))
print('menor valor digitado foi {}'.format(menor))'''

# Aumentos salarios

'''salario = float(input('Digite o valor do seu salario'))

if salario <= 1250:
    salarion = salario + (15 * salario / 100)
else:
    salarion = salario + (10 * salario / 100)
print('seu salario com aumento é {:.2f}'.format(salarion))'''

#formando triangulos com 3 retas


print('-=' * 20)
print('Analisador de triangulos')
print('-=' * 20)
r1 = float(input('Digite primeiro segmento'))
r2 = float(input('Dgite segundo segmento'))
r3 = float(input('Digite o terceiro segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 <r1 +r2:
    print('os segmentos acima podem formar triangulo')
else:
    print('os segmentos acima não podem formar triangulo')


