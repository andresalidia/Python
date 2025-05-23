#Exemplo de coleção aninhada.

Cadastro = {
  "usuario1":{"nome": "Claudia", "idade": 26},
  "usuaria2":{"nome":"Rafael", "idade":23}
 }

index = len(Cadastro)



quercadastrar= int(input("Você deseja cadrastrar um novo usuário? se sim 1, se não 2"))

if quercadastrar == 1:
    index +=1
    nome= input("Digite seu nome: ")
    idade= input("Digite sua idade: ")
    Cadastro[f"usuario{index}"] ={"nome":nome,"idade":idade}

print(Cadastro)