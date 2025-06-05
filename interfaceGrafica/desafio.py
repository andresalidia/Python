from PyQt6.QtWidgets import*
from caixa import CaixaCor

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        botao= QPushButton("Teste")
        botao.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        caixa1 = CaixaCor("#991B38")
        caixa2 = CaixaCor("#EB2799")
        caixa3 = CaixaCor("#0084FF")
        caixa4 = CaixaCor("#056604")

        layout_V = QVBoxLayout()
        layout_V.addWidget(caixa3,8)
        layout_V.addWidget(botao,2)

        layout_h = QHBoxLayout()
        layout_h.addWidget(caixa1,2)
        layout_h.addWidget(caixa2,10)
        layout_h.addLayout(layout_V, 4)

        layout_c = QWidget()# Cria um componente para hospedae o layou_v
        layout_c.setLayout(layout_h) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
