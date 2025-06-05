from PyQt6.QtWidgets import*
from caixa import CaixaCor

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        caixa1 = CaixaCor("#5EFF01")
        caixa2 = CaixaCor("#0184FF")
        caixa3 = CaixaCor("#FF00D0")
        caixa4 = CaixaCor("#FF5100")
        caixa5 = CaixaCor("#FFFB00")
        caixa6 = CaixaCor("#FF0000")


        layout_v = QVBoxLayout()
        layout_v.addWidget(caixa1,12)
        layout_v.addWidget(caixa2,3)
        layout_v.addWidget(caixa3,7)
        layout_v.addWidget(caixa4,9)
        layout_v.addWidget(caixa5,14)
        layout_v.addWidget(caixa6,20)

        layout_c = QWidget()# Cria um componente para hospedae o layou_v
        layout_c.setLayout(layout_v) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
