nome = []
total = []
maior = menor = 0
while True:
    nome.append(str(input('Nome:')))
    nome.append(float(input('Peso:')))
    if len(total) == 0:
        maior = menor = nome[1]
    else:
        if nome[1] > maior:
            maior = nome[1]
        if nome[1] < menor:
            menor = nome[1]
    total.append(nome[:])
    nome.clear()
    resp = str(input('Quer comtinuar [S/N]?'))
    if resp in 'nN':
        break

print(f'o mais pesado foi {maior}')
for p in total:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'o mais leve foi {menor}')
print('o total de cadastrados foi',len(total))



