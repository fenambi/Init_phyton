#faca um programa que leia o preco de um produto e mostre seu
#novo preco com 5% de disconto
from markdown_it.common.normalize_url import validateLink

volor = float(input('digite o preco: '))
new_prece = volor - (volor * 0.05)
print('O preco com disconto de 5% e de {:.2f}'.format(new_prece))
