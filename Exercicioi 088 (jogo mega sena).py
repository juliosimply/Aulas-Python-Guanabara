from random import randint
palpites = []
jogos = list()
totalJogos=1
num  =0
quant = int(input('Quantos jogos deseja?'))
while totalJogos <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
            cont +=1
        if cont >= 6:
            break
    jogos.append(palpites[:])
    palpites.clear()
    totalJogos += 1
print(f'sorteando {quant} jogos ')
for i, l in enumerate (jogos):
    print(f'jogo {i+1}: {l}')




