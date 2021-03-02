aluno = {}
resultado = 0
aluno['nome']= str(input('Nome:'))
aluno['media'] = float(input('Media:'))
if aluno['media']  >= 5:
    print(f'{aluno["nome"]} foi aprovado com media: {aluno["media"]} ')
else:
    print(f'{aluno["nome"]} foi reprovado com media:  {aluno["media"]}')
