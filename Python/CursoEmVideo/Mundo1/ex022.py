'''Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas e minúsculas.

- Quantas letras ao todo (sem considerar espaços).

- Quantas letras tem o primeiro nome.'''

nome = str(input('Informe seu nome completo: ')).strip()    #já pode utilizar essa função aqui direto para remover os espaçoes inúteis

print('Analisando seu nome...')

print('Seu nome em maiúsculas é ', nome.upper())
print('Seu nome em minúsculas é ', nome.lower())

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#outra forma de fazer o último print.
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

