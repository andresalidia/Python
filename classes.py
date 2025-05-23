# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
#     def area(self):
#         return self.largura * self.altura
# retangulo = Retangulo(5,3)
# print(retangulo.area())


# class Pessoa:
#     def __init__ (self, nome, idade ):
#         self.nome = nome
#         self. idade = idade
#     def apresentar(self):
#         return f"Olá {self.nome}, você tem {self.idade} anos "
    
# pessoal = Pessoa("Andresa", 19)
# print(pessoal.apresentar())

# import math 
# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio
#     def area(self):
#         return math.pi*self.raio**2
#     def circunferencia(self):
#         return 2* math.pi* self.raio
    
# circulo = Circulo(2)

# print(f" a area do circulo será:{circulo.area():.2f} e a circunfencia será: {circulo.circunferencia():.2F}")

# class Cachorro:
#     def __init__(self, nome, raca):
#         self.nome = nome
#         self.raca = raca
#     def latir(self):
#         print(f"{self.nome} da raça {self.raca} está latindo")

# cachorros = Cachorro("Kyra", "salcinha")

# cachorros.latir()


# class Calculadora:
#     def __init__(self, numero1, numero2):
#         self.numero1 = numero1
#         self.numero2 = numero2
#     def somar(self): 
#         return self.numero1 + self.numero2
#     def subtrair (self):
#         return self.numero1 - self.numero2
#     def dividir (self):
#         return self.numero1//self.numero2# dividi inteiro
#     def multiplicar(self):
#         return self.numero1*self.numero2
    
# num1 = int((input("Informe um número: ")))
# num2 = int(input("Informe outro número: "))
# calc = Calculadora(num1,num2)
# continua = True
# while(continua) :
#     print( "Escolha a operação que você dejesa fazer com esse 2 números: ")
#     escolha = int(input("1 - soma;\n2 - subtração\n3 - divisão\n4 - multiplicação:\n"))
#     if escolha == 1:
#          print(f"Soma:{calc.somar()}")
#          continuar = input("Deseja continua fazendo outras oprações? s/n: ")
#          if continuar.lower() == 'n':
#             continua = False
        

#     elif escolha == 2:
#         print(f"subtração:{calc.subtrair()}")
#         continuar = input("Deseja continua fazendo outras oprações? s/n: ")
#         if continuar.lower() == 'n':
#             continua = False
#     elif escolha == 3:
#         print(f"divisão: {calc.dividir()}")
#         continuar = input("Deseja continua fazendo outras oprações? s/n: ")
#         if continuar.lower() == 'n':
#             continua = False
#     elif escolha == 4:
#         print(f"multiplicação: {calc.multiplicar()}")
#         continuar = input("Deseja continua fazendo outras oprações? s/n: ")
#         if continuar.lower() == 'n':
#             continua = False
#     else:
#         print("Escolha não encontra, tente novamente")
# print("Obrigado por usar essa calculadora :)")


# class ContaBancaria:
#     def __init__(self, saldo, titular):
#         self.saldo = saldo
#         self.titular = titular

#     def depositar(self, valor):
#         self.saldo += valor
#         return self.saldo

#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#             return self.saldo
#         else:
#             return f"O valor R${valor} é maior que o disponível atualmente, tente novamente!"

# banco = ContaBancaria(1500, "Andresa")

# opcao = int(input(f"Olá {banco.titular}, deseja fazer qual operação na conta?\n1 - Depositar\n2 - Sacar:\n"))
# if opcao == 1:
#     valor = float(input("Informe um valor: R$"))
#     print(f"O valor depositado foi de R${valor}, seu saldo atual é de R${banco.depositar(valor):.2f}")
# elif opcao == 2:
#     valor = float(input("Informe um valor: R$"))
#     resultado = banco.sacar(valor)
#     print(f"O valor do saque foi de R${valor}, seu saldo atual é de R${resultado:.2f}" if isinstance(resultado, float) else resultado)


# class Livro:
#     def __init__(self, nome, autor):
#         self.nome= nome
#         self.autor= autor
#     def detalhes(self):
#         print(f"{self.nome} - {self.autor}")

# class Biblioteca:
#     def __init__(self):
#         self.livros= []
#     def adcionar (self,livro):
#         self.livros.append(livro)
#     def lista(self):
#         for livro in self.livros:
#             print(f"{livro.nome} - {livro.autor}")
#     def excluir (self):
#         liv = input("Qual o nome do Livro que você deseja excluir? ")
#         for livro in self.livros:
#             if livro.nome == liv:
#                 self.livros.remove(livro)
#                 return# ele finaliza a função
#         print("Livro não encontrado!")
        


# livro1 = Livro('O pequeno princípe', 'Sant Express')
# livro2 = Livro('Sitio do pica pau Amarelo', 'Monteiro Lobato')
# livro3 = Livro('O cortiço', 'Aluísio de Azevedo')

# bib = Biblioteca()

# bib.adcionar(livro1) 
# bib.adcionar(livro2)
# bib.adcionar(livro3)  
# bib.lista() 
# bib.excluir()
# bib.lista()       
        
# import math
# class Ponto:
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
#     def distancia (self):
#         return math(self.x**2 + self.y**2)
# print("Vamos calcular a distância de dois pontos x e y.") 
# x = int(input("Informe o ponto x: "))
# y = int(input("Informe o ponto y: "))
# pontos = (x,y)
# print(pontos.distancia())


