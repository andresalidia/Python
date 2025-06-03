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
        
        self.Layout = QHBoxLayout()# Cria o layout vertical
        self.texto = QLineEdit() # Criar um campo de linha de texto
        self.botao = QPushButton("ok") # cria um botão
        

        # Seta evento_botao como evento para quando o botão for clicado
        self.botao.clicked.connect(self.evento_botao)
        

        #Definir tamanhos
        self.texto.setFixedHeight(20)
        self.texto.setFixedWidth(200)
        self.botao.setFixedHeight(20)
        self.botao.setFixedWidth(50)

        
        
        self.Layout.addWidget(self.texto)# add campo texto no layout vertical
        self.Layout.addWidget(self.botao)# add botão no layout vertical


        obj_Layout = QWidget()# Cria um widget em branco
        obj_Layout.setLayout(self.Layout)# Seta o 'Layout' como layout widget
        self.setCentralWidget(obj_Layout)# torna o 'obj_Layout' o widget central
        
         
    def evento_botao(self):
        print(f"Olá, {self.texto.text()}!")# precisa colocar o .text(), pois se não sai apenas o objeto e não o texto
App = QApplication([])# inicia a aplicação
janela = JanelaPrincipal() #Widget

janela.show() # Mostra a janela
App.exec() # Executa a aplicação






