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
        
        layout = QHBoxLayout()# Cria o layout vertical
        
        texto = QLineEdit() # Criar um campo de linha de texto
        botao = QPushButton("ok") # cria um botão
        

        # Seta evento_botao como evento para quando o botão for clicado
        botao.clicked.connect(self.evento_botao)
        texto.textEdited.connect(self.evento_botao)# pode ser usado: validação de e-mail. prever  digitação

        #Definir tamanhos
        texto.setFixedHeight(20)
        texto.setFixedWidth(200)
        botao.setFixedHeight(20)
        botao.setFixedWidth(50)

        
        
        layout.addWidget(texto)# add campo texto no layout vertical
        layout.addWidget(botao)# add botão no layout vertical

        obj_Layout = QWidget()# Cria um widget em branco
        obj_Layout.setLayout(layout)# Seta o 'Layout' como layout widget
        self.setCentralWidget(obj_Layout)# torna o 'obj_Layout' o widget central
        
         
    def evento_botao(self):
        print(f"Olá, {self.texto}!")

App = QApplication([])# inicia a aplicação
janela = JanelaPrincipal() #Widget

janela.show() # Mostra a janela
App.exec() # Executa a aplicação







