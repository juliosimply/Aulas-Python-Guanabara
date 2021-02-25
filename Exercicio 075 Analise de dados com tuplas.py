num = (int(input('Digite um numero')),
       int(input('Digite outro numero')),
       int(input('Digite  mais um numero')),
       int(input('Digite ultimo numero')))
print(f'Vc Digitou os numeros {num}')
print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3) + 1}')
else:
    print(' o valor 3 não foi digitado')
for n in num:
    if n % 2 == 0:
        print(f'o numero {n} é par')
