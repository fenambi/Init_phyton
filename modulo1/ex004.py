# Um programa que recebe um valor e diz se pertence a que tipo

valor = input('digite algo: ')
print(type(valor))
print('e numerico: ', valor.isnumeric())
print('e alfanumerico: ', valor.isalnum())
print('e alfabeto: ', valor.isalpha())
print('e decimal: ', valor.isdecimal())
print('e espaco: ', valor.isspace())
print('e maiuscula: ', valor.isupper())
print('e miniscula: ', valor.islower())