# 📘 Teoria — Aula 09
Este arquivo reúne os conceitos apresentados na aula 09, abordando os fundamentos das operações com String no Python. As principais operações são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join(). O objetivo é servir como material de apoio para revisão e consulta rápida durante os estudos.

## Cadeia de caracter ou cadeia de texto

        'Curso em vídeo'  

Qualquer linguagem de programação chama isso de cadeia de carcter e um outro nome muito utilizado é *String*. Para o *Python* toda cadeia de texto está dentro de aspas simples ou aspas duplas. Também há a possibilidade de utilizar aspas triplas, mas isso seá visto mais pra frente. Iremos aprender modos de manipular essa cadeia de caracteres para podermos ter funcionalidades específicas.  

## Exemplos

Forma de atribuição de uma *string* em *Python*:  

        frase = 'Curso em Vídeo Python'  

Quando fazemos esse tipo de atribuição, o *Python* coloca esses dados na memória do computador, mas essa frase não vai inteira. O *Python* cria mini espaços dentro da memória do computador e dentro de cada mini espaço desse, ele vai colocar cada um dos caracteres. Cada mini espaço vai receber um **índice**. Ex:  

        ```frase
        ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
        │ C │ u │ r │ s │ o │   │ e │ m │   │ V │ í │ d │ e │ o │   │ P │ y │ t │ h │ o │ n │
        └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
        0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
        ```


## Fatiamento

Fatiar uma *string* é conseguir pegar pedaços dela. No *Python*, o fatiamento fica muito simples para ser tratado. Vamos començar de forma bem simples, se mandarmos escrever, por exemplo:  

frase[9]  

O símbolo de colchetes [] é o identificador de uma estrutura de daos no Python chamada lista.  

Se mandarmos escrever, por exemplo:   

        print(frase)
        ↪ Curso em Vídeo Python  

Mas se mandarmos:  

        frase[9]  
        ↪ V  

Irá retornar apenas o caracter de índice 9.  

Mas existem outras formas de fatiar que podem ser úteis em outras situações. Ex:  

        frase[9:13]  
        ↪ Víde  

Nesse caso, ele pegará do 9 até o 13, só o que o 13 ele irá excluir! O índice 13 não será mostrado, é sempre um a menos. Ou seja, pega do 9 até o 13, incluindo o 9 e removendo o 13.  
Então, e se quisermos pegar até o "o" da palavra "Vídeo"? Aí temos que fazer da seguinte forma:  

        frase[9:14]
        ↪ Vídeo  

Será que dá erro se fizermos:  

        frase[9:21]

Não é a melhor forma de fazer o fatiamento, mas não dará erro apesar desse índice não existir. Pense comigo, se colocamos o frase[9:13] e ele retornou apenas do índice 9 até o 12, nesse caso então ele retornaria do índice 9 até o 20.  

Outra forma de fatiar seria:

        frase[9:21:2]  

Quando escrevemos dessa forma estamos informando o seguinte: Vai começar no índice 9 e vai até o 21 (como no caso anterior) mas com um diferencial, o 2 nesse caso siginifica que irá do 9 até o 21 pulando de 2 em 2. Ou seja, retornaria o seguinte:  

        frase[9:21:2]
        ↪ Vdopto  

Se colocarmos agora da seguinte forma:  

        frase[:5]  

Até então estávamos acostumados a sempre ver frase[índice:índice] mas, e agora? Quando não há índice na frente, o *Python* vai pegar do início até o índice que foi delimitado, nesse caso, o 5. Então temos:  

        frase[:5]
        ↪ Curso  

Para completar o racioncínio, vamos de mais um exemplo:  

        frase[15:]  

Na mesma linha do exemplo anterior, temos: foi delimitado o índice de início mas o índice de término não foi informado. Isso indica que o fatiamento irá ocorrer do índice 15 até o final da *string*. Resultando em:  

        frase[15:]
        ↪ Python  

Com esses exemplos podemos notar que, de forma simples, o fatiamento se resume a:  

        frase[índice de início : índice de final : intervalo]  


## Análise

Analisar um *string* é saber algumas informações sobre ela. Saber o tamanho, o número de caracters, com que letra começa, entre outras coisas.  

Segue alguns exemplos de métodos que podemos utilizar para analisar uma *string*.  

        len(frase) → analisar o comprimento de uma *string*.  

        frase.count('o') → conta quantas vezes aparece a letra 'o'.  

        frase.count('o', 0, 13) → faz uma contagem já com o fatiamento.  

        frase.find('deo') → ele vai informar quantas vezes encontrou 'deo', vai indicar onde começa. Nesse caso, informaria 11.  

        frase.find('Android') → nesse caso, retornaria -1 já que não há essa *string* que foi passada no método find na *string* que está sendo analisada. Não foi encontrada.  

        'Curso' in frase → o operador 'in' vai informar o seguinte: existe 'curso' em frase? Sim. Então ele vai retornar Ture.

## Transformação

Via de regra, uma listra de *string* é imutável mas é possível mudar ela atravéz dos métodos.

        frase.replace('Python','Android')  → substitui   

Nesse caso, o próprio *Python* complenta o índice que faltaria na lista.  

        frase.upper() → método que mantém o que está em maiúsculo e torna tudo que está em minúsculo em maiúsculo.

        frase.lower() → método que mantém o que está em minúsculo e torna tudo que está em maiúculo em minúsculo.

        frase.capitalize() → método que torna toda a string em minúsculo e só o primeiro caracter vai ficar em maiúsculo.

        frase.title() → analisa quantas palavras tem uma string pela posição dos espaços, ele vai fazer o capitale agora palavra por palavra. Ou seja, o primeiro caracter (letra) de cada palavra será maiúsculo.  

Vamos mudar a *string* agora para analisamos outras funcionalidades. Utilizaremos a seguinte:  

        ```frase
        ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
        │   │   │   │ A │ p │ r │ e │ n │ d │ a │   │ P │ y │ t │ h │ o │ n │   │   │   │   │
        └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
        0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
        ```    

Podemos explorar outras formas de transformar, são elas:    

        frase.strip() → remove todos os espaços inúteis, os primeiros e os últimos.  

        frase.rstrip() → remove todos os espaços a direita (r) mas mantém os da esquerda.  

        frase.lstrip() → remove os espaços da esquerda (l) mas mantém os da direita.  

## Divisão

Vamos retornar a *string* inicial de exemplo para vermos algumas funcionalidades de divisão:  


        ```frase
        ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
        │ C │ u │ r │ s │ o │   │ e │ m │   │ V │ í │ d │ e │ o │   │ P │ y │ t │ h │ o │ n │
        └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
        0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
        ```

Algumas opções que temos:  

        frase.split() → por padrão, o slipt é feito em seus espaços. Basicamente ele vai pegar onde tem espaço e vai criar uma divisão, um split. Ele refez os índices, cada palavra recebe uma indexação nova. Ou seja, o split gera uma lista com todas as palavras de uma cadeia de caracters.  

        '-'.join(frase) → cosniderando a strig separada pelo split (do exemplo anterior): ele vai juntar todos os elementos de frase e vai usar o separador '-', gerando uma string única em uma cadeia de caracter.  


## Exemplos passados em aula:  


        frase = 'Curso em Vídeo Python'

        print(frase)  
        ↪ Curso em Vídeo Python  

        print(frase[3])  
        ↪ s  

        print(frase[3:13])  
        ↪ so em Víde  

        print(frase[:13])  
        ↪ Curso em Víde  

        print(frase[13:])  
        ↪ o Python  

        print(frase[1:15:2])  
        ↪ us mVdo  

        print(frase[1::2])  
        ↪ us mVdoPto  

        print(frase[::2])  
        ↪ Croe íe yhn  

        print(frase.count('o'))  
        ↪ 3  

        print(frase.count('O'))  
        ↪ 0  

        print(len(frase))  
        ↪ 21  

        print(frase.split())  
        ↪ ['Curso', 'em', 'Vídeo', 'Python']  
