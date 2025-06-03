from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLineEdit
)
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()# Cria o layout vertical
        botao = QPushButton("aperte") # cria um botão
        texto = QLineEdit() # Criar um campo de linha de texto

        #Definir tamanhos
        texto.setFixedHeight(20)
        texto.setFixedWidth(200)
        botao.setFixedHeight(20)
        botao.setFixedWidth(50)

        layout.addWidget(botao)# add botão no layout vertical
        layout.addWidget(texto)# add campo texto no layout vertical


        obj_Layout = QWidget()# Cria um widget em branco
        obj_Layout.setLayout(layout)# Seta o 'Layout' como layout widget
        self.setCentralWidget(obj_Layout)# torna o 'obj_Layout' o widget central 


App = QApplication([])# inicia a aplicação
janela = JanelaPrincipal() #Widget

janela.show() # Mostra a janela
App.exec() # Executa a aplicação







