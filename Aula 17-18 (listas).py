# aula de listas
# o metodo .append('novoItem') vai adicionar novo item a um alista (no final da lista)
# o metodo .insert(0, 'novoItem') vai adicionar um novo item porem na posição "zero" conforme o argumento
# para apagar a 3 formas = del novoItem[3] / novoItem.pop(3) / item.remove('nomeDoItem') em todos os casos remove o item e recontar os indices
'''num = [2,5,9,1]
num[2] = 4
num.sort()
num.append(9)
num.sort(reverse=True)
num.insert(1, 35)
num.pop() #elimina  o ultimo
num.pop(3) # elimina na posição 3
num.remove(5) #elimina o ELEMENTO '5' da lista
print(num)
print(f'essa lista tem {len(num)} elementos')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate (valores): # pegando as chaves e os valores com o enumerate
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')


for cont in range(0,3):
    valores.append(int(input('Digite um valor')))
print(f'Encontrei esse valores digitados {valores}')''''''

#a = [1,2,3,4]
#b=a[:] # nesse caso com o "[:]" ele faz uma copia independente de a, se não colocar ele simplesmente atribui uma a outra'''

# Aula 018

'''teste = list()
teste.append('Julio')
teste.append(37)
galera = list()
galera.append(teste[:]) # importancia dos ":" sem ele uma sobrepoe a outra
teste[0] = 'maria'
teste[1] = 22
galera.append(teste)
print(galera)

galera = [['julio', 37], ['paulo', 25],['vania', 60], ['maria', 45]]
for p in galera:
    print(f'o {p[0]} tem {p[1]} anos de idade')'''
galera = list()
dado = list()
totmaior= totmenor=0
for c in range (0,3):
    dado.append(str(input('Qual o seu nome?')))
    dado.append(int(input('Qual a sua idade')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de 21 anos')
        totmaior +=1
    else:
        print(f'{p[0]} é menores de 21 anos')
        totmenor +=1
print(f'temos {totmaior} maiores de idade e {totmenor} menores de idade')
