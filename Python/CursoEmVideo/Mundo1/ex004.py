'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre 
ele.'''

a = input('Digite algo:')

print('O tipo primitivo desse valor é:', type(a)) #Analisa o tipo primitivo.
print('Só tem espaçoes?', a.isspace()) #Analise se é composto por apenas espaços.
print('É um número?', a.isnumeric()) #Analise se é composto por completamente por números.
print('É alfabético?' , a.isalpha()) #Analise se é composto por completamente por letras.
print('É alfanumérico?', a.isalnum()) #Analise se é composto por letras ou números, ou ambos.
print('Está em maiúsculas?', a.isupper()) #Analise se todas as letras estão em maiúsculas.
print('Está em minúsculas?', a.islower()) #Analise se todas as letras estão em minúsculas.
print('Está capitalizada?', a.istitle()) #Analisa se a primeira letra de cada palavra é maiúscula e as outras são minúsculas.