from random import randint
from operator import itemgetter
jogador = {'jogador1': randint(1,6),
            'jogador2': randint(1,6),
            'jogador3': randint(1,6),
            'jogador4': randint(1,6)}
ranking = []
for k,v in jogador.items():
    print(f'o jogador {k} tirou {v}')
print('O RESULTADO DO RANKING')
print('=-'*30)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f' o {i+1} lugar:  {v[0]} com {v[1]}')