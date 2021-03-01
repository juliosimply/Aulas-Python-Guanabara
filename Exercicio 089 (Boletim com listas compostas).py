alunos =[]
resposta = 0
while True:
    nome =str(input('Nome:'))
    nota1 =float(input('nota 1:'))
    nota2 =float(input('Nota 2:'))
    media = (nota2 + nota1)/2
    alunos.append([nome, [nota1, nota2], [media]])
    resp = str(input('Quer continuar?[S/N]'))
    if resp in 'Nn':
        break
print('Numero Nome     media')
for i, l in enumerate(alunos):
    print(f'{i} {l[0]}{l[2]}')
    print('=-' * 30)

while True:
    resposta=int(input('Mostrar notas de qual aluno (999 interrompe)'))
    if resposta == 999:
        break
    if resposta <= len(alunos) -1:
        print(f'o aluno {alunos[resposta][0]} teve essas notas {alunos[resposta][1]}')
        print('='*25)
print('Fim')