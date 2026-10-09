# Um programa que recebe um numero e imprime o seu antecessor e o seu sucessor

num = int(input("digite um numero: "))
suc = num + 1
ante = num - 1
print('O seu sucessor é: {} \nO seu antecessor é: {}'.format(suc, ante))