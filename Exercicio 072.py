nExtenso = ('zero', 'Um', 'Dois', ' Três', 'Quatro', 'Cinco', ' Seis', 'Sete', 'Oito',
            ' NOve', 'Dez', 'Onze', ' Doze', 'Treze', 'Quatorze', ' Quinze', 'Dezesseis', 'Dezessete',
             'dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero de 0 a 20:'))
    if num > 20 or num < 0:
        print('Voce Digitou um numero invalido')
    else:
        break
print(f'Voce Digitou o número {nExtenso[num]}')
