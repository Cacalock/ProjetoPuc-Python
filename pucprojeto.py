import os
import time

def main(): 
    print(f"___________________MENU PRINCIPAL___________________")
    print(f"1. Estudantes.")
    print(f"2. Professores.")
    print(f"3. Disciplinas.")
    print(f"4. Turmas.")
    print(f"5. Matriculas.")
    print(f"6. Sair.")

    
    while True:
      opcao = input("Escolha uma das opções: ")
      if opcao == "1" or "2" or "3" or "4" or "5" or "6":
        print(f"A opção escolhida foi {opcao}") 
        if opcao == "6":
          print("Saindo")
          time.sleep(3)
          quit()
      mainname = opcao
      if mainname == "1": 
        mainname = "[ESTUDANTES]"
      elif mainname == "2":
        mainname = "[PROFESSORES]"
      elif mainname == "3":
        mainname = "[DISCIPLINAS]"
      elif mainname == "4":
        mainname = "[TURMAS]"
      elif mainname == "5":
        mainname = "[MATRICULAS]"
      else:
        mainname = "_"
        print(f"Opção invalida.")
        print(f"Escolha uma opção valida.")
        time.sleep(3)
        main()       
      

      print(f"___________________" + mainname + " MENU ___________________")
      print(f"1. Incluir.")
      print(f"2. Listar.")
      print(f"3. Atualizar.")
      print(f"4. Excluir.")
      print(f"5. Voltar ao menu principal.")
      menu2 = int(input("Escolha uma opção: "))
      if menu2 <= 6:
          print(f"Opção valida.")
      else:
        print(f"Opção invalida.")
        main()
        
      match menu2:
        case 1:
          print(f"___________________INCLUIR___________________")
          print(f"Carregando menu de incluir...")
          os.system("pause")
          break
        case 2:
          print(f"___________________LISTAR___________________")
          print(f"Carregando menu de listar...")
          os.system("pause")
          break
        case 3:
          print(f"___________________ATUALIZAR___________________")
          print(f"Carregando menu de atualização...")
          os.system("pause")
          break
        case 4:
          print(f"___________________EXCLUIR___________________")
          print(f"Carregando menu de exclusão...")
          os.system("pause")
          break
        case 5:
            main()

main()