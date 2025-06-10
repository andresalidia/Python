class Usuario:
    def __init__ (self, nome, email, senha):
        self.nome = nome
        self.email= email
        self._senha = senha

    def confere_senha(self, senha):
        if(senha == self._senha):
            return True
        else:
            return False

    def detalhes(self):
        print (f"Nome: {self.nome}")
        print (f"Email: {self.email}")

class Aluno(Usuario):
    def __init__(self,nome, email, senha, semestre, matricula):
        super().__init__(nome, email, senha)
        self.semestre = semestre
        self.matricula = matricula
        self._notas={}

    def get_notas(self):
        return self._notas.values()

    def set_notas(self, semestre, nota):
        self._notas[semestre]=nota

    def del_nota(self,semestre):
        del self._notas[semestre]
    
    def media(self):
       soma = 0
       divisor = 0 
       for semestre, nota  in self._notas.items():
           soma += nota
           divisor +=1
       
       if divisor == 0:
            return 0
       else:
            media = soma/divisor
            return media
    
    def aprovado(self):
        if (self.media() > 7.0):
            return True
        else:
            return False
        
    def detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Média: {self.media():.2f}")
        if( self.aprovado()):
            print("Situação: Aprovado" )
        else:
            print("Situação: Reprovado")

class AlunoTecnico(Aluno):
    def __init__(self,nome, email, senha, semestre, matricula, ):
        super().__init__(nome, email, senha,matricula)
        self._falats = 0
    def add_falta(self, quantidade_faltas):
        self._falats+=quantidade_faltas
    
    def aprovado(self):
        if(self.media> 7.0 and self._falats/320 <0.25):
            return True
        else:
            return False
    
    def detalhes(self):
        print(f"Nome:{self.nome} ")
        print(f"Email: {self.email}")
        print(f"Média: {self.media:.2f}")
        print(f"Faltas: {self._falats}")
        if(self.aprovado):
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")

    




