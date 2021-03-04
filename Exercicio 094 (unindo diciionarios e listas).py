galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]:')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digte apenas M ou F:')
    pessoa['idade']= int(input('Idade:'))
    galera.append(pessoa.copy())
    soma = soma + pessoa['idade']
    while True:
        resp = str(input('Quer continuar?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda S ou N')
    if resp == 'N':
        break
print('=-'*30)
print(f' A todo foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'a media de idade  é {media:5.2f} anos')
print(f' As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome" ]}', end='  ')
print()
print('Lista das pessoas que estão acima da media:')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
