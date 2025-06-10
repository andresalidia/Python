from PyQt6.QtWidgets import*
from caixa import CaixaCor

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        Botao2 = QPushButton("×")
        Botao3 = QPushButton("+")
        Botao1 = QPushButton("÷")
        Botao4 = QPushButton("-")
        Botao5 = QPushButton("7")
        Botao6 = QPushButton("8")
        Botao7 = QPushButton("9")
        Botao8 = QPushButton("%")
        Botao9 = QPushButton("4")
        Botao10 =QPushButton("5")
        Botao11 =QPushButton("6")
        Botao12= QPushButton("C")
        Botao13= QPushButton("1")
        Botao14= QPushButton("2")
        Botao15= QPushButton("3")
        Botao16 =QPushButton("+/-")
        Botao17 =QPushButton("0")
        Botao18 =QPushButton(",")
        historico = QListWidget()
        botao_igual= QPushButton('=')
        expressao= QLineEdit()
        
        expressao.setText("0")
        expressao.returnPressed.connect(self.calcular)
        botao_igual.clicked.connect(self.calcular)
       

        #Modifica o estilo do botão 
        self.setStyleSheet(
            """ 
                QPushButton{
                    font-size: 24px
                }
                QLineEdit{
                    font-size: 24px
                }
            """
        )

        layout_g = QGridLayout()
        layout_g.addWidget(historico, 1,1,2,4)
        layout_g.addWidget(expressao, 3,1,1,4)
        layout_g.addWidget(Botao1, 4,1,1,1)
        layout_g.addWidget(Botao2, 4,2,1,1)
        layout_g.addWidget(Botao3, 4,3,1,1)
        layout_g.addWidget(Botao4, 4,4,1,1)
        layout_g.addWidget(Botao5, 5,1,1,1)
        layout_g.addWidget(Botao6, 5,2,1,1)
        layout_g.addWidget(Botao7, 5,3,1,1)
        layout_g.addWidget(Botao8, 5,4,1,1)
        layout_g.addWidget(Botao9,6,1,1,1)
        layout_g.addWidget(Botao10,6,2,1,1)
        layout_g.addWidget(Botao11,6,3,1,1)
        layout_g.addWidget(Botao12,6,4,1,1)
        layout_g.addWidget(Botao13,7,1,1,1)
        layout_g.addWidget(Botao14,7,2,1,1)
        layout_g.addWidget(Botao15,7,3,1,1)
        layout_g.addWidget(Botao16,8,1,1,1)
        layout_g.addWidget(Botao17,8,2,1,1)
        layout_g.addWidget(Botao18,8,3,1,1)
        layout_g.addWidget(botao_igual,7,4,2,1)

    
        self.setWindowTitle("Calculadora")
        layout_c = QWidget()# Cria um componente para hospedae o layou_v
        layout_c.setLayout(layout_g) # Define 'layout_v' como layout do componente
        self.setCentralWidget(layout_c)

        self.expressao = expressao
        self.historico = historico

    def calcular(self):
        exp = self.expressao.text()
        res = eval(exp)
        # print(f"{exp}={res}")
        self.historico.addItem(f"{exp}={res}")

app = QApplication([])

janela = JanelaPrincipal()
janela.show()

app.exec()
