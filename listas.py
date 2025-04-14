#lista é uma estrutura versártil de dados que permite armazenar uma coleção de itens em uma única variável.
# As listas podem conter elementos de diferentes tipos, como números, strings e até outras listas.
# Elas são definidas usando colchetes [] e os elementos são separados por vírgulas.
# Por exemplo:
lista = [1, 2, 3, 4, 5]
print("Lista:", lista) # a saída será uma lista de números inteiros, pois não foi definida o tipo antes.

# Retorno de um elemento específico da lista usando o índice.
# Os índices começam em 0, então o primeiro elemento tem o índice 0, o segundo elemento tem o índice 1 e assim por diante.
# Por exemplo:
elemento = lista[2] # Isso retorna o terceiro elemento da lista, que é 3.
print("Elemento na posição 2:", elemento) # a saída será: 3

# Diferente das Strings, que são imutáveis, as listas são mutáveis, o que significa que você pode alterar seus elementos.
#Por exemplo:
lista = [1, 2, 3, 4, 5]
lista[0] = 10 # Isso altera o primeiro elemento da lista para 10.
print("Lista após alteração:", lista) # a saída será: 10, 2, 3, 4, 5

# Como as strings as listas podem ser fatiadas usando o operador de fatiamento [start:end:step].
# Por exemplo:
lista = [1, 2, 3, 4, 5]
fatiada = lista[1:4] # Isso retorna os elementos do índice 1 ao 3 (o índice final é exclusivo).
print("Lista fatiada:", fatiada) # a saída será: 2, 3, 4
# você também pode fatiar com números negativos.
# Por exemplo:
fatiada_negativa = lista[-4:-1] # Isso retorna os elementos do índice -4 ao -2 (o índice final é exclusivo).
print("Lista fatiada negativa:", fatiada_negativa) # a saída será: 2, 3, 4
#Você também pode usar o operador de fatiamento para inverter a lista.
# Por exemplo:
inversa = lista[::-1] # Isso retorna a lista invertida.
print("Lista invertida:", inversa) # a saída será: 5, 4, 3, 2, 1

# A Atribuição simples em Python não copia dados. quando você atribui uma lista a uma variável,  a variável se refere à lista existente.
# Quaisquer alterações feitas em uma variável afetará a lista original.
# Por exemplo:
lista1 = [1, 2, 3, 4, 5]
lista2 = lista1 # Isso atribui a lista1 à lista2.
# Agora, ambas as variáveis se referem à mesma lista.
lista2.append(6) # Isso adiciona o número 6 à lista2.
# Como lista1 e lista2 se referem à mesma lista, a alteração também afeta a lista1.
print("Lista1 após adicionar 6:", lista1) # a saída será: 1, 2, 3, 4, 5, 6

# Atribuiação a fatias também é possível.
# isso até pode alterar o tamanho da lista ou remover todos os itens dela.
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista2=lista # Isso atribui a lista à lista2.
# Agora, ambas as variáveis se referem à mesma lista.

# Isso substitui os elementos do índice 1 ao 2 (o índice final é exclusivo) por 10 e 20.
lista2[1:3] = [10, 20]
print("Lista após atribuição a fatias:", lista) # a saída será: 1, 10, 20, 4, 5
# isso remove os elementos do índice 1 ao 2 (o índice final é exclusivo).
lista2[1:3] = []
print("Lista após remover elementos:", lista) # a saída será: 1, 4, 5
#Isso remove todos os elementos da lista.
lista2[:] = [] # Isso remove todos os elementos da lista.
print("Lista após remover todos os elementos:", lista) # a saída será: []




# Metodos e Manipulação de listas:

# Operadores

#concatenação e repetição.
# Você pode concatenar duas listas usando o operador +.
# Por exemplo:
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8]
lista_concatenada = lista1 + lista2 # Isso retorna uma nova lista que contém todos os elementos de ambas as listas.
print("Lista concatenada:", lista_concatenada) # a saída será: 1, 2, 3, 4, 5, 6, 7, 8
# Você também pode repetir uma lista usando o operador *.
# Por exemplo:
lista_repetida = lista1 * 2 # Isso retorna uma nova lista que contém os elementos da lista original repetidos duas vezes.
print("Lista repetida:", lista_repetida) # a saída será: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5


# Verificadores

# in 
# Você  pode verificar se um elemento está na lista usando o operador in.
# Por exemplo:
lista = [1, 2, 3, 4, 5]
elemento_existe = 3 in lista # Isso verifica se o número 3 está na lista.
print("O elemento 3 está na lista?", elemento_existe) # a saída será: True
#not in
# Você também pode usar o operador not in para verificar se um elemento não está na lista.
# Por exemplo:
elemento_nao_existe = 6 not in lista # Isso verifica se o número 6 não está na lista.
print("O elemento 6 não está na lista?", elemento_nao_existe) # a saída será: True


# Métodos de Adição

#Método append()
#Você  pode adicionar novos elementos à lista usando o método append().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.append(6) # Isso adiciona o número 6 ao final da lista.
print("Lista após adicionar 6:", lista) # a saída será: 1, 2, 3, 4, 5, 6

# Você também pode fazer operações dentro de um parâmetro do append().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.append(lista[0] + lista[1]) # Isso adiciona a soma do primeiro e segundo elemento da lista ao final da lista.
print("Lista após adicionar a soma do primeiro e segundo elemento:", lista) # a saída será: 1, 2, 3, 4, 5, 3


#Método insert()
# Você pode adicionar novos elementos à lista usando o método insert().
# Por Exemplo:
lista = [1, 2, 3, 4, 5]
lista.insert(2, 10) # Isso adiciona o número 10 na posição 2 da lista.
# A sintaxe do insert() é: lista.insert(posição, elemento).
# A posição é o índice onde o elemento será inserido e o elemento é o valor que você deseja adicionar.
print("Lista após adicionar 10 na posição 2:", lista) # a saída será: 1, 2, 10, 3, 4, 5


# Nota: A diferença entre o append() e o insert() é que o append() adiciona o elemento ao final da lista,
# enquanto o insert() adiciona o elemento em uma posição específica.


# Método extend()
# Você pode adicionar vários elementos à lista usando o método extend().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.extend([6, 7, 8]) # Isso adiciona os números 6, 7 e 8 ao final da lista.
# A sintaxe do extend() é: lista.extend(iterável).
# O iterável pode ser uma lista, tupla ou qualquer outro objeto que possa ser percorrido.
# O método extend() não retorna nada.
# Após usar o método extend(), a lista original será alterada.
print("Lista após adicionar 6, 7 e 8:", lista) # a saída será: 1, 2, 3, 4, 5, 6, 7, 8



# Método de remoção

# Método remove()
# Você pode remover elementos da lista usando o método remove().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.remove(3) # Isso remove o número 3 da lista.
# A sintaxe do remove() é: lista.remove(elemento).
# O elemento é o valor que você deseja remover.
# Se o elemento não estiver na lista, ocorrerá um erro.
print("Lista após remover 3:", lista) # a saída será: 1, 2, 4, 5


# Método pop()
# Você pode remover elementos da lista usando o método pop().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.pop() # Isso remove o último elemento da lista.
# A sintaxe do pop() é: lista.pop(posição).
# A posição é o índice do elemento que você deseja remover.
# Se você não especificar a posição, o último elemento será removido.
print("Lista após remover o último elemento:", lista) # a saída será: 1, 2, 3, 4
# O método pop() também retorna o elemento removido.
# Por exemplo:
elemento_removido = lista.pop(1) # Isso remove o elemento na posição 1 da lista e armazena o valor na variável elemento_removido.
print("Elemento removido:", elemento_removido) # a saída será: 2
print("Lista após remover o elemento na posição 1:", lista) # a saída será: 1, 3, 4


# Método clear()
# você pode remover todos os elementos da lista usando o método clear().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.clear() # Isso remove todos os elementos da lista.
# A sintaxe do clear() é: lista.clear().
# O método clear() não retorna nada.
# Após usar o método clear(), a lista ficará vazia.
print("Lista após remover todos os elementos:", lista) # a saída será: []

# Método de Busca e contagem

# Método index()
# Você pode encontrar o índice de um elemento na lista usando o método index().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
indice = lista.index(3) # Isso retorna o índice do número 3 na lista.
# A sintaxe do index() é: lista.index(elemento).
# O elemento é o valor que você deseja encontrar.
# Se o elemento não estiver na lista, ocorrerá um erro.
print("Índice do elemento 3:", indice) # a saída será: 2

# Método count()
# Você pode contar quantas vezes um elemento aparece na lista usando o método count().
# Por exemplo:
lista = [1, 2, 3, 4, 5, 3]
contagem = lista.count(3) # Isso conta quantas vezes o número 3 aparece na lista.
# A sintaxe do count() é: lista.count(elemento).
# O elemento é o valor que você deseja contar.
# Se o elemento não estiver na lista, o método retornará 0.
print("Contagem do elemento 3:", contagem) # a saída será: 2

# Método de ordenação

# Método sort()
# Você pode ordenar os elementos da lista usando o método sort().
# esse metodo ordena a lista original, ou seja, modifica a própria lista e não retorna uma nova lista.
# Por padrão, o método sort() ordena os elementos em ordem crescente.
# Ela também pode ordenar strings em ordem alfabética.
# Por exemplo:
lista = [5, 3, 1, 4, 2]
lista.sort() # Isso ordena a lista em ordem crescente.
print("Lista ordenada:", lista) # a saída será: 1, 2, 3, 4, 5
#Importante: O método sort() modifica a lista original e não retorna uma nova lista.
# Por isso você não precisa atribuir o resultado a uma nova variável.
# se você fizer isso, a variável que você atribuiu o resultado não terá o valor esperado.
# Por exemplo:
lista = [5, 3, 1, 4, 2]
lista_ordenada = lista.sort() # Isso não funcionará como esperado.
print("Lista ordenada:", lista_ordenada) # a saída será: None
# Ordem decrescente:
# Você pode ordenar os elementos da lista em ordem decrescente usando o parâmetro reverse=True.
# Por exemplo:
lista = [5, 3, 1, 4, 2]
lista.sort(reverse=True) # Isso ordena a lista em ordem decrescente.
print("Lista ordenada em ordem decrescente:", lista) # a saída será: 5, 4, 3, 2, 1
#Ordenação personalizada:
# Você pode usar o parâmetro key para especificar uma função de comparação personalizada.
# Por exemplo:
lista = ['banana', 'maçã', 'laranja']
# Você pode usar o método sort() para ordenar a lista de acordo com o comprimento das strings.
lista.sort(key=len) # Isso ordena a lista em ordem crescente de comprimento.
print("Lista ordenada pelo comprimento das strings:", lista) # a saída será: ['maçã', 'banana', 'laranja']

# Método reverse:
# Você pode inverter a ordem dos elementos da lista usando o método reverse().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.reverse()# Isso inverte a ordem dos elementos da lista.
# A sintaxe do reverse() é: lista.reverse().
# O método reverse() não retorna nada.
# Após usar o método reverse(), a lista ficará invertida.
print("Lista invertida:", lista) # a saída será: 5, 4, 3, 2, 1
# O método reverse() modifica a lista original e não retorna uma nova lista.
# Por isso você não precisa atribuir o resultado a uma nova variável.
# Se você fizer isso, a variável que você atribuiu o resultado não terá o valor esperado.
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista_invertida = lista.reverse() # Isso não funcionará como esperado.
# print("Lista invertida:", lista_invertida) # a saída será: None
print("Lista invertida:", lista) # a saída será: 5, 4, 3, 2, 1

#Método copy():
# Você pode criar uma cópia da lista usando o método copy().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista_copia = lista.copy() # Isso cria uma cópia da lista.
# A sintaxe do copy() é: lista.copy().
# O método copy() retorna uma nova lista que é uma cópia da lista original.
# Após usar o método copy(), a lista original e a cópia serão independentes.
# Isso significa que alterações feitas na lista original não afetarão a cópia e vice-versa.
print("Cópia da lista:", lista_copia) # a saída será: 1, 2, 3, 4, 5

# Metodo sorted()
# Você pode ordenar os elementos da lista usando a função sorted().
# A diferença entre o método sort() e a função sorted() é que o método sort() modifica a lista original,
# enquanto a função sorted() retorna uma nova lista ordenada.
# Por exemplo:
lista = [5, 3, 1, 4, 2]
lista_ordenada = sorted(lista) # Isso retorna uma nova lista ordenada.
print("Lista ordenada:", lista_ordenada) # a saída será: [1, 2, 3, 4, 5]
# A lista original permanece inalterada.
print("Lista original:", lista) # a saída será: [5, 3, 1, 4, 2]
# A sintaxe do sorted() é: sorted(iterável, key=None, reverse=False).
# O iterável é a lista que você deseja ordenar.
# O parâmetro key é uma função de comparação personalizada (opcional).
# O parâmetro reverse é um booleano que indica se a lista deve ser ordenada em ordem decrescente (opcional).
# Por padrão, o parâmetro reverse é False, o que significa que a lista será ordenada em ordem crescente.
# A função sorted() não modifica a lista original.
# Por isso você precisa atribuir o resultado a uma nova variável.
# Se você não fizer isso, a variável que você atribuiu o resultado não terá o valor esperado.



# Funções Built-in
# Você pode usar funções built-in para manipular listas.


# Método len()
#Você pode saber o tamanho da lista usando a função len().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
print("Tamanho da lista:", len(lista)) # a saída será: 5


# Método min()
# Você pode encontrar o menor elemento da lista usando a função min().
# Por exemplo:
lista = [5, 3, 1, 4, 2]
minimo = min(lista) # Isso retorna o menor elemento da lista.
print("Menor elemento da lista:", minimo) # a saída será: 1


# Método max()  
# Você pode encontrar o maior elemento da lista usando a função max().
# Por exemplo:
lista = [5, 3, 1, 4, 2]
maximo = max(lista)
print("Maior elemento da lista:", maximo)# a saída será: 5


# Método sum()
# Você pode encontrar a soma dos elementos da lista usando a função sum().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
soma = sum(lista) # Isso retorna a soma dos elementos da lista.
print("Soma dos elementos da lista:", soma) # a saída será: 15  



# Aninhamento de Listas

# É possível aninhar listas, ou seja, criar listas dentro de listas.
# Por exemplo:
lista_aninhada = [[1, 2, 3], ['a',' b', 'c']]
# como funciona os índices em listas aninhadas?
# Para acessar um elemento em uma lista aninhada, você pode usar múltiplos índices.
# Por exemplo:
elemento_aninhado = lista_aninhada[0][1] # Isso retorna o segundo elemento da primeira lista aninhada, que é 2.
print("Elemento aninhado:", elemento_aninhado) # a saída será: 2
# Você também pode adicionar listas aninhadas usando o método append().
# Por exemplo:
lista_aninhada.append([4, 5, 6]) # Isso adiciona uma nova lista ao final da lista aninhada.
print("Lista aninhada após adicionar nova lista:", lista_aninhada) # a saída será: [[1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]]
# Você também pode adicionar listas aninhadas usando o método insert().
# Por exemplo:
lista_aninhada.insert(1, [7, 8, 9]) # Isso adiciona uma nova lista na posição 1 da lista aninhada.
print("Lista aninhada após adicionar nova lista na posição 1:", lista_aninhada) # a saída será: [[1, 2, 3], [7, 8, 9], ['a', 'b', 'c'], [4, 5, 6]]


# Percorrendo elementos de uma Lista

# Laço for:
# Você pode percorrer os elementos da lista usando um laço for.
# Por exemplo:
lista = [1, 2, 3, 4, 5]
for elemento in lista: # Isso percorre todos os elementos da lista.
    print("Elemento:", elemento) # a saída será: 1, 2, 3, 4, 5
# Você também pode usar o índice para percorrer os elementos da lista.
for i in range(len(lista)):
    print("Elemento pelo índice:", lista[i]) # a saída será: 1, 2, 3, 4, 5


# Laço while:
# Você pode percorrer os elementos da lista usando um laço while.
# Por exemplo:
lista = [1, 2, 3, 4, 5]
i = 0
while i < len(lista): # Isso percorre todos os elementos da lista.
    print("Elemento:", lista[i]) # a saída será: 1, 2, 3, 4, 5
    i += 1 # Incrementa o índice para percorrer o próximo elemento.




# Maneira Comapacta de criar grandes listas:

# Você pode criar listas grandes de maneira compacta usando a compreensão de listas.
# Por exemplo:
nova_lista = [x for x in range(10)] # Isso cria uma nova lista com os números de 0 a 9, pois o elemento do range(10) é exclusivo.
print("Nova lista:", nova_lista) # a saída será: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# outra opção:

quadrados = [x**2 for x in range(1,11)]# Irá mostrar os quadrados de 1 a 10.
print("Quadrados de 1 a 10:", quadrados) # a saída será: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Você também pode adicionar uma condição para filtrar os elementos.
# Por exemplo:
nova_lista = [x for x in range(10) if x % 2 == 0] # Isso cria uma nova lista com os números pares de 0 a 9.
print("Nova lista com números pares:", nova_lista) # a saída será: [0, 2, 4, 6, 8]





#Funções úteis para listas:






#Isso foi um pouco sobre listas em Python.
#Para treinar fica esse desafio:
# Gerenciador de Tarefas
# Crie um programa que permita ao usuário:
# ● Adicionar tarefas a uma lista
# ● Marcar tarefas como concluídas (removendo-as da lista)
# ● Listar todas as tarefas pendentes
# ● Desafio extra: Adicionar prioridade às tarefas