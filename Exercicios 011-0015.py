#Exercicios de 11 ao 15

#lg = float (input('Digite a largura da sua parede:'))
#al = float (input('Digite a altura da sua parede:'))
#ar = (lg * al)
#qt = ar/ 2
#print('a area da sua parede :é {:.2f} m2 e precisara de {:.2f} lts de tinta'.format(ar, qt))

#Exercicio 012 calculando descontos

valor1 =float(input('Digite o valor do produto'))
valorD = valor1 - (valor1 * 5/100)
print(valorD)

#Exercicio 013 Reajuste salarial

sal = float(input('qual o seu salario R$?'))
saln = sal + (sal * 15/100)
print(saln)

#Exercicio 014 conversor de temperaturas

c = float(input('Informe a temperatuea em c'))
f = ((9 * c) /5) + 32
print(' a temperatura de {}c corresponde a  {:.2f}f'.format(c,f))

#Exercicio 015 Aluguel de carros

km = float (input('Quantos KM foram rodados?'))
Diaria = int (input('quantos dias de locação?'))
total = (km * 0.15) + (Diaria * 60)
print('o valor a pagar é ', total)


