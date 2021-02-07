# Exercicio 027 primeiro e ultimo no de uma pessoa
n = str(input('Digite o nome complet')).strip()
nome = n.split()
print('Seu primeiro nome é {}  '.format(nome[0]))
print('e seu ultimo nome é {}'.format(nome[len(nome)-1]))