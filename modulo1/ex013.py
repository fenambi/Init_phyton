#faca um algoritmo que leia o salaria de um funcionario e
#mostre seu novo salario com 15% de aumento

salary = float(input('digite o salario actual: '))
new_salary = salary + (salary * 0.15)
print('O novo salario com 15% de aumento e de {:.2f}'.format(new_salary))
