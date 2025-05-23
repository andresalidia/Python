contatos = {
 "João": {"telefone": "1234", "email": "joao@example.com"},
 "Ana": {"telefone": "5678", "email": "ana@example.com"}
}


print("Agenda telefonica:")
for nome,info in contatos.items():
  
     print(f"Nome:{nome}, Telefone {info["telefone"]}, email:{info["email"]}")
print("Deseja alterar as informações de alguem na lista? ")

