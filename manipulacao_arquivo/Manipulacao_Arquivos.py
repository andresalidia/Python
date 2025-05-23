# Manipulação de Arquivos:

# Metodo open():
# O método open() é usado para abrir um arquivo, ler, escrever ou adicionar conteúdo a ele.
# A sintaxe básica é a seguinte:
#arquivo = open("nome_do_arquivo.txt ou caminho/para/o/arquivo.txt", "modo")
# onde "modo" pode ser: 
# "r" para leitura (read), 
# "w" para escrita (write),
# "a" para adicionar (append)
# 'x' para criar um novo arquivo (erro se já existir),)
#  "b" para binário (usado com 'rb' e 'wb').
# "t" para texto (usado com 'rt' e 'wt').
# "r+" para leitura e escrita (read and write).
# "w+" para escrita e leitura (write and read).
# "a+" para adicionar e leitura (append and read).
# "x+" para criar e leitura (create and read).
# 'rb' leitura em modo binário (tipo pra imagens)
# 'wb' escrita em modo binário (tipo pra imagens)
# O método open() retorna um objeto de arquivo que pode ser manipulado. ex: read(), write(), close().

#vamos criar um arquivo e escrever nele
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um arquivo de exemplo.\n")
    arquivo.write("Manipulação de arquivos em Python é fácil!\n")

    conteudo = arquivo.read()
    print(conteudo)