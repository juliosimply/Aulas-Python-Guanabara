# Exercicio 10 Conversão de moedas

real = float(input("quanto em reais você deseja converter para dolares "))
dolar = float (real /5.37)
euro = float( real / 6.47)
libra = float(real/ 7.38)
print('o valor convertido de {:.2f} reais convertido em dolares : \n da {:.2f} em dolares,\n em Euro da {:.2f} euros,\n em Libras da {:.2f} libras'.format(real, dolar, euro, libra))
