# Faça uma tela para calcular o IMC
# A tela deve possuir:
# - Campo de texto para altura e para peso
# - botão para efetuar o cálculo
# Escreva o resultado no terminal

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QLabel
)

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Layout= QVBoxLayout()
        self.altura = QLineEdit()
        self.peso = QLineEdit()
        self.botao = QPushButton("Calcular") # cria um botão
        
          
        self.Layout.addWidget(QLabel("Altura: "))
        self.Layout.addWidget(self.altura)# add campo texto no layout vertical
        self.Layout.addWidget(QLabel("Peso: "))
        self.Layout.addWidget(self.peso)# add botão no layout vertical
        self.Layout.addWidget(self.botao)



        # Seta evento_botao como evento para quando o botão for clicado
        self.botao.clicked.connect(self.evento_botao)
        


        obj_Layout = QWidget()# Cria um widget em branco
        obj_Layout.setLayout(self.Layout)# Seta o 'Layout' como layout widget
        self.setCentralWidget(obj_Layout)# torna o 'obj_Layout' o widget central


    def evento_botao(self):  
        print(f" Seu IMC é: {float(self.peso.text())//(float(self.altura.text())**2):.2f}")

        
App = QApplication([])# inicia a aplicação
janela = JanelaPrincipal() #Widget

janela.show() # Mostra a janela
App.exec() # Executa a aplicação


    