#Exercicio 025 procurando uma string dentro de outra
nome = str(input('Digite seu nome completo')).strip()
print('tem silva no seu nome?{}'.format('silva' in nome.lower()))
