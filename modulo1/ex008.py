# ecreva um prograna que leia um valor em metros e o exiba convertido em centimetro e milicentro


valor = float(input('Digite o valor: '))
centimetro = valor * 100
milicentro = valor * 1000
print(valor, 'metros e igual a {} centimetros'.format(centimetro))
print(valor, 'metros e igual a {} milimetros'.format(milicentro))