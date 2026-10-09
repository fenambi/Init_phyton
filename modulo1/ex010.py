#crie um programa que leia quanto dinheiro tem na carteira
#e mostre quantos dolares ela pode comprar

valor = float(input('Digite quantos kzs tens: '))
dolares = valor / 913
print('com', valor, ' voce pode comprar {:.2f} dolares'.format(dolares))