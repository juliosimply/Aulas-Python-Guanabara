num=[]
maior= menor =0
for n in range(0, 5):
    num.append(int(input(f'Digite um numero na posição {n} = ')))
    if n == 0:
        menor=maior=num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]
print(f' {num}')
print(f'o maior {maior}')
print(f'o menor é {menor}')


