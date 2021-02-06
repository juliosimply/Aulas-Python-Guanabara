# Exercicio 016 separando o numero inteiro
'''
from math import trunc
num = float(input('Digite um numero'))
print('o valor digitado foi {} e a sua porção inteira é{}'.format(num, trunc(num)))'''

num = float (input(' Digite um numero'))
print('o valor digitado foi {} e sua parte inteira é{}'.format(num, int(num)))

# Exercicio 017 calculando a hipotenusa
from math import hypot
ca = float(input('comprimento cateto adjacente'))
co = float(input('comprimento cateto oposto'))
# hi = (co ** 2 + ca ** 2) ** (1/2) importando da match a função hypot abaixo
hi = hypot(co, ca)
print(' a hipotenusa vai medir {:.2f}'.format(hi))

# Exercício 018 seno, cosseno e tangente
import math
angulo = float(input('Digite o angulo'))
seno = math.sin(math.radians(angulo))
print('o ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('o ângulo de {}, tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print(' o ângulo {}, tem a TANGENTE de {:.2f}'.format(angulo,tangente))

# Exercicio 019 sorteando um item da lista
import random

aluno1 = str (input('primeiro  nome'))
aluno2 = str (input('segundo nome'))
aluno3 = str (input('terceiro nome'))
aluno4 = str (input('quarto nome'))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))

#Exercicio 020 sorteando ordem da lista

from random import shuffle
nome1 = str(input('Primeiro nome'))
nome2 = str(input('segundo nome'))
nome3 = str(input('terceiro nome'))
nome4 = str(input('quarto nome'))
listas = [nome1,nome2,nome3,nome4]
shuffle(listas)
print('a ordem de apresentação é:', listas)





