# Modulos são  bibliotecas com algumas funções.
#Você pode cria-las ou importar as que ja existem no python 
#importando Modolo com import
# Há varias maneiras de importar
import math # contém funções matemáticas
from random import randint # Essa é uma maneira mais especifica de importação
# esse modolo gera números aleatórios
import datetime as date # Manipula datas 
#Modulo de manipulação de datas


# Como usa-las

numero = randint(1,101)
print("O número sorteado foi: ",numero)

raiz = math.sqrt(numero)

print("A raiz quadrada dele é: ", raiz)

data_atual = date.datetime.now()# Mostra a data e horas atuais de  forma muito especifica.
print("Obrigada por participar desse teste! Data atua... ", data_atual)
# Exemplos de Módulos comuns:
#Math
#random
#os
#json
#existe uma comunidade que criam pacotes
# você pode instar elas via gerenciador de pacotes(pip)
# há milhares de opções no PyPI (Python Package Index)
#bibliotecas externas:
#pandas: análise de dados
# numpy: Computação numérica
#matplotlib: visualização de dados
#requests: requisições HTTP
#pygame: desenvolvimento de jogos

#Como instalar:
# No terminal digite...
#pip install nome_do_pacote
#ou.. para baixar uma versão especifica
#pip install nome_do_pacote==1.0.0
# ou.. instalar multtiplos pacotes
#pip install -r requirements.txt