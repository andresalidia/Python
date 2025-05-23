precomaiscaro = 0.0
nome_produtomaiscaro=""
produtos = [
 {"nome": "Notebook", "preco": 3000},
 {"nome": "Celular", "preco": 1500},
 {"nome": "Tablet", "preco": 2000}
]
#procurando o produto mais caro:

for produto in produtos:
    if produto["preco"]>precomaiscaro:
        precomaiscaro=produto["preco"]
        nome_produtomaiscaro = produto["nome"]

print(f"O {nome_produtomaiscaro} é o produto mais caro, e custa: {precomaiscaro}")