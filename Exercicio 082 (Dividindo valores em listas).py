num =list()
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor')))
    resp =str(input('Quer continuar [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-'*25)
print(f'Foram Digitados esse numeros impares {impares}')
print(f'foram digitados esses numeros pares {pares}')
print(f'o total de numeros é : {num}')