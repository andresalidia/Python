from PyQt6.QtWidgets import*
from caixa import CaixaCor

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        caixa1 = CaixaCor("#5EFF01")
        caixa2 = CaixaCor("#0184FF")
        caixa3 = CaixaCor("#FF00D0")
        caixa4 = CaixaCor("#FFFB00")
       
        layout_g = QGridLayout()
        layout_g.addWidget(caixa4, 1, 1, 1,2)# os primeiro dos números e onde começa e os 2 ultimos é quantas linhas e colunas anda.
        layout_g.addWidget(caixa1, 1, 3)
        layout_g.addWidget(caixa2, 2, 1,2,1)
        layout_g.addWidget(caixa3, 2,2, 2,2)
       
        layout_c = QWidget()# Cria um componente para hospedae o layou_v
        layout_c.setLayout(layout_g) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
