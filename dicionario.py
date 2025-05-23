# Dicionários são estruturas de dados que armazenam pares de informações:
#uma chave e um valor
#Exemplo
meu_dicionario={
    "nome": "Andresa Lídia",
    "idade": 18,
    "cidade": "Cuiabá",
    "data de nascimento": "10/05/2006",
}

# acessando valores especificos:

print(meu_dicionario["nome"])# saída: Andresa Lídia
#print(meu_dicionario["mãe"]) dá erro pois a chave não existe

#Você pode adcionar valores a chaves já existentes:
meu_dicionario["idade"]+=1
#Ou add mais chaves e valores
meu_dicionario["curso"]= "Engenharia da Computação"
#removendo valores:
del meu_dicionario["cidade"]

# Como mostrar dicionario:
for chave, valores in meu_dicionario.items():
    print(f"{chave}:{valores}")


#Metodos de manipulção de dicionários:

#.get(chave,valor_padrão):
#para evitar erros de uma chave que não existe, pode-se usar get()

print(meu_dicionario.get("mãe","Valor não encontrado"))# o valor antes da virgula é a chave a ser encontrada, e o valor depois da virgula é a valor a ser mostrado caso não ache a chave e seu valor.

#.keys()
#Retoma todas as chaves
print(meu_dicionario.keys())#  saída: dict_keys(['nomes chaves'],[],[]...)

#.values():
# retoma todos os valores
print(meu_dicionario.values())#  saída: dict_keys(['nomes valores'],[],[]...)

# .update()
#Atualiza o dicionário com outro

parentes = {
    "mãe": "linda",
    "pai": "Inteligente"
}
meu_dicionario.update(parentes)
print(meu_dicionario)

#.pop(chave)
#remove uma chave especificada e retoma o valor
data = meu_dicionario.pop( "data de nascimento")
print(data)

# .popitem()
#Remove o ultimo item adicionado e retoma o valor

ultimo = meu_dicionario.popitem()
print(ultimo)

#.copy()
#Cria uma copia rasa (shallow copy) do dicionário
novo_dicionario = meu_dicionario.copy()
print(novo_dicionario)

#.clear():
#Remove todos os itens do dicionário
meu_dicionario.clear()
print(meu_dicionario)

#fromkeys(interável, valor)
chaves = ["Nome", "Idade","Cor preferida"] 
meu_dicionario = meu_dicionario.fromkeys(chaves,"Só poso colocar um valor em todos com essa função :(")
print(meu_dicionario)


# # Testando Metodos de Lista em dicionário:

dicionario_teste={
    "chave":"valor",
    "nome":"Laura",
    "sobrenome":"Cardoso",
     "profissão":"Engenheira"
 }
# remove não funciona em dicionário
#Não pode deletar apenas um valor sem a  chave

print(len(dicionario_teste))

# in
# verifica que uma chave existe, devolve True ou False
print("Andresa" in dicionario_teste)

#not in
#verifica se uma chave não existe, devolve True ou False
print("Andresa" not in dicionario_teste)
#items
#Retomas os pares (Chave-valor) usado normalmente em for
print(dicionario_teste.items())
#set
#converte as chaves do diciário em um conjunto
print(set(meu_dicionario))# saída: {'Nome', 'Cor preferida', 'Idade'}
#setdefault():
# Retorna o valor de uma chave, se ela existir. Caso contrário, insere a chave com um valor padrão e retorna o valor padrão.
meu_dicionario.setdefault("cor","Rosa")
print(meu_dicionario)



