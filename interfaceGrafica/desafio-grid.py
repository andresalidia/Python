from PyQt6.QtWidgets import*
from caixa import CaixaCor

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        botao= QPushButton("Teste")
        botao.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        caixa1 = CaixaCor("#04C4FF")
        caixa2 = CaixaCor("#246807")
        caixa3 = CaixaCor("#48525B")
        caixa4 = CaixaCor("#0EE824")
        caixa5 = CaixaCor("#6E0827")
        caixa6 = CaixaCor("#FFD900")
        caixa7 = CaixaCor("#FF00A2")

        layout_g = QGridLayout()
        layout_g.addWidget(caixa1, 1,1,8,5)
        layout_g.addWidget(caixa2, 9,1,2,3)
        layout_g.addWidget(caixa3, 9,4,2,2)
        layout_g.addWidget(caixa4, 1,6,1,4)
        layout_g.addWidget(caixa5, 1,10, 1,4)
        layout_g.addWidget(caixa6, 1,14,1,3)
        layout_g.addWidget(caixa7, 2,6,9,11)








        layout_c = QWidget()# Cria um componente para hospedae o layou_v
        layout_c.setLayout(layout_g) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
