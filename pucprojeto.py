import os
import time

def estudantes():
    lista = []
    while True:
        os.system("cls")
        raw_string = """
___________________MENU DOS ESTUDANTES___________________
1. Incluir.
2. Listar.
3. Atualizar.
4. Excluir.
5. Voltar oa menu principal. 
        """
        print(raw_string)
        switch = int(input())
        match switch:
            case 1:
                os.system("cls")
                for nome in range(1):
                    if lista == []:
                        print("___________________INCLUIR___________________\n")
                        print("Não há nenhum estudante cadastrado.")
                        nome = input("Digite o nome de um novo estudante: ")
                        lista.append(nome)
                        print("___________________LISTAGEM___________________\n")
                        print(nome)
                    elif lista != []:
                        print("___________________INCLUIR___________________\n")
                        nome = input("Digite o nome de um novo estudante: ")
                        lista.append(nome)
                        print("___________________LISTAGEM___________________\n")
                        print(nome)
            case 2:
                os.system("cls")
                if lista == []:
                    print("___________________LISTAGEM___________________\n"
                    "Não há nada cadastrados")
                    input("Aperte ENTER para sair.")
                    estudantes()
                else:
                    print("___________________LISTAGEM___________________")
                    for nome in (lista):
                        print(nome)

                    input("Aperte ENTER para sair.")
            case 3:
                os.system("cls")
                print("___________________ATUALIZAR___________________\n")
                print("atualizando")
                time.sleep(2)
                print("atuzalição feita com sucesso! \n" 
                "Voltando ao menu anterior:")
                time.sleep(2)
                estudantes()

            case 4:
                os.system("cls")
                print("___________________EXCLUIR___________________\n")
                remover = input("Escreva o nome do estudante que deseja excluir:")
                lista.remove(remover)    
                print("Exclusão feita com sucesso")
                time.sleep(2)
                print(f"mostrando atualizacão:\n")
                print("___________________LISTAGEM___________________")
                for nome in (lista):
                        print(nome)
                input("Aperte ENTER para sair.")

            case 5:
                return

def main():
    os.system("cls")
    raw_string ="""
___________________MENU PRINCIPAL___________________
1. Estudantes.
2. Professores.
3. Disciplinas.
4. Turmas.
5. Matriculas.
6. Sair.
"""
    while True:
        print(raw_string)
        switch = int(input())
        match switch:
            case 1:
                estudantes()

            case 2:
                print("___________________MENU DOS PROFESSORES___________________ \n"
                "Em desenvolvimento.")
                input("Aperte ENTER para sair.")


            case 3:
                print("___________________MENU DAS DISCIPLINAS___________________ \n"
                "Em desenvolvimento.")
                input("Aperte ENTER para sair.")

            case 4:
                print("___________________MENU DAS TURMAS___________________\n" 
                "Em desenvolvimento.")
                input("Aperte ENTER para sair.")
            case 5:
                print("___________________MENU DAS MATRICULAS___________________\n"
                "Em desenvolvimento.")
                input("Aperte ENTER para sair.")
            case 6:
                print("Saindo")
                time.sleep(3)
                quit()

if __name__ == "__main__":
    main()