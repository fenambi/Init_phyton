# Um programa que recebe um numero e imprime o dobro, triblo e a raiz quadrada do mesmo

num = int(input("digite um numero: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('Seu dobro e: {}\nSeu triplo e: {}\nSua raiz e: {}'.format(dobro, triplo, raiz))