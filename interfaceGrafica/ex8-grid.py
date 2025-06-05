from PyQt6.QtWidgets import*
from caixa import CaixaCor

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        caixa1 = CaixaCor("#5EFF01")
        caixa2 = CaixaCor("#0184FF")
        caixa3 = CaixaCor("#FF00D0")
        caixa4 = CaixaCor("#552202")
        caixa5 = CaixaCor("#FFFB00")
        caixa6 = CaixaCor("#FF0000")
        caixa7 = CaixaCor("#5B0FA8")
        caixa8 = CaixaCor("#FF5E00")
        caixa9 = CaixaCor("#46EAE7")

        layout_g = QGridLayout()
        layout_g.addWidget(caixa1, 1, 1)
        layout_g.addWidget(caixa2, 1, 2)
        layout_g.addWidget(caixa3, 1, 3)
        layout_g.addWidget(caixa4, 2, 1)
        layout_g.addWidget(caixa5, 2, 2)
        layout_g.addWidget(caixa6, 2, 3)
        layout_g.addWidget(caixa7, 3, 1)
        layout_g.addWidget(caixa8, 3, 2)
        layout_g.addWidget(caixa9, 3, 3)

        layout_c = QWidget()# Cria um componente para hospedae o layou_v
        layout_c.setLayout(layout_g) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
