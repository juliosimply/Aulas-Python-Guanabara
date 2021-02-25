nome =list()
peso = list()
total = []
maior=menor=0
while True:
    nome.append(str(input('Nome:')))
    peso.append(int(input('Peso:')))
    total.append(peso)
    resp = str(input('Quer comtinuar [S/N]?'))
    if resp in 'nN':
        break
    if len(total) == 0:
        peso = menor = maior = 0
    else:
        if total[0] < menor:
            menor = total[0]
        if total[0] > maior:
            maior = total[0]
print(f'o mais pesado foi {maior}')
print(f'o mais leve foi {menor}')
print('o total de cadastrados foi',len(nome))



