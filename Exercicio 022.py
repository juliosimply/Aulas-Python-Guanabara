#Exercicio 022 analisando seu nome
nome = str(input('Digite seu nome completo')).strip()
print('seu nome em maiusculas é{}'.format(nome.upper()))
print('seu nome em minusculas é:{}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {}'.format(nome.find(' ')))

#Exercicio 023 separando digitos de um numero

'''num = int (input('Digite um numero de o a 9999'))     transformando numero em strings
n = str(num)
print('Analisando o numero{}'.format(num))
print('unidade{}'.format(n[3]))
print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar{}'.format(n[0]))'''

num =int(input('Informe um numero'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero{}'.format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))