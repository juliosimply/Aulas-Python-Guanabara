# Exercicio 067
'''num = 0
cont =soma= 0
while True:
    num = int(input('Digite um numero'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'vc digitou {cont} numeros e a soma entre eles é {soma}')'''

#Exercicio 068 tabuada

'''num =0
tabuada = cont =0
while  True:
    num = int(input('Digite um numero para saber sua tabuada'))
    if num < 0:
        break
    for cont in range (0,10):
        tabuada = cont * num
        print(f'a tabuada de {num} x {cont} = {tabuada}  ')
print('PROGRAMA ENCERRADO')'''


#Exercicio 069
'''from random import randint
v = 0

while True:
    num = int(input('Digite um valor'))
    computador = randint(0, 10)
    total = num + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar?')).strip().upper()[0]
    print(f'voce jogou {num} e o computador {computador}. total de {total}')
    print('deu par' if total % 2== 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('parabens vc venceu')
            v +=1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('vc venceu')
            v +=1
        else:
            print('vc perdeu')
            break
print('fim')'''




# Exercicio 070
'''tot18=totH= totM20 =0
while True:
    idade = int(input('Digite idade'))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo= str(input('sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total de pessoas com mais de 18 anos é {tot18}')
print(f'ao todo temos {totH} homens')
print(f' e temos {totM20} mulheres com menos de 20 anos')
print('Acabou')'''

# Exercicio 070
'''total = totmil = menor = cont = 0
barato =' '
while True:
     produto = str(input('Digite o produto'))
     preço = float(input('Digite o preço'))
     cont +=1
     total += preço
     if preço > 1000:
         totmil = totmil + 1
     if cont == 1 or preço < menor:
         menor = preço
         barato =produto
     resp =' '
     while resp not in 'SN':
         resp = str(input('quer continuar?')).strip().upper()[0]
     if resp == 'N':
         break
print('='* 40,'FIM DO PROGRAMA')
print(f'o total dos produtos é R${total:.2f}')
print(f'temos {totmil} que custam mais de 1000,00')
print(f'o produto mais barato foi {barato} que custa R${menor}')'''

#Exercicio 071 caixa eletronico

print('=' * 30)
print(f"{'BANCO CEV':^30}")
print('=' * 30)
saque = int(input('Qual o valor do saque?'))
valorSaque = saque
cedula = 50
totalCedula=0
while True:
    if valorSaque >=cedula:
        valorSaque -= cedula
        totalCedula +=1
    else:
        if totalCedula > 0:
            print(f'total de cedulas {totalCedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula =10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula =1
        totalCedula = 0
        if valorSaque ==0:
            break
print('='* 30)
print('SAQUE REALIZADO COM SUCESSO. VOLTE SEMPRE!')



