#Estrutura de repetição while, diferentemente do for que geralmente sabemos onde começa e onde termina, o while vai loopar até  a condição ser atingica
'''for c in range(1,10):
    print(c)
print('fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n % 2 ==0:
        par +=1
    else:
        impar +=1
print(f'vc digitou {par} numeros pares e {impar} numeros impares')
