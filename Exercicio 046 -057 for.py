# Exercicio 046 contagem regressiva fogos de artificio

'''import time

for c in range (11, 0, -1):
    time.sleep(1)
    print(c)
    time.sleep(1)
print("foooogooo")'''

# Exercício 047 mostrar numeros pares de 1 a 50

'''for c in range(2, 51, 2):
    print(c)'''

#Exercicios 048 soma numeros impares de 1 a 500

'''soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
        soma = soma + c # OU soma += c
        cont = cont +1  # OU cont += 1

print('a soma dos {} numeros da {}'.format(cont, soma))'''

# Exercício 049

'''Num = int(input('Digite um numero para saber sua tabuada'))
for m in range (0,11):
    tab = m * Num
    print('o numero {} X {} = {}'.format(Num,m,tab))'''

# Exercicio 050
'''s = 0
cont = 0
for c in range (1,7):
    n = int(input("Digite o {} numero".format(c)))
    if n % 2 == 0:
        s  += n
        cont += 1
print('a soma desses numeros é {} '.format(s))'''

# Exercicio 051 progressão aritimetica

'''primeiro = int(input('primeiro termo'))
razao = int(input('razão'))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(' {}'.format(c), end= '->')
print('Acabou')'''

#Exercicio 052 numeros primos

'''num = int(input('Digite um numero'))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
        print('{}'.format(c), end='')
print('o numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print(' esse numero é primo')
else:
    print('ELe não é primo')'''

# Exercicio 053 crie um palindromo


'''frase = str(input("digite uma frase")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo')
else:
    print('A frase digitada não é um palindromo')
print('Voce digitou a frase '.format(frase))'''

#Exercicio 054

'''from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a pessoa nasceu:'))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print(f'ao todo tivemos {totmenor} menore e um total de {totmaior} maiores ')'''

#Exercicio 055
'''maior = 0
menor = 0
for pessoa in range(1,6):
    peso =float(input(f'peso {pessoa}'))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso {maior}')
print(f'o menor peso {menor}')'''

#Exercicio 056

somaIdade = 0
mediaIdade = 0
maiorIdade =0
nomeVelho = ''
totMulher = 0
for p in range (1,4):
    print(f'--------{p} pessoa ---------')
    nome = str(input('nome:')).strip()
    idade = int(input('idade'))
    sexo = str(input('sexo [M/F] ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher +=1
mediaIdade = somaIdade/3
print(f'a media de idade é {maiorIdade}')
print(f'o mais velho é {nomeVelho}')
print(f' ao todo são {totMulher} mulheres com menos de 20 anos')



