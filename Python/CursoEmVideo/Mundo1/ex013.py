'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Qual o salário do funcionário? R$'))

salario_novo = salario * 1.15 #(aumento de 15%)

print('Um funcionário que ganahva R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, salario_novo))