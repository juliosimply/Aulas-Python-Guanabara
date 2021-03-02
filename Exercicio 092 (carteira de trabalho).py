from datetime import datetime
dados = {}
dados['nome']= str(input('Nome:'))
nasc = int(input('ano de nascimento:'))
dados['ctps'] = int(input('Numero CTPS: '))
dados['idade']=  datetime.now().year - nasc
if dados['ctps'] != 0:
    dados['contratação']= int(input('Ano de contratação'))
    dados['salario']= float(input('Salario R$:'))
    dados['Aposentadoria'] = dados['idade'] + (dados['contratação']+35) - datetime.now().year
else:
    print('Voce não possui carteira de trabalho')


print('=-'*30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
