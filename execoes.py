# try:
#  x = int(input("Digite um número: "))
#  print(f"O dobro de {x} é {x * 2}")
# except ValueError:
#  print("Você não digitou um número válido!")

#Multiplas exceções:

# try:
#  x = int(input("Digite um número: "))
#  y = int(input("Digite outro número: "))
#  resultado = x / y
# except ValueError:
#  print("Erro: Você não digitou um número válido.")
# except ZeroDivisionError:
#  print("Erro: Divisão por zero não é permitida.")
# else:
#  print(f"O resultado da divisão de {x}/{y} é: {resultado}")


# Uso de cláusulas else e finally:

# try:
#  arquivo = open("dados.txt", "r")# entender melhor como  funciona
#  conteudo = arquivo.read()
# except FileNotFoundError:
#  print("Erro: Arquivo não encontrado.")
# else:
#  print("Arquivo lido com sucesso!")
# finally:
#  print("Encerrando operação.")
#  if 'arquivo' in locals() and not arquivo.closed:
#   arquivo.close()


# nomes = ['maria','joao','antonio','jose','marta','ana','luan','luana','maria','joao','antonio','jose','marta','ana','luan','luana']
# # Função para acessar um elemento da lista
# def ascesar_nomes(nomes):
#     index =  int(input("Digite o índice do elemento que você deseja acessar: "))
#     try:
#         elemento = nomes[index]
#         print(f"O elemento no índice {index} é: {elemento}")
#     except IndexError:
#         print("Erro: Índice fora do intervalo da lista.")
#     except ValueError:
#       print("Erro: Valor inválido. Por favor, insira um número inteiro.")

# ascesar_nomes(nomes)


# import math
# try:
#     numero = int(input("Digite um número: "))
#     if numero < 0:
#         print("Erro: Número negativo. Por favor, insira um número inteiro e positivo.")
#     else:
#         raiz = math.sqrt(numero)
#         print(f"A raiz quadrada de {numero} é: {raiz}")
# except ValueError:
#     print("Erro: Valor inválido. Por favor, insira um número inteiro.")

