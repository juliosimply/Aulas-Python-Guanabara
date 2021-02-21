palavras= ('aprender', 'julio', 'somar', 'cesar', 'ferreira', 'campos', 'mercado', 'dinheiro', 'ouro')
for p in palavras:
    print(f'\n na palavra {p}, temos ',end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')