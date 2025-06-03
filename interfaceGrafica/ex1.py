from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLineEdit
)


App = QApplication([])# inicia a aplicação
janela = QMainWindow() #Widget

botao = QPushButton("Aperte em mim") # instanciei o botão
janela.setCentralWidget(botao)# coloquei para ele ser o widget central

janela.show() # Mostra a janela
App.exec() # Executa a aplicação