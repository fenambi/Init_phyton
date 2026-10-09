#ecreve um programa que converta uma
#temperatura digitada em ºC e converta em ºF

c = float(input('digite a temperatura em Celsius: '))
f = c * 1.8 + 32
print('A temperatura de {}ºC, coresponde {}ºF'.format(c, f))