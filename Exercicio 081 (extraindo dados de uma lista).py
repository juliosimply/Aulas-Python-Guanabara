num = []
resp = 's'
while True:
    n = int(input('Digite um valor'))
    num.append(n)
    resp = str(input('Quer continuar [S/N]?'))
    if resp in 'nN':
        break
num.sort(reverse=True)
print(f'foram digitados {len(num)}')
print(f' os numeros digitados foram: {num} elementos')
if 5 in num:
    print('o numero 5 foi digitado ')
else:
    print('não foi digitado nenhum numero 5')
