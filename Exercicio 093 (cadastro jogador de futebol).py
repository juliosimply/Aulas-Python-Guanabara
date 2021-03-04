jogador = {}
gols = []
totalGols =0
jogador['nome'] = str(input('Nome:'))
jogador['partidas'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou:'))
for c in  range (jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c +1}')))
    totalGols = totalGols + gols[c]
    jogador['gols'] = gols[:]
print('=-'*30)
print(f'{jogador} fez um total de {totalGols}')
for i, v in enumerate(gols):
    print(f'o jogador fez {v} gols na partida {i +1} ')


## solução Guanabara

'''jogador = dict()
partidas = list()
jogador['nome']= str(input('nome jogador'))
tot = int(input(f'quantas partidas o {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida{c}')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'o campos {k} tem o valor {v}')
print('-='* 30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols')
print(f' Foi um total de {jogador["total"]} gols')'''

