lanche =('Hambúguer', 'Suco', 'pizza' ,'Pudim', ' Batata frita')
for comida in lanche:
    print(f'Eu vou comer {comida}') #sem precisar da posição

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # precisando da posição

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))  # metodo sorted coloca a em orgem alfabetica

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  #nesse caso não ha soma e sim uma contenação
print(c)
print(c.count(5)) # vai imprimir quantas vezes tem o numero 5
print(c.index(8)) # vai mostrar em que posição esta o numero 8 mas mostra apenas a primeira ocorrencia

pessoa = ( 'Julio', '37 anos', 'Analista de sistemas', 'pesa= 99,88kg') #detro de uma tupla pode haver varios tipos primitivos























print('Comi pra caramba')

# 03 maneiras de usar tuplas e for usando determinadas maneiras de escrever e indentificar e atribuir