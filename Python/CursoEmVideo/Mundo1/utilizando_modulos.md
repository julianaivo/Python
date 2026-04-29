# 📘 Teoria — Aula 08
Este arquivo reúne os conceitos apresentados na aula 08, abordando como utilizar módulos em *Python* utilizando os comandos import e from/import no *Python* e, também, como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi. O objetivo é servir como material de apoio para revisão e consulta rápida durante os estudos.

## Módulos

Por padrão, o *Python* já vêm com uma série de funcionalidades instaladas.  

É como se fossem adicionais. Por exemplo: Temos um carro básico. Com o tempo, podemos adicionar um ar-condicionado, um tapete novo, etc. A ideia é: colocar coisas para adicionar funcionalidades.  

Outro exemplo, imagine três grupos: 

|   bebidas  | comidas   | doces    |
| :--------: | :-------: | :------: |
|     🧃     |   🍕     |    🧁   |
|     ☕     |   🥩     |    🍰   |
|     🍹     |   🥪     |    🍩   |
|     🧋     |   🍿     |    🍨   |  

Esses seriam os adicionais que poderiamos ter no dia a dia do ser humano, comulmente consumimos esses alimentos para nos dar energia ao longo do dia. Esses recursos não são padronizados e não estão imbutidos na gente, precisamos adicionar esses *"módulos"* para fazer as atividades do dia.  

Imagine cada um desses grupos (bebidas, comidas, doces) como **bibliotecas**.  

Dentro da linguagem *Python*, para incluir alguam coisa, temos que utilizar o *import*. Então se quiséssemos incluir algo, poderíamos fazer:

        import bebidas  

            🧃☕🍹🧋

        import doces  

            🧁🍰🍩🍨

Cada *import* desses, importa todos os itens dentro do grupo (biblioteca). Ou seja, com os *import*, podemos utilizar todos os itens dentro do grupo.  

Mas e se só quisermos um item da biblioteca? 🧐  

Para fazer essas importações únicas, nós fazemos uma alteração no momento da importação. 

        from comidas import pizza  

            🍕

Então temos que: existem duas maneiras básicas de importar módulos dentro do *Python*. A primeira maneira é mais generalista e a segunda é mais específica, economizando um pouco mais a memória.  


## Exemplo de biblioteca

1. math → Quando importamos a biblioteca *math*, ela permite o uso de diversas funcionalidades extras. Por exemplo, temos algumas funcionalidades nessa biblioteca que são muito utilizadas. Ex:  
    ↪ ceil (Podemos utilizar em uma operação que é necessário o arredondamento para cima)  
    ↪ floor (Podemos utilizar em uma operação que é necessário o arredondamento para baixo)  
    ↪ trunc (Podemos utilizar em uma operação para eliminar da vírgula pra frente, descartando dígitos indesejados. Apenas irá truncar)  
    ↪ pow (Podemos utilizar em uma operação para realizar o cálculo da potência)  
    ↪ sqrt (Podemos utilizar em uma operação para calcular a raiz quadrada)  
    ↪ factorial (Podemos utilizar em uma operação para calcular o fatorial de um número)  

Ou seja, relembrando, se quisermos importar todas as funcionalidades, devemos importar da seguinte forma:  

        import math  

Mas, e se quisermos utilizar apenas uma funcionalidade? Então teremos:  

        from math import sqrt  

Eita, então tenho que importar uma por uma se eu for utilizar duas ou três?  
Não❗  

Podemos, também, importar da seguinte maneira:  

        from math import sqrt, pow  

Se houver necessidade de importar mais de um item, pode fazê-lo separando as funcionalidades com vírgula.  

## Parte prática da aula

1. Mostrar a raiz quadrada de um número.  

        import math  

        num = int(input('Digite um número: '))  

        raiz = math.sqrt(num)  

        print('A raiz de {} é igual a {}.'.format(num, raiz))  

Outra forma de fazer esse mesmo exercício seria:  

        from math import sqrt  

        num = int(input('Digite um número: '))  

        raiz = sqrt(num)  #oberserve que não é necessário o "math."

        print('A raiz de {} é igual a {}.'.format(num, raiz))  

Quando utilizamos dessa maneira, o *Python* já traz o método direto para a pasta. Ou seja, não é necessário utilizar a referência *math.* + a função.  


## Quais são as bibliotecas existentes?

São inúmeras as bibliotecas existentes, mas aqui está o link para a documentação que trata a respeito desse tópico.  

[A Biblioteca Padrão do Python](https://docs.python.org/pt-br/3.13/library/index.html#the-python-standard-library)  

Se digitarmos na IDE *import* e pressionarmos ctrl + tecla de espaço, podemos visualizar todas as bibliotecas disponíveis.  

É importante lembrar que também existe o **PyPI** — the Python Package Index.  

Certo, mas o que é isso?   
É um índice de pacotes **extras**, ou seja, é uma lista de módulos que podem ser importados separadamente. Qualquer pessoa pode criar um pacote/módulo e disponibilizar isso para os outros usuários do *Python*.  

Vamos utilizar de exemplo a biblioteca "emoji". Ela serve para mostrar emojis.  

Se dermos um *import emoji* na IDE resultará em erro pois ela não está instalada no computador. Mas ela pode ser importada, para isso devemos:  

1. Devemos instalar a biblioteca.  
    ↪ A forma mais comum de instalar bibliotecas PyPI no *Python* é usando o gerenciador de pacotes *pip* diretamente no terminal/prompt de comando com o comando:
    
            pip install nome_da_biblioteca 
            
    Para garantir a instalação no ambiente *Python* correto, utilize no Windowns: 
    
            python -m pip install nome_da_biblioteca

2. Devemos importar a biblioteca no código, dentro da IDE.  
3. Devemos utilizar a funcionalidade.  