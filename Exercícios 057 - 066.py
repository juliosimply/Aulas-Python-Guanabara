# Exercicio 057 Estruturas while

'''sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'mMFf':
    sexo = str(input('Dados incorretos. Digite novamente'))
print('dados cadastrados com sucesso')'''

# Exercicio 058

'''from random import randint
computador = randint(0,5)
print('Sou seu computador e estou pensando em um numero de 0 a 5')
print('será que vc consegue acertar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('um pouco mais.. tente novamente!')
        else:
            print('um pouco menos... tente novamente!')
print(f'você acertou em {palpites} tentativas')'''


# Exercicio 059
'''
maior = 0
num1 = int(input('Digite um numero'))
num2 = int (input('Digite outro numero'))
print('Escolha uma das opções abaixo:')
operação = 0
while not operação == 5 :
    operação = int(input'(
    [1] Somar
    [2] Multiplicar
    [3] Maior 
    [4] Novos numeros
    [5] Sair do programa''''''))
    print(f"qual é sua opção? {operação}")
    if operação == 1:
        totals = num1 + num2
        print(f' a soma de {num1} + {num2} é igual a {totals}')
    elif operação == 2:
        totalM = num1 * num2
        print(f' a multiplacação de {num1} x {num2} é igual a {totalM}')
    elif operação == 3:
        if num1 > num2:
            maior = num1
            print(f'o maior numero é {maior}')
        else:
            maior = num2
        print(f' o maior numero foi {maior}')
    elif operação == 4:
        num1 = int(input('Digite um numero'))
        num2 = int(input('Digite outro numero'))
        print('Escolha uma das opções abaixo:')
    elif operação == 5:
        print('finalizando')
    else:
        print('Opção invalida, Digite novamente')
    print('=-=' * 10)
print(f'FIm do programa, volte sempre!')'''

#Exercício 060

'''n = int(input('digite o numero para fatorial'))
count = n
fatorial = 1
while count > 0:
    fatorial = fatorial * count
    count -= 1
print(f'o fatorial é {fatorial}')'''

#Exercicio 061

'''primeiro = int(input('primeiro termo'))
razao = int(input('razão'))
termo = primeiro
cont = 1
while  cont <= 10:
    print(f' {termo}', end='->')
    termo = termo + razao # ou termo += razao
    cont +=1
print('Acabou')'''

#Exercicio 062

'''primeiro = int(input('primeiro termo'))
razao = int(input('razão'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while  cont <= total:
        print(f' {termo}', end='->')
        termo = termo + razao # ou termo += razao
        cont +=1
    print('Pausa')
    mais = int(input('quantos termos vc quer mostrar a mais?'))
print('FIM')
print(f'Foram gerados {total} termos')'''

# Exercicio 063
'''print('-' * 30)
print('SEQUENCIA FIBONACCI')
print('-' *  30)
n = int(input('Digite quantos termos quer mostrar?'))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end= '')
cont = 3    # pq os dois primeiros termos ja foram atribuidos a t1 e t2
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')'''


'''cont = n1 = 0
n = 0
n = int(input('digite um numero'))
while n != 999:
    n1 += n
    cont +=1
    n = int(input('digite um numero'))
print(f' vc digitou {cont}a soma dos numeros é {n1}')'''

#Exercicio 065


resposta = 'S'
soma = quant =  maior = menor = 0
media =0
while resposta in 'Ss':
    num = int(input('Digite um numero'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar?')).strip().upper()[0]
media= soma / quant
print(f'vc digitou  {quant} numero e a media deu {media}')
print(f'o menor numero e {menor} e o maior é {maior}')








