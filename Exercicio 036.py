# Emprestimo Bancário
'''preco = float(input('Qual o valor do imóvel'))
sal = float(input('Qual o seu salário?'))
prazo = int(input('qual o prazo do financiamento?'))
salarioNovo = sal * 30 /100
prestacao = preco/prazo
if prestacao > salarioNovo:
    print('Seu finaciamento não foi aprovado')
elif prestacao <= salarioNovo:
    print('Seu financiamento foi aproovado, sua prestação é de {:.2f}'.format(prestacao))'''

# ver qual numero é o maior

'''n1 = int(input('Digite um numero'))
n2 = int(input('Digite um numero'))
if n1 > n2:
    print('o primeiro numero é o maior')
elif n2 > n1:
    print('o segundo numero é o maior')
else:
    print('não exite valor maior, os dois são iguais')'''

#Alistamento militar


'''from datetime import date

ano = int(input('que ano vc nasceu?'))
idade = date.today().year - ano
if idade < 18:
    print('Ainda não esta na hora de se alistar, faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Esta ma hora de se alistar')
else:
    print('Você já ´passou do prazo de se alistar a {} anos'.format(idade -18))'''

# Notas de alunos

'''nota1 = float(input('Nota 1'))
nota2 = float(input('Nota 2'))
media = (nota1 + nota2) / 2
if media < 5:
    print('Lamento, vc foi reprovado. sua nota final foi {}'.format(media))
elif media >= 5 and media < 7:
    print('Você esta de recuperação, sua nota foi{}'.format(media))
else:
    print("Parabéns você foi aprovado! sua media é {}".format(media))'''

#041 categoria natação

'''from datetime import date
ano = int(input("informe o ano do seu nascimento"))
idade = date.today().year - ano
if idade <= 9:
    print('você é da categoria MIRIM')
elif idade <= 14:
    print('Vc é da categoria INFANTIL')
elif idade <= 19:
    print('vc é da categoria JUNIOR')
elif idade <= 20:
    print('Vc é da categoria SENIOR')
else:
    print('Você é da categoria MASTER')'''

# Analisador de triângulos

'''r1 = float(input('informe o primeiro angulo'))
r2 = float(input('informe o segundo angulo'))
r3 = float(input('Informe o terceiro angulo'))
if r1 > r2 + r3 or r2 > r1+r3 or r3 > r1 + r2:
    print('Não é possivel formar um trinagulo com essas retas')
elif r1 == r2 and r2 == r3:
    print('Este é um triangulo EQUILATERO')
elif r1 == r2 or r1 == r3 or r3 == r2:
    print('Esse é um triangulo ISÓSCELES')
else:
    print('Esse é um triangulo ESCALENO')'''

#043 Calculo IMC

'''alt = float(input('qual a sua altura'))
peso = float(input('qual o seu peso'))
imc = peso / alt **2
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc <= 40:
    print('obesidade')
else:
    print('obesidade mórbida')
'''

# calculando descontos progressivos


'''valor = float(input('Valor do produto'))
pagamento = int (input('1- chque  2-Debito , 3- cartao 2x, 4- parcelado'))
cheque = valor - (valor * 10 / 100)
debito = valor - (valor * 5 / 100)
cartao2x = valor
parcelado = valor + (valor * 20 / 100)
print(cheque, debito,cartao2x, parcelado)
if pagamento == 1:
    print('Voce tem 10% de desconto, seu produto fica por {}'.format(cheque))
elif pagamento == 2:
    print('vc tem 5% de desconto, valor do produto é {}'.format(debito))
elif pagamento == 3:
    print('não tem desconto, valor normal {}'.format(cartao2x))
else:
    print('o valor parcelado é {}'.format(parcelado))'''