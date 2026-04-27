# 📘 Teoria — Aula 07
Este arquivo reúne os conceitos apresentados na aula 07, abordando os fundamentos dos operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. O objetivo é servir como material de apoio para revisão e consulta rápida durante os estudos.


## Operadores Aritméticos

+ → adição
- → subtração
* → multiplicação
/ → divisão
** → potência
// → divisão inteira
% → resto da divisão (módulo)

## Exemplos

Todo operador precisa de operandos! Esses são operadores binários, ou seja, precisa de dois operandos.

5 + 2 == 7                  5 ** 2 == 25
                  
5 - 2 == 3                  5 // 2 == 2

5 * 2 == 10                 5 % 2 == 1

5 / 2 == 2.5

❗Obs: Quando queremos testar se uma coisa é igual a outra, nós utilizaremos dois símbolos de igual. Lembre-se: 1 símbolo de igual significa "recebe".

## Ordem de precedência

1. () → No Python, utilizamos apenas os parênteses para expressões aritmétcas. Mas podemos ter parênteses dentro de parênteses.

2. ** 

3. *, /, //, % → Multiplicação, divisão, divisão interia, resto da divisão. Faz por ordem de aparição.

4. +, - → Adição e subtração.

## Exemplo passado em aula:

1. 5 + 3 * 2 == **11**

↪ 3 * 2 == 9
↪ 9 + 5 == 11

2. 3 * 5 + 4 ** 2 == **31**

↪ 4 ** 2 == 16
↪ 3 * 5 == 15
↪ 15 + 16 == 31

3. 3 * (5 + 4) ** 2 == **243**

↪ (5 + 4) == 9
↪ 9 ** 2 == 81
↪ 3 * 81 == 243

## Outros formas de realizar operações. Seguem alguns exemplos:

4 ** 3 == 64
↪ pow (4,3) #função interna

round(x, n): arredonda um número *x* para *n* dígitos após a vírgula
↪ round(34.56789, 2) == 34.56

abs(x): Retorna o valor absoluto (módulo) de um número
↪ abs(-8) == 8

Essas funções internas matemáticas, também chamadas de *b   uilt-in* também realizam as operações que os operadores aritméticos realizam. Contudo, com as funções internas, perde-se a ordem de precedência vista anteriormente.❗

## Outros exemplos passados na aula:

n1 = int(input('Digite um valor:))
n2 = int(input('Digite outro valor:))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d)) #divisão com apenas 3 casas decimais, o que devo fazer?
print('Divisão inteira é {} e potência é {}'.format(di, e))

↪ solução para o #
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))

⁉️ Tem como manipular o print dessa forma???
SIM, podemos manipular o print de algumas formas!

## Manipulação do print

\n → quebra de linha no print.
↪ Ex: print('A quebra de linha é muito útil \n para evitar criar vários prints no \n corpo do código.')

end='' → para não haver quebra de linha no final do print.
↪ Ex: print('Quero continuar essa linha de código', end='   ') #coloquei 3 espaços entre as aspas simples
    print('no outro print')

    retorno: Quero continuar essa linha de código   no outro print

❗Obs: podemos juntar os prints com o *end=''* deixando zero espaços entre eles, deixando espaços entre eles (como foi o caso do exemplo anterior) ou preenchendo com outros caracteres. 

Ex: print('Meu nome é ', end='>>>>>')
    print('Juliana Ivo')

retorno: Meu nome é >>>>>Juliana Ivo

→ Caracters e alinhamento 

nome = input(('Qual seu nome?')) #Juliana
print('Prazer em te conhecer, {}!'.format(nome))

retorno esperado: Prazer em te conhecer, Juliana! 

Como poderíamos manipular esse print:

print('Prazer em te conhecer, {:20}!'.format(nome)) # o nome aparece em 20 caracteres. ou seja, escreve Juliana em 20 espaços.
↪ retorno: Prazer em te conhecer, Juliana            ! #escreveu Juliana e 20 espaços

print('Prazer em te conhecer, {:>20}!'.format(nome)) # utilizando alinhamento a direita
↪ retorno: Prazer em te conhecer,             Juliana!

print('Prazer em te conhecer, {:<20}!'.format(nome)) # utilizando alinhamento a esquerda
↪ retorno: Prazer em te conhecer, Juliana            !

print('Prazer em te conhecer, {:^20}!'.format(nome)) # utilizando alinhamento centralizado
↪ retorno: Prazer em te conhecer,       Juliana      !

print('Prazer em te conhecer, {:=^20}!'.format(nome)) # utilizando alinhamento centralizado
↪ retorno: Prazer em te conhecer, ======Juliana======!