
frase = str ('curso em vídeo')
print(frase[9])
print(frase[9:13]) #mostrar do 9 ao 12 pois o 13 é excluido da contagem
print(frase[9:21:2]) #do 9 ao 21 pulando 2
print(frase[:5]) # quando omite o primeiro, ele começa do "0" ate o 4
print(frase[15:]) # indicou o inicio mas não o final, vai do 15 até o final
print(frase[9::3]) # vai começar no 9 pulando de 3 em 3 (mostra o terceiro)
print(len(frase)) # mostrar o tamanho da (frase) o len seria 21
print(frase.count('o')) #quantas vezes tem o; "o" (case sensitive)
print(frase.count('o', 0, 13)) #vai contar quantos "0" tem do 0 ao 13
print(frase.find('deo')) #vai indicar onde começa o "deo" ex [11] se colocar algo que não tenha vai retornar [-1]
print('curso' in frase) #vai retornar boleano
print(frase.replace('python', 'android')) # replace vai subsituir "python" por "android"
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) # vai colocar tudo em minusculo, somente a primeira letra em maisculo
print(frase.title()) # vai colocar todas as palavras com a primeira letra maiuscula
print(frase.strip()) # remove todos os espaço do começo e do final da string
print(frase.rstrip())# remove somente os ultimos espaços
print(frase.lstrip())# remove somente os espaços do inicio da string
print(frase.split()) # cria uma divisão quando a espaços gerando novas listas de cada cadeia de caracteres
print('-'.join(frase)) #vai juntas as cadeias de caracteres com um hifem

nome = str (input("qual o seu nome?"))
print(nome.upper())
print(nome.lower())
print(nome.strip())
print(len(nome))
nome1 = (nome.split())
print(len(nome1[0]))