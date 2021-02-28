matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
somaColuna = somaLinha = somaPar=maior= 0
for c in range(0,3):
    for l in range (0,3):
        matriz[c][l]= int(input(f'Digite um valor para [{l}, {c}]'))
print('=-'*30)
for c in range(0,3):
    for l in range (0,3):
        print(f'[{matriz[c] [l]:^3}]', end='')
        if matriz[c][l] % 2 == 0:
            somaPar+= matriz[c][l]
    print()
print(f'a soma dos pares é :{somaPar} ')
for c in range(0,3):
    somaColuna += matriz[c][2]
for l in range(0,3):
    if l == 0 or matriz[1][l] > maior:
        maior= matriz[1][l]
print(f'o maior numero da segunda coluna {maior}')
print(f'a soma dos valores da terceira coluna é {somaColuna}')


