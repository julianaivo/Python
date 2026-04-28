# 📘 Teoria — Aula 06
Este arquivo reúne os conceitos apresentados na aula 06, abordando os fundamentos da entrada de dados, tipos primitivos do Python e algumas formas básicas de manipulação e exibição de informações. O objetivo é servir como material de apoio para revisão e consulta rápida durante os estudos.

## Entrada de dados

input('entre aspas simples por padrão/convenção')

## Variáveis

n1 → variável  
a → variável

## Tipos primitivos

int → números inteiros: positivos, negativos ou nulo. Ex: 7, -4, 0, 9875.

float → números real: números com casas decimais. O python utiliza o ponto (.) para separar as casas decimais. Ex: 4.5, 0.076, -15.223, 7.0

bool → só aceita dois valores(True ou False). Quando utilizado, a primeira letra maiúscula (capitalized): T ou F

str → palavras, sempre entre aspas simples ou duplas. Por convenção, no python usa-se as aspas simples. Pode ser uma string vazia. Ex: "olá", '7.5', ''.

## Formas de utilizar o print:

print('A soma vale,' s)

print('A soma vale {}'.format{s})

print(f'A soma vale {s}')

## Exemplo passado em aula:

n = float(input('Digite um valor: '))  
print(n)

❗Obs: se colocar o *type()* dentro do *print()* aparece o tipo que aquela variável é. Exemplo:

n = float(input('Digite um valor: '))  
print(type(n))

Esse código nos retornaria:   
    <class 'float'>    
Mas segue a mesma ideia para as outras classes, por exemplo:

n = input('Digite um valor: ')  
print(type(n))

Retorno:  
    <class 'str'>

❗Obs: o *input*, por *default* retorna *string*. Ou seja, se eu quiser que apareça o tipo primitivo, devo por para que haja a devida conversão.

n = bool(input('Digite um valor: '))  
print(type(n))

Retorno:  
    <class 'bool'> 

⁉️'Mas booleano não é só True ou False?'

Lembre-se, estou retornando o **tipo** de variável. Agora, se formos escrever 'n', teremos:

n = bool(input('Digite um valor: '))  
print(n)

Retorno:  
    True

Mas, por que? O valor booleano só aceita verdadeiro e falso, nesse caso há a seguinte interpretação: 

Tem um valor dentro?    
Sim → True

É nulo?  
Sim → False

Ou seja, se houver valor = True.

## Outros métodos que podemos utilizar dentro do print(). Seguem alguns exemplos:

    n = (input('Digite um valor: '))  
    print(n.isnumeric()) 

    n = (input('Digite um valor: '))  
    print(n.isalfa())

    n = (input('Digite um valor: '))  
    print(n.isalnum())

    n = (input('Digite um valor: '))  
    print(n.isupper())

    n = (input('Digite um valor: '))  
    print(n.islower())

Esses métodos ajudam na validação e análise de dados fornecidos pelo usuário. Há vários outros métodos que podem ser utilizados. 