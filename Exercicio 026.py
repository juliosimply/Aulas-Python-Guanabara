# Exercicio 026 Primeira e ultima ocorrencia de uma string
frase = str(input('Digite uma frase')).strip().upper()
#fraseU = frase.upper()
print('A letra A aparece {} vezes nesta frase '.format(frase.count('A')))
print('a primeira letra A aparece na posição{}'.format(frase.find('A') + 1))
print('a ultima posição que o A apareceu foi{}'.format(frase.rfind('A') +1 )) # rfind busca da direita para a esquerda