# Python pode manipular Textos(representado pelo tipo str, também chamado de “strings”) de várias maneiras.
#Eles podem ser colocados entre aspas simples ('...') ou aspas duplas ("...") com o mesmo resultado.


# Para colocar aspas entre aspas, você pode usar a barra invertida (\) para escapar as aspas.
# Por exemplo:
texto = "Ele disse: \"Olá!\""
print(texto) # a saída será Ele disse: "Olá!"

# Se você não quiser que o caracter de escape seja interpretado, você pode usar o caractere de escape \ antes do caractere.
# Por exemplo:
texto = 'C:\\alguma\\pasta\\arquivo.txt'
print(texto) # a saída será C:\alguma\pasta\arquivo.txt

# ou  você pode adicionar um r antes da string para torná-la uma string "crua" (raw string).
# Por exemplo:
texto = r'C:\alguma\pasta\arquivo.txt'
print(texto) # a saída será C:\alguma\pasta\arquivo.txt

# Com o caracter de escape \ mais  n você pode adicionar uma nova linha na string.
# Por exemplo:
texto = "Esta é uma string com uma nova linha.\nEla continua aqui."
print(texto) # saída 

# Você também pode usar aspas triplas ('''...''' ou """...""") para criar strings de várias linhas.
# Por exemplo:
texto_multilinha = """Esta é uma string de várias linhas.
Ela pode conter várias linhas de texto.
E você pode usar aspas 'simples' ou "duplas" dentro dela."""
print(texto_multilinha) # saída

# Concatenação de strings
# Você pode usar o operador + para concatenar strings.
# Por exemplo:
String1 = "Olá"
String2 = "Mundo"
String3 = String1 + " " + String2
print(String3) # a saída será "Olá Mundo"

# Duas ou mais strings lado a lado são concatenadas automaticamente.
# Por exemplo:
String4 = "PY" "THON"
print(String4) # a saída será "PYTHON"

# Esse recurso é útil quando você quer concatenar strings longas.
# Por exemplo:
texto = ('Coloque várias strings dentro de parênteses '
         'para fazer com que elas sejam concatenadas.')
print(texto) # saída

# Você pode concatenar por variáveis.
# Por exemplo:
String5 = "Olá"
String5 += " Python"
print(String5) # a saída será "Olá Python"

# você tambem pode concatenar strings usando o operador %.
# Por exemplo:
String5 = "Olá %s" % String1
print(String5) # a saída será "Olá Olá"

# Multiplicação de strings

# Você pode usar o operador * para multiplicar strings.
# Por exemplo:
String1 = "Olá "
String2 = String1 * 3
print(String2) # a saída será "Olá Olá Olá "

# No Python uma String também pode ser tratada como uma lista de caracteres.
# Você pode acessar os caracteres de uma string usando índices.
# Por exemplo:
String1 = "Python"
print(String1[0]) # a saída será "P"
print(String1[5]) # a saída será "n"
# o primeiro caractere sempre tem índice 0

# ínsdes também podem ser negativos.
# Por exemplo:
String1 = "Python"
print(String1[-1]) # a saída será "n"
print(String1[-6]) # a saída será "P"
# Note que dado que -0 é o mesmo que 0, índices negativos começam em -1.

# Fatiamento de strings
# Você pode usar fatiamento para obter uma substring de uma string.
# Por exemplo:
String1 = "Python"
print(String1[0:2]) # a saída será "Py"
# o primeiro índice é inclusivo e o segundo índice é exclusivo.
# quando um numero não é especificado, o padrão é 0 para o início e o comprimento da string para o fim.
#exemplo:
String1 = "Python"
print(String1[:2]) # a saída será "Py"
print(String1[2:]) # a saída será "thon"

# Você também pode usar índices negativos para fatiar strings.
# Por exemplo:
String1 = "Python"
print(String1[-3:]) # a saída será "hon"
# Você também pode usar o operador de fatiamento para inverter uma string.
# Por exemplo:
String1 = "Python"
print(String1[:: -1]) # a saída será "nohtyP"
#explicação:
# o primeiro índice é o início, o segundo índice é o fim e o terceiro índice é o passo.
#string[início:fim:passo]
# nesse caso:
# Não especificou início nem fim → pega a string toda
# O passo é -1, ou seja, vai "andando de trás pra frente", um caractere por vez.

# Nota: as strings são imutáveis, ou seja, atribuir a uma posição indexada na sequência resulta em um erro:
# Por exemplo:
String1 = "Python"
# String1[0] = "J" # isso vai gerar um erro, pois strings são imutáveis

# Você pode criar uma nova string com o valor desejado.
# Por exemplo:
String1 = "J" + String1[1:]
print(String1) # a saída será "Jython"

# funções para manipular strings


# Contagens:

# você pode saber o comprimento de uma string usando a função len().
# Por exemplo:
String1 = "Python"
print(len(String1)) # a saída será 6

# Você pode usar o método count() para contar o número de ocorrências de uma substring em uma string.
# Por exemplo:
String1 = "Python Python Python"
print(String1.count("Python")) # a saída será 3

# Você também pode usar o método find() para encontrar a posição da primeira ocorrência de uma substring em uma string.
# Por exemplo:
String1 = "Python Python Python"
print(String1.find("Python")) # a saída será 0

# Você também pode usar o método index() para encontrar a posição da primeira ocorrência de uma substring em uma string.
# Por exemplo:
String1 = "Python Python Python"
print(String1.index("Python")) # a saída será 0

# Você também pode usar o método rfind() para encontrar a posição da última ocorrência de uma substring em uma string.
# Por exemplo:
String1 = "Python Python Python"
print(String1.rfind("Python")) # a saída será 14

# Você também pode usar o método rindex() para encontrar a posição da última ocorrência de uma substring em uma string.
# Por exemplo:
String1 = "Python Python Python"
print(String1.rindex("Python")) # a saída será 14


# Verificações:

# Você também pode usar o método startswith() para verificar se uma string começa com uma substring.
# Por exemplo:
String1 = "Python"
print(String1.startswith("Py")) # a saída será True

# Você também pode usar o método endswith() para verificar se uma string termina com uma substring.
# Por exemplo:
String1 = "Python"
print(String1.endswith("on")) # a saída será True

# Você também pode usar o método isalpha() para verificar se uma string contém apenas letras.
# Por exemplo: 
string1 = "Python123"
print(string1.isalpha()) # a saída será False, pois contém números

# Você também pode usar o método isdigit() para verificar se uma string contém apenas dígitos.
# Por exemplo:
string1 = "12345"
print(string1.isdigit()) # a saída será True, pois contém apenas dígitos

# Você também pode usar o método isalnum() para verificar se uma string contém letras ou dígitos.
# Por exemplo:
string1 = "Python"
print(string1.isalnum()) # a saída será True, pois contém ao menos letras

#para verificar se a string contém caracteres especiais, você pode usar o método isalnum() e verificar se a string não é alfanumérica.
# Por exemplo: 
string1 = "Python@123"
print(string1.isalnum()) # a saída será False, pois contém caracteres especiais 

# para verificar se uma string contém apenas espaços em branco, você pode usar o método isspace().
# Por exemplo: 
string1 = " olá   "
print(string1.isspace()) # a saída será False, pois contém letras
string1 = "   "
print(string1.isspace()) # a saída será True, pois contém apenas espaços em branco

# Você também pode usar o método isupper() para verificar se uma string contém apenas letras maiúsculas.
# Por exemplo:
string1 = "PYTHON"
print(string1.isupper()) # a saída será True, pois contém apenas letras maiúsculas

# Você também pode usar o método islower() para verificar se uma string contém apenas letras minúsculas.
# Por exemplo:
string1 = "python"
print(string1.islower()) # a saída será True, pois contém apenas letras minúsculas


# Manipulação de strings:

# Você também pode usar o método upper() para converter uma string em letras maiúsculas.
# Por exemplo:
String1 = "Python"
String2 = String1.upper()
print(String2) # a saída será "PYTHON"

# Você também pode usar o método lower() para converter uma string em letras minúsculas.
# Por exemplo:
string1 = "Python"
string2 = string1.lower()
print(string2) # a saída será "python"

# Você também pode usar o método title() para capitalizar a primeira letra de cada palavra em uma string.
# Por exemplo:
string1 = "python é uma linguagem de programação"
print(string1.title()) # a saída será "Python É Uma Linguagem De Programação"

# Você também pode usar o método capitalize() para capitalizar a primeira letra de uma string.  
## Por exemplo:
string1 = "python é uma linguagem de programação"
print(string1.capitalize()) # a saída será "Python é uma linguagem de programação"

# Você também pode usar o método swapcase() para inverter o case de cada letra em uma string.
# Por exemplo:
string1 = "Python"
print(string1.swapcase()) # a saída será "pYTHON"

# Você também pode usar o método strip() para remover espaços em branco do início e do fim de uma string.
#por exemplo:
string1 = "  Olá Python   "
print(string1.strip()) # a saída será "Olá Python"
#Nota: o método strip() remove espaços em branco, mas não remove espaços em branco entre as palavras.

# Você também pode usar o método lstrip() para remover espaços em branco do início de uma string.
# Por exemplo:
string1 = "  Olá Python   "
print(string1.lstrip()) # a saída será "Olá Python   "

# Você também pode usar o método rstrip() para remover espaços em branco do fim de uma string.
# Por exemplo:
string1 = "  Olá Python   "
print(string1.rstrip()) # a saída será "  Olá Python"

# Você também pode usar o método zfill() para preencher uma string com zeros à esquerda.
# Por exemplo:
string1 = "42"
print(string1.zfill(5)) # a saída será "00042"

# Você também pode usar o método expandtabs() para manipular o tamanho da tabulação.
# Por exemplo:
string1 = "Python\té\tuma\tlinguagem\tde\tprogramação"
print(string1.expandtabs(10))# a saída será "Python é uma linguagem de programação"

# Você também pode usar o método splitlines() para transformar textos com quebras de linhas (\n) em uma lista.
# Por exemplo:
string1 = "Python\né\numa\nlinguagem\nde\nprogramação"
print(string1.splitlines()) # a saída será ["Python", "é", "uma", "linguagem", "de", "programação"]
# para manter o \n na string, você pode usar o método spitlines(keepends=True).
# Por exemplo:
string1 = "Python\né\numa\nlinguagem\nde\nprogramação"
print(string1.splitlines(keepends=True)) # a saída será ["Python\n", "é\n", "uma\n", "linguagem\n", "de\n", "programação"]


# Você também pode usar o método format() para formatar strings.
# Por exemplo:
String1 = "Olá {}"
string2 = String1.format("Mundo")
print(string2) # a saída será "Olá Mundo"


# Você também pode usar o método format_map() para formatar strings.
# # Por exemplo:
String1 = "Olá {nome}"
String2 = String1.format_map({"nome": "Mundo"})
print(String2) # a saída será "Olá Mundo"

# Você também pode usar o método join() para concatenar strings em uma lista.
# Por exemplo:
lista = ["Olá", "Mundo"]
String = " ".join(lista)
print(String) # a saída será "Olá Mundo"

# Dividir strings
# Você pode usar o método split() para dividir uma string em uma lista de substrings. esse método é parecido com slitlines(), 
# mas não é compativel com todos os tipos de  quebra de linha.
# Porém tem a vantagem de você poder escolher o delimitador.
# # Por exemplo:
String5 = "Olá Mundo"
lista2 = String5.split(" ")
print(lista2) # a saída será ["Olá", "Mundo"]

# Você também pode usar o método partition() para dividir uma string em três partes:
#  a parte antes do delimitador, o delimitador e a parte depois do delimitador.
# Por exemplo:
String = "Olá@103"
parte1, delimitador, parte2 = String.partition("@")
print(parte1) # a saída será "Olá"
print(delimitador) # a saída será "@" 
print(parte2) # a saída será "103"


# Substituir strings
# Você pode usar o método replace() para substituir uma substring por outra.
# Por exemplo:
String = "Olá Mundo"
String = String.replace("Mundo", "Python")# o primeiro argumento é a substring que você quer substituir
#e o segundo argumento é a substring que você quer colocar no lugar.
print(String) # a saída será "Olá Python"

# Essa foi uma breve explicação de como usar os operadores matemáticos básicos e manipular strings em Python.
# Existem muitos outros métodos e funções disponíveis para trabalhar com strings em Python.
# Você pode consultar a documentação oficial do Python para mais informações.
# Espero que isso tenha ajudado você a entender como trabalhar com strings em Python.
# Boa sorte com sua programação em Python!
# Se desejar praticar mais, aqui vai alguns exercícios:
# 1. Crie um programa que peça ao usuário para digitar seu nome e sobrenome e imprima o nome completo em letras maiúsculas.
# 2. Crie um programa que peça ao usuário para digitar uma frase e conte quantas palavras ela tem.
# 3. Crie um programa que peça ao usuário para digitar uma frase e imprima a frase invertida.
# 4. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de vogais e consoantes na frase.
# 5. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de letras "a" na frase. 
# 6. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de espaços em branco na frase.
# 7. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de caracteres especiais na frase.
# 8. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de números na frase.
# 9. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de letras maiúsculas e minúsculas na frase.
# 10. Crie um programa que peça ao usuário para digitar uma frase e imprima a quantidade de palavras que começam com a letra "a".

#Esses exercícios vão te ajudar a praticar o que você aprendeu sobre strings em Python.
# Boa sorte e divirta-se programando!