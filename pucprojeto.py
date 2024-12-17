import os
import time
decoracao = "=========================================================="
class Operacoes:
    def __init__(self):
        self.lista = {}
        self.legenda = {1: "estudante(s)", 2: "professor(a/es)"}

    def incluir(self, decisao): 
        os.system("cls")
        while True:
            print(f"=========================INCLUIR==========================")
            if not self.lista:
                print(f"Não há {self.legenda[decisao]} cadastrado.")
                codigo = input(f"Digite o codigo de um novo {self.legenda[decisao]}  \n('s' para cancelar):")
                if codigo.lower() == 's':
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                nome = input("Informe o seu nome:")
                cpf = int(input("Digite seu cpf:"))
                self.lista[codigo] = {'nome': nome, 'cpf': cpf}
                print(f"Adicionado a lista com sucesso.: {codigo, nome, cpf}")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            else:
                codigo = input(f"Digite o codigo de um novo {self.legenda[decisao]} \n('s' para cancelar):")
                if codigo.lower() == 's':
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                nome = input("Digite seu nome:")
                cpf = int(input("Digite seu cpf:"))
                if codigo in self.lista:
                    print(f"Codigo de {self.legenda[decisao]} ja está na lista.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                self.lista[codigo] = {'nome': nome, 'cpf': cpf}
                print(f"Adicionado a lista com sucesso.: {codigo, nome, cpf,}")
                input("Aperte ENTER para sair.\n" + decoracao)
                return

    def excluir(self, decisao):
        os.system("cls")
        while True:
            print("=========================EXCLUIR==========================")
            if not self.lista:
                print(f"Não há {self.legenda[decisao]} para excluir")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            os.system('cls')                
            print("=========================EXCLUIR==========================")
            print(f"Lista de {self.legenda[decisao]}:")
            for codigo,item in self.lista.items():
                print(codigo,item)
            remover = (input(f"Escreva o codigo do {self.legenda[decisao]} que deseja excluir \n('s' para cancelar):"))
            if remover.lower() == 's':
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            try:
                remover = (remover)
                if remover in self.lista:
                    del self.lista[remover]
                    print(f"{remover} removido com seucesso.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                else:
                    print(f"Código {remover} não encontrado na lista.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
            except ValueError:
                print(f"Código {remover} não encontrado na lista.")
                input("Aperte ENTER para sair.\n" + decoracao)
                return

    def listar(self, decisao):
        os.system('cls')
        print("===========================LISTAR=========================")
        if not self.lista:
            print(f"Não há {self.legenda[decisao]} cadastrado")
            input("Aperte ENTER para sair.\n" + decoracao)
            return
        else:   
            print(f"Lista de {self.legenda[decisao]}:")
            for elemento,valor in self.lista.items():
                print(f"codigo:",elemento,valor)
            input("Aperte ENTER para sair.\n" + decoracao)
            return

    def atualizar(self):
        os.system("cls")
        print(f"=========================ATUALIZAR========================")           
        print("Atualizando...")
        time.sleep(2)
        print("Atualização feita com sucesso! \n"
        "Voltando ao menu anterior:\n" + decoracao)
        time.sleep(2)
        return
        
    def editar(self,decisao):
        os.system('cls')
        while True:
            print("==========================EDITAR===========================")  
            if not self.lista:
                print(f"Nao há nenhum {self.legenda[decisao]}")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            try:
                os.system('cls')                
                print("==========================EDITAR===========================")  
                print(f"Lista de {self.legenda[decisao]}:")
                for elemento,valor in self.lista.items():
                    print(elemento,valor)
                editor = input(f"Qual {self.legenda[decisao]} deseja editar? \n('s' para cancelar.)")
                if editor.lower() == 's':
                    return
                print(""" 
==========================================================
1. Editar nome.
2. Editar cpf.
3. Editar codigo. 
==========================================================              
                      """)        
                parametro = int(input())
                if parametro == 1:
                    editar_nome = input("Digite o novo cpf: ")
                    self.lista[editor]['nome'] = editar_nome
                    print(f"Atualização feita com sucesso!")
                    input("Aperte ENTER para sair.")
                    os.system('cls')
                    return
                elif parametro == 2: 
                    editar_cpf = input("Digite o novo cpf: ")
                    self.lista[editor]['cpf'] = editar_cpf
                    print(f"Atualização feita com sucesso!")
                    input("Aperte ENTER para sair.")
                    os.system('cls')
                    return
                elif parametro == 3:
                    editar_codigo = input("Digite o novo codigo: ")
                    self.lista[editar_codigo] = self.lista.pop(editor)
                    print(f"Atualização feita com sucesso!")
                    input("Aperte ENTER para sair.")
                    os.system('cls')
                    return
            except KeyError:  
                print(f"Codigo não encontrado na lista.")
                input("Aperte ENTER para sair.")
                return
class Menus:
    def __init__(self):
        self.operacoes = Operacoes()
        
    def mainOp(self, decisao):
        while True:
            os.system("cls")
            raw_string = """
=============================MENU DE OPERAÇÕES=============================
1. Incluir.
2. Listar.
3. Atualizar.
4. Excluir.
5. Editar.
6. Voltar ao menu principal.
===========================================================================
"""
            print(raw_string)
            opcao = int(input())
            match opcao:
                case 1:
                    self.operacoes.incluir(decisao)
                case 2:
                    self.operacoes.listar(decisao)
                case 3:
                    self.operacoes.atualizar()
                case 4:
                    self.operacoes.excluir(decisao)
                case 5:
                    self.operacoes.editar(decisao)
                case 6:
                    os.system("cls")
                    return
                case _:
                    print("Opcao invalida.")

    def main(self):
        os.system("cls")
        while True:
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
            decisao = int(input())
            match decisao:
                case 1:
                    self.mainOp(decisao)
                case 2:
                    self.mainOp(decisao)
                case 3:
                    os.system("cls")
                    print(decoracao + "\nOPÇÃO EM DESENVOLVIMENTO.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    os.system("cls")
                case 4:
                    os.system("cls")
                    print(decoracao + "\nOPÇÃO EM DESENVOLVIMENTO.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    os.system("cls")
                case 5:
                    os.system("cls")
                    print(decoracao + "\nOPÇÃO EM DESENVOLVIMENTO.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    os.system("cls")
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

if __name__ == "__main__":
    operacoes_menu = Menus()
    operacoes_menu.main()