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
print("Elemento na posição 2:", elemento) # a saída será um número inteiro, pois não foi definida o tipo antes.

# Como as strings as listas podem ser fatiadas usando o operador de fatiamento [start:end:step].
# Por exemplo:
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

# As listas também suportam operações de concatenação e repetição.
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

# Diferente das Strings, que são imutáveis, as listas são mutáveis, o que significa que você pode alterar seus elementos.
#Por exemplo:
lista = [1, 2, 3, 4, 5]
lista[0] = 10 # Isso altera o primeiro elemento da lista para 10.
print("Lista após alteração:", lista) # a saída será: 10, 2, 3, 4, 5

#Você também pode adicionar novos elementos à lista usando o método append().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.append(6) # Isso adiciona o número 6 ao final da lista.
print("Lista após adicionar 6:", lista) # a saída será: 1, 2, 3, 4, 5, 6

# Você também pode fazer operações dentro de um parâmetro do append().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.append(lista[0] + lista[1]) # Isso adiciona a soma do primeiro e segundo elemento da lista ao final da lista.
print("Lista após adicionar a soma do primeiro e segundo elemento:", lista) # a saída será: 1, 2, 3, 4, 5, 3

# Você também pode adicionar novos elementos à lista usando o método insert().
# Por Exemplo:
lista = [1, 2, 3, 4, 5]
lista.insert(2, 10) # Isso adiciona o número 10 na posição 2 da lista.
# A sintaxe do insert() é: lista.insert(posição, elemento).
# A posição é o índice onde o elemento será inserido e o elemento é o valor que você deseja adicionar.
print("Lista após adicionar 10 na posição 2:", lista) # a saída será: 1, 2, 10, 3, 4, 5

# Nota: A diferença entre o append() e o insert() é que o append() adiciona o elemento ao final da lista,
#  enquanto o insert() adiciona o elemento em uma posição específica.

# Você também pode remover elementos da lista usando o método remove().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.remove(3) # Isso remove o número 3 da lista.
# A sintaxe do remove() é: lista.remove(elemento).
# O elemento é o valor que você deseja remover.
# Se o elemento não estiver na lista, ocorrerá um erro.
print("Lista após remover 3:", lista) # a saída será: 1, 2, 4, 5

# Você também pode remover elementos da lista usando o método pop().
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

# você também pode remover todos os elementos da lista usando o método clear().
# Por exemplo:
lista = [1, 2, 3, 4, 5]
lista.clear() # Isso remove todos os elementos da lista.
# A sintaxe do clear() é: lista.clear().
# O método clear() não retorna nada.
# Após usar o método clear(), a lista ficará vazia.
print("Lista após remover todos os elementos:", lista) # a saída será: []


