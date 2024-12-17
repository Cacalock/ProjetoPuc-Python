import os
import time
decoracao = "=========================================================="

class Operacoes:
    def __init__(self):
        self.legenda = { 1: "estudante(s)", 2: "professor(a/es)" }
        self.lista = { 1: [], 2: [] }

    def incluir(self, decisao): 
        os.system("cls")
        while True:
            print(f"=========================INCLUIR==========================")
            if not self.lista[decisao]:
                print(f"Não há {self.legenda[decisao]} cadastrado.")
                nome = input(f"Digite o nome de um novo {self.legenda[decisao]}  \n('s' para cancelar):")
                if nome.lower() == 's':
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                codigo = +1
                cpf = int(input("Digite seu cpf:"))
                self.lista[decisao].append({'codigo': codigo, 'nome': nome, 'cpf': cpf})
                print(f"Adicionado a lista com sucesso.: {codigo, nome, cpf}")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            else:
                try:
                    nome = input(f"Digite o nome de um novo {self.legenda[decisao]} \n('s' para cancelar):")
                    if nome.lower() == 's':
                        input("Aperte ENTER para sair.\n" + decoracao)
                        return
                    for item in self.lista[decisao]:
                        codigo = item['codigo'] + 1
                    cpf = int(input("Digite seu cpf:"))
                    self.lista[decisao].append({'codigo': codigo,'nome': nome, 'cpf': cpf})
                    print(f"Adicionado a lista com sucesso.: {codigo, nome, cpf,}")
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
            if not self.lista[decisao]:
                print(f"Não há {self.legenda[decisao]} para excluir")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            os.system('cls')                
            print("=========================EXCLUIR==========================")
            print(f"Lista de {self.legenda[decisao]}:")
            for item in self.lista[decisao]:
                print(f"{item}")    
            remover = (input(f"Escreva o codigo do {self.legenda[decisao]} que deseja excluir \n('s' para cancelar):"))
            if remover.lower() == 's':
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            for elemento, item in enumerate(self.lista[decisao]):
                if str(item['codigo']) == remover:
                    del self.lista[decisao][elemento]
                    print(f" {remover} removido com sucesso.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
                else:
                    print(f"Código {remover} não encontrado na lista.")
                    input("Aperte ENTER para sair.\n" + decoracao)
                    return
         

    def listar(self, decisao):
        os.system('cls')
        print("===========================LISTAR=========================")
        if not self.lista[decisao]:
            print(f"Não há {self.legenda[decisao]} cadastrado")
            input("Aperte ENTER para sair.\n" + decoracao)
            return
        else:   
            print(f"Lista de {self.legenda[decisao]}:")
            for item in self.lista[decisao]:
                print(f"{item}")
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
            if not self.lista[decisao]:
                print(f"Nao há nenhum {self.legenda[decisao]}")
                input("Aperte ENTER para sair.\n" + decoracao)
                return
            os.system('cls')                
            print("==========================EDITAR===========================")  
            print(f"Lista de {self.legenda[decisao]}:")
            for item in self.lista[decisao]:
                print(f"{item}")
            editor = input(f"Qual {self.legenda[decisao]} deseja editar? \n('s' para cancelar.)")
            if editor.lower() == 's':
                return
            for item in self.lista[decisao]:
                if str(item['codigo']) == editor:
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
                    os.system('cls')
                    return
                elif parametro == 2: 
                    editar_cpf = input("Digite o novo cpf: ")
                    item['cpf'] = editar_cpf
                    print(f"Atualização feita com sucesso!")
                    input("Aperte ENTER para sair.")
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
1. Incluir.
2. Listar.
3. Atualizar.
4. Excluir.
5. Editar.
6. Voltar ao menu principal.
============================================================================         
              

"""
            try: 
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
            except ValueError or KeyError:
                print("Escolha uma opção.")
                input('Aperte ENTER para sair.')
                os.system("cls")

if __name__ == "__main__":
    operacoes_menu = Menus()
    operacoes_menu.main()