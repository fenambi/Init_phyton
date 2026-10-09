#faca um programa que leia a largura e a altura
#de uma parede em metros, calcula a area e quantidade de tinta necessaria
#para pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
tinta = area / 2
print('a area da parede de {}m'.format(area))
print('A quantidade de tinta necessaria e de {}L'.format(tinta))