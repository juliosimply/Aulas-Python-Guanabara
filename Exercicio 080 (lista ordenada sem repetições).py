num = list()
for cont in range (0,5):
    n= int(input('Digite um valor'))
    if cont == 0 or n > num[-1]:
        num.append(n)
        print(f'Adicionado na posição {cont}')
    else:
        pos=0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos +=1
print(f'os numero digitados foram {num}')