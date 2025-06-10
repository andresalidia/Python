from classes import Aluno, AlunoTecnico

def recebe_int(nome_campo):

    while True:
        res = input(f'{nome_campo}: ')
        try:
            res = int(res)
            break
        except:
            print(f'{nome_campo} deve ser int!')

    return res

def recebe_float(nome_campo):

    while True:
        res = input(f'{nome_campo}: ')
        try:
            res = float(res)
            break
        except:
            print(f'{nome_campo} deve ser float!')

    return res

class Menu:
    """
    Cria um menu com título e opções a partir de um dicionário
    """
    def __init__(self, titulo, menu):
        self.titulo = titulo 
        self.menu = menu

    @staticmethod
    def mostrar_menu(titulo, raiz, nivel):
        elementos = list(raiz.items())

        while True:
            i = 1
            # print(titulo)
            for opcao, _ in elementos:
                print(f'{' '*nivel}{i} - {opcao.title()}')
                i += 1

            print(f'{' '*nivel}0 - Voltar')

            try:
                opc = abs(int(input('>>> ')))
            except:
                print('\nOpção inválida\n')
                continue 
            
            if opc == 0:
                break

            if opc <= len(elementos):
                titulo, resultado = elementos[opc-1]
                if isinstance(resultado, dict):
                    Menu.mostrar_menu(titulo, resultado, nivel+1)
                elif callable(resultado):
                    resultado()
            else:
                print('\nOpção inválida\n')
                continue 

    def poll(self):
        Menu.mostrar_menu(self.titulo, self.menu, 0)

class Programa:
    alunos = {}

    def dummy(self):
        pass

    def cadastrar_novo_aluno(self, tecnico = True):
        nome = input('Nome: ')
        email = input('Email: ')
        senha = input('Senha: ')
        semestre = recebe_int('Semestre')
        matricula = recebe_int('Matricula')

        if tecnico:
            novo_aluno = AlunoTecnico(nome=nome, email=email, senha=senha, semestre=semestre, matricula=matricula)
        else:
            novo_aluno = Aluno(nome=nome, email=email, senha=senha, semestre=semestre, matricula=matricula)

        self.alunos[matricula] = novo_aluno
        print(f'Aluno criado, aluno {nome} - {matricula}')

    def cadastrar_aluno_tecnico(self):
        self.cadastrar_novo_aluno(tecnico=True)
    
    def cadastrar_aluno(self):
        self.cadastrar_novo_aluno(tecnico=False)

    def get_aluno(self):
        matricula = recebe_int('Matricula')

        if matricula not in self.alunos:
            print(f'Aluno com matricula ({matricula}) não existe') 
            return None
    
        return self.alunos[matricula]

    def listar_info_aluno(self):
        aluno = self.get_aluno() 
        if aluno is not None: 
            aluno.detalhes()

    def listar_info_alunos(self):
        for aluno in self.alunos.values():
            print('-' * 80)
            aluno.detalhes()

    def login(self):
        matricula = recebe_int('Matricula')
        senha = input('Senha: ')
        
        if matricula not in self.alunos:
            print(f'Matricula ou senha inválidos') 
        else:
            if self.alunos[matricula].confere_senha(senha):
                print(f'Login efetuado com sucesso!')
            else:
                print(f'Matricula ou senha inválidos') 

    def adicionar_nota(self):
        aluno = self.get_aluno()
        
        if aluno is not None:
            semestre = recebe_int('Semestre')
            nota = recebe_float('Nota')
            aluno.set_nota(semestre=semestre, nota=nota)  
            print(f'Nota adicionada, aluno {aluno.nome}')

    def remover_nota(self):
        aluno = self.get_aluno()
        
        if aluno is not None:
            semestre = recebe_int('Semestre')
            nota = recebe_float('Nota')
            aluno.del_nota(semestre=semestre, nota=nota)        
            print(f'Nota removida, aluno {aluno.nome}')

    def adicionar_faltas(self):
        aluno = self.get_aluno()
        
        if aluno is not None:
            if isinstance(aluno, AlunoTecnico):
                faltas = recebe_int('Faltas')
                aluno.add_falta(faltas)
                print(f'Faltas adicionadas, aluno {aluno.nome}')
            else:
                print(f'Aluno {aluno.nome} não é técnico!')

    def __init__(self):
        self.__menu = Menu("Gestor Escolar",
            {
                'Cadastro': {
                    'Aluno': self.cadastrar_aluno,
                    'AlunoTecnico': self.cadastrar_aluno_tecnico
                },
                'Listar Informações Aluno': {
                    'Por Matricula': self.listar_info_aluno,
                    'Todos': self.listar_info_alunos
                },       
                'Alterar notas': {
                    'Adicionar/modificar nota': self.adicionar_nota,
                    'Remover nota': self.remover_nota,
                },
                'Adicionar faltas': self.adicionar_faltas,
                'Verificar Login': self.login
            }
        )

    def menu(self):
        self.__menu.poll()

if __name__ == '__main__':
    programa = Programa()
    programa.menu()

