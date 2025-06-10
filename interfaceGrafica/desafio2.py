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

        layout_h_1 = QHBoxLayout()
        layout_h_1.addWidget(caixa2,3)
        layout_h_1.addWidget(caixa3,2)

        layout_v_1 = QVBoxLayout()
        layout_v_1.addWidget(caixa1, 8)
        layout_v_1.addLayout(layout_h_1, 2)

        layout_h_2 = QHBoxLayout()
        layout_h_2.addWidget(caixa4,4)
        layout_h_2.addWidget(caixa5,4)
        layout_h_2.addWidget(caixa6,3)

        layout_v_2 = QVBoxLayout()
        layout_v_2.addLayout(layout_h_2, 1)
        layout_v_2.addWidget(caixa7, 9)

        layout_h_principal = QHBoxLayout()
        layout_h_principal.addLayout(layout_v_1, 5)
        layout_h_principal.addLayout(layout_v_2, 11)

        layout_c = QWidget()# Cria um componente para hospedar o layou_v
        layout_c.setLayout(layout_h_principal) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
