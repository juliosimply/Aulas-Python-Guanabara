

num = list()
while True:
    n = int(input('Digite um numero'))
    if n not in num:
        num.append(n)
        print('Numero adicionado com sucesso')
    else:
        print('Numero duplicado')
    resp = str(input('Quer continuar? [ S/N]'))
    if resp in 'nN':
        break
num.sort()
print(f'os numeros digitados foram {num}')

