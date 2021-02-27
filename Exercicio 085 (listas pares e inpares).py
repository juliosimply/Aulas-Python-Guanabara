num = [[], []]
total = 0
for cont in range (1,8):
    total =(int(input(f'Digite o {cont} numero:')))
    if total % 2 == 0:
        num[0].append(total)
    else:
        num[1].append(total)
print(f'os numeros pares foram {sorted(num[0])}, os impares foram {sorted(num[1])} e o total foi {sorted(num)}')
