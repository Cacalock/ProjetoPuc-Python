import os
import time
import json
import copy

decoracao = "=========================================================="

arquivo = 'semana8.json'

class Operacoes:
    def __init__(self):
        self.legenda = { 1: 'estudante(s)', 2: 'professor(a/es)', 3: 'disciplina(s)', 4: 'turma(s)', 5: 'matricula(s)'}
        self.lista = self.carregar_lista()
        self.lixo = copy.copy(self.carregar_lista())

    def carregar_lista(self):
        try:
            if os.path.exists(arquivo):
                with open(arquivo, 'r') as f:
                    loaded_data = json.load(f)
                    loaded_data = {int(key): value for key, value in loaded_data.items()}  
                    return loaded_data
            else:
                return {1: [], 2: [], 3: [], 4: [], 5: []}
        except json.JSONDecodeError:
            print('Erro ao carregar arquivo.')
            return {1: [], 2: [], 3: [], 4: [], 5: []}


    def salvar_lista(self):
        with open(arquivo, 'w') as f:
            json.dump(self.lista, f)

    def Lixo(self, decisao):
        print(f"=========================LIXO=============================")
        if self.lixo[decisao]:
            for item in self.lixo[decisao]:
                print(item)
            input('Aperte ENTER para sair. \n' + decoracao)
            return
        else:
            print("O lixo está vazio.")
            input('Aperte ENTER para sair. \n' + decoracao)
            return
            
    def incluir(self, decisao): 
        while True: 
            os.system("cls")
            print(f"=========================INCLUIR==========================")
            try:
                if decisao == 1 or decisao == 2:
                        codigo = 1
                        nome = input(f"Digite o nome de um novo {self.legenda[decisao]} \n('s' para cancelar):")
                        if nome.lower() == 's':
                            input("Aperte ENTER para sair.\n" + decoracao)
                            return
                        for item in self.lista[decisao]:
                            codigo = item['codigo'] + 1
                        cpf = int(input("Digite seu cpf:"))
                        self.lista[decisao].append({'codigo': codigo,'nome': nome, 'cpf': cpf})
                        print(f"Adicionado a lista com sucesso.: {codigo, nome, cpf,}")
                        self.salvar_lista()
                        input("Aperte ENTER para sair.\n" + decoracao)
                        os.system("cls")
                        return
                elif decisao == 3:
                        codigo = 1
                        for item in self.lista[decisao]:
                            codigo = item['codigo'] + 1
                        nome = input(f"Digite o nome de uma nova disciplina: \n('s' para cancelar):")
                        if nome.lower() == 's':
                            input("Aperte ENTER para sair.\n" + decoracao)
                            return
                        self.lista[decisao].append({'codigo': codigo,'nome': nome})
                        print(f"Adicionado a lista com sucesso.: {codigo, nome}")
                        self.salvar_lista()
                        input("Aperte ENTER para sair.\n" + decoracao)
                        os.system("cls")
                        return
                elif decisao == 4:
                    codigo = 1
                    for item in self.lista[decisao]:
                        codigo = item['codigo'] + 1
                    disciplina = input(f"Digite o codigo da disciplina: \n('s' para cancelar):")
                    if disciplina.lower() == 's':
                        input("Aperte ENTER para sair.\n" + decoracao)
                        return
                    professor = input(f"Digite o codigo do professor:")
                    for item in self.lista[decisao]:
                        codigo = item['codigo'] + 1
                    self.lista[decisao].append({'codigo':codigo, 'disciplina': disciplina ,'professor':professor})
                    self.salvar_lista()
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                elif decisao == 5:
                    codigo = 1
                    for item in self.lista[decisao]:
                        codigo = item['codigo'] + 1
                    turma = input(f"Digite o codigo da turma: \n('s' para cancelar):")
                    if turma.lower() == 's':
                        input("Aperte ENTER para sair.\n" + decoracao)
                        return
                    estudante = input(f"Digite o codigo do estudante:")
                    self.lista[decisao].append({'codigo':codigo, 'turma': turma,'estudante': estudante})
                    self.salvar_lista()
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
            except ValueError or KeyError:
                    print('São apenas permitidos número.' +
                                '\nTente novamente')
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return

    def excluir(self, decisao):
        os.system("cls")
        while True:
            print("=========================EXCLUIR==========================")
            if len(self.carregar_lista()[decisao]) == 0:
                print(f"Não há {self.legenda[decisao]} para excluir")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            os.system('cls')                
            print("=========================EXCLUIR==========================")
            print(f"Lista de {self.legenda[decisao]}:")
            for item in self.carregar_lista()[decisao]:
                print(item)
            else: 
                try:
                    remover = int((input(f"Escreva o codigo do {self.legenda[decisao]} que deseja excluir \n('0' para cancelar):")))
                    if remover == '0':
                            input("Aperte ENTER para sair.\n" + decoracao)
                            self.salvar_lista()
                            return
                    for elemento, item in enumerate(self.carregar_lista()[decisao]):
                        if item['codigo'] == remover:
                            self.lixo = copy.copy(self.carregar_lista())
                            del self.lista[decisao][elemento]
                            print(f" {remover} removido com sucesso.")
                            input("Aperte ENTER para sair.\n" + decoracao)
                            self.salvar_lista()
                            return
                except ValueError:
                    print("Escolha um dos codigos na lista.")         

    def listar(self, decisao):
        os.system('cls')
        print("===========================LISTAR=========================")
        if len(self.carregar_lista()[decisao]) == []:
            print(f"Não há {self.legenda[decisao]} cadastrado")
            input("Aperte ENTER para sair.\n" + decoracao)
            return
        else:
            print(f"Lista de {self.legenda[decisao]}:")
            for item in self.carregar_lista()[decisao]:
                print(item)
            input("Aperte ENTER para sair.\n" + decoracao)
            return

    def editar(self,decisao):
        os.system('cls')
        while True:
            print("==========================EDITAR===========================")  
            if not self.lista[decisao]:
                print(f"Nao há nenhum {self.legenda[decisao]}")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            os.system('cls')                
            print("==========================EDITAR===========================")  
            print(f"Lista de {self.legenda[decisao]}:")
            for item in self.carregar_lista()[decisao]:
                print(item)
            if decisao == 1 or decisao == 2:
                editor = int(input(f"Qual {self.legenda[decisao]} deseja editar? \n('0' para cancelar.)"))
                if editor == '0':
                    return   
                for item in self.lista[decisao]:
                    if item['codigo'] == editor:
                        print(""" 
==========================================================
1. Editar nome.
2. Editar cpf.
==========================================================              
""")        
                        parametro = int(input())
                        if parametro == 1:
                            editar_nome = input("Digite o novo nome: ")
                            item['nome'] = editar_nome
                            print(f"Atualização feita com sucesso!")
                            input("Aperte ENTER para sair.")
                            self.salvar_lista()
                            os.system('cls')
                            return
                        elif parametro == 2: 
                            editar_cpf = input("Digite o novo cpf: ")
                            item['cpf'] = editar_cpf
                            print(f"Atualização feita com sucesso!")
                            input("Aperte ENTER para sair.")
                            self.salvar_lista()
                            os.system('cls')
                            return
                        else:
                            print("Opção inválida.")
                            input("Aperte ENTER para sair.")
                            os.system('cls')                
                            return
            elif decisao == 3:
                editor = int(input(f"Qual {self.legenda[decisao]} deseja editar? \n('0' para cancelar.)"))
                if editor == '0':
                    return   
                for item in self.lista[decisao]:
                    if item['codigo'] == editor:
                        editar_nome = input("Digite o novo nome: ")
                        item['nome'] = editar_nome
                        print(f"Atualização feita com sucesso!")
                        input("Aperte ENTER para sair.")
                        self.salvar_lista()
                        os.system('cls')
                        return
            elif decisao == 4:
                editor = int(input(f"Qual {self.legenda[decisao]} deseja editar? \n('0' para cancelar.)"))
                if editor == '0':
                    return   
                for item in self.lista[decisao]:
                    if item['codigo'] == editor:
                        print(""" 
==========================================================
1. Editar professor.
2. Editar disciplina.
==========================================================              
""")        
                        parametro = int(input())
                        if parametro == 1:
                            editar_nome = input("Edite o nome do professor: ")
                            item['professor'] = editar_nome
                            print(f"Atualização feita com sucesso!")
                            input("Aperte ENTER para sair.")
                            self.salvar_lista()
                            os.system('cls')
                            return
                        if parametro == 2:
                            editar_nome = input("Edite o nome do estudante: ")
                            item['disciplina'] = editar_nome
                            print(f"Atualização feita com sucesso!")
                            input("Aperte ENTER para sair.")
                            self.salvar_lista()
                            os.system('cls')
                            return
                        else:
                            print("Opção inválida.")
                            input("Aperte ENTER para sair.")
                            os.system('cls')                
                            return
            elif decisao == 5:
                editor = int(input(f"Qual {self.legenda[decisao]} deseja editar? \n('0' para cancelar.)"))
                if editor == '0':
                    return   
                for item in self.lista[decisao]:
                    if item['codigo'] == editor:
                        print(""" 
==========================================================
1. Editar estudante.
2. Editar turma.
==========================================================              
""")        
                        parametro = int(input())
                        if parametro == 1:
                            editar_nome = input("Edite o nome do estudante: ")
                            item['estudante'] = editar_nome
                            print(f"Atualização feita com sucesso!")
                            input("Aperte ENTER para sair.")
                            self.salvar_lista()
                            os.system('cls')
                            return
                        if parametro == 2:
                            editar_nome = input("Edite o nome do estudante: ")
                            item['turma'] = editar_nome
                            print(f"Atualização feita com sucesso!")
                            input("Aperte ENTER para sair.")
                            self.salvar_lista()
                            os.system('cls')
                            return
                        else:
                            print("Opção inválida.")
                            input("Aperte ENTER para sair.")
                            os.system('cls')                
                            return
                        
class Menus:
    def __init__(self):
        self.operacoes = Operacoes()
        
    def mainOp(self, decisao):
        while True:
            os.system("cls")
            raw_string = """
=============================MENU DE OPERAÇÕES=============================
1.Incluir.
2.Listar.
3.Excluir.
4.Lixo.
5.Editar.
6.Voltar ao menu principal.
============================================================================         
"""
            try: 
                print(raw_string)
                opcao = int(input())
                match opcao:
                    case 1:
                        self.operacoes.incluir(decisao)
                        os.system("cls")
                    case 2:
                        self.operacoes.listar(decisao)
                        os.system("cls")
                    case 3:
                        self.operacoes.excluir(decisao)
                        os.system("cls")
                    case 4:
                        os.system("cls")
                        self.operacoes.Lixo(decisao)
                    case 5:
                        os.system("cls")
                        self.operacoes.editar(decisao)
                    case 6:
                        os.system("cls")
                        return
                    case _:
                        print("Opcao invalida.")
            except ValueError or KeyError:
                print("Escolha uma opção.")
                input('Aperte ENTER para sair.')
                return
    def main(self):
        while True:
            os.system("cls")
            print( """
=============================MENU PRINCIPAL=============================
1. Estudantes.
2. Professores.
3. Disciplinas.
4. Turmas.
5. Matriculas.
6. Sair.
========================================================================
""")  
            try:
                decisao = int(input())
                match decisao:
                    case 1:
                        self.mainOp(decisao)
                    case 2:
                        self.mainOp(decisao)
                    case 3:
                        self.mainOp(decisao)
                    case 4:
                        self.mainOp(decisao)
                    case 5:
                        self.mainOp(decisao)
                    case 6:
                        print("Saindo...")
                        time.sleep(3)
                        quit()
                    case _:
                        os.system("cls")
                        print(decoracao + "\nOpção inválida. Tente novamente.")
                        input("Aperte ENTER para sair.\n" + decoracao)
                        os.system("cls")
                        Menus.main(decisao)
            except ValueError or KeyError:
                print("Escolha uma opção.")
                input('Aperte ENTER para sair.')
                os.system("cls")

if __name__ == "__main__":
    operacoes_menu = Menus()
    operacoes_menu.main()