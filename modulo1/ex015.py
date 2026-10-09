#escreve um programa que pergunte a quantidade de KM
#percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preco a pagar,
#sabendo que custa 60kzs por diaa e 0.15 por km rodado

km = float(input('Quantos km rodar o carro? '))
dia_alugado =int(input('Quantos dias alugados? '))
valor_por_dia = dia_alugado * 60
valor_por_km = 0.15 * km
total = valor_por_dia + valor_por_km
print('O valor a pagar e de {}'.format(total))