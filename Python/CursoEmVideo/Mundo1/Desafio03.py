'''Crie um script python que leia dois números e tente mostrar a soma entre eles.'''

#se não colocar o int() na frente do input, o programa irá concatenar os números ao invés de somá-los, pois o input() retorna uma string. Exemplo: se o usuário digitar 2 e 3, o resultado será 23 ao invés de 5.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

soma = n1 + n2

print(f'A soma é {soma}.')