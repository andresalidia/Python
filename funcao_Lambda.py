# são funções anônimas que podem ser usadas em qualquer lugar. tem expressões mais compactas
#exemplo:

# quadrado = lambda x:x**2
# soma = lambda a,b:a+b
# print(quadrado(5))# 25
# print(soma(5,10))# 15


# método map():
# aplica uma função a cada elemento de um iterável (como uma lista) e retorna um novo iterável com os resultados.
# sintaxe:map(função, interável)
# Na parte de função um função lambda pode ser usada.

# Exemplo:

# lista = [1, 2, 3, 4, 5]

# quadrados = list(map(lambda x: x**2, lista))    
# print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# método filter():
# filtra elementos de um iterável com base em uma função que retorna True ou False.
# sintaxe: filter(função, interável)
# Exemplo:
# lista = [1, 2, 3, 4, 5]
# pares = list(filter(lambda x: x % 2 ==0, lista))
# print(pares)  # Saída: [2, 4]

# exercicio:
# 1. Crie uma função lambda que retorne o quadrado de um número.
# try:
#     numero = int(input("Digite um número: "))
#     numero_quadrado = lambda x: x**2
#     print(f"O quadrado de {numero} é: {numero_quadrado(numero)}")  # Saída: 25
# except ValueError:
#     print("Por favor, digite um número válido.")


#Use `map()` com uma função lambda para converter uma lista de temperaturas de Celsius para
# Fahrenheit.

# temperaturas_celsius_semana = [20, 25, 30, 35, 40,32, 28]
# temperaturas_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperaturas_celsius_semana))
# print(f"temperatura em fahrenheit: {temperaturas_fahrenheit}")


# Utilize `filter()` com uma função lambda para obter todos os números pares de uma lista.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_pares = list(filter(lambda x: x % 2 == 0, lista))
# print(f"números pares: {numeros_pares}")  # Saída: [2, 4, 6, 8, 10]


# Implemente uma função que ordene uma lista de strings pelo seu comprimento usando `sorted()` e
# uma função lambda.

# lista = ['natan', 'luan', 'luana', 'maria', 'joao', 'antonio', 'jose', 'marta']

# print(sorted(lista, key=lambda x: len(x)))# sorted tem um parametro key que pode receber uma função lambda




# # Crie uma lista de números e use `map()` e `filter()` para obter os quadrados dos números ímpares
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20]
# quadrados_impares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, lista)))
# print(f"quadrados dos ímpares: {quadrados_impares}")


#DESAFIO:

# Implemente um sistema de filtragem de dados que permita ao usuário especificar múltiplos critérios de
# filtragem usando funções lambda e `filter()`