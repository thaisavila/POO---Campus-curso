from Campus import Campus
from Cursos import Cursos

def menu():
  print("===============================")
  print("========== MENU UFC ===========")
  print("===============================")
  
def gerenciar_campus():
    print("\n=== Gerenciar Campus ===")
    print("1. Criar novo Campus")
    print("2. Listar campus existentes")
    print("3. Modificar nome do Campus")
    print("4. Excluir campus")
    print("5. Voltar ao menu principal da UFC")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      print("=== Criar Campus ===")
      novo_campus = input("Digite o nome do campus: ")
      novo_campus = Campus()

    elif opcao == "2":
       pass

    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        return
    else:
        print("Opção inválida! Digite um número de 1 a 5")


def gerenciar_cursos():
    print("\n=== Gerenciar Cursos ===")
    print("1. Criar novo Curso")
    print("2. Listar cursos existentes")
    print("3. Modificar nome do Curso")
    print("4. Excluir curso")
    print("5. Voltar ao menu principal da UFC")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        pass  # implementar depois
    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        return
    else:
        print("Opção inválida! Digite um número de 1 a 5")

def listar():
  pass

while True:
  print("\n1. Gerenciar Campus")
  print("2. Gerenciar Cursos")
  print("3. Listar Campus e Cursos")
  print("4. Sair")

  opcao = input("Escolha uma opção de 1 a 4: ")
  if opcao == "1":
    gerenciar_campus()
  elif opcao == "2":
    gerenciar_cursos()
  elif opcao == "3":
    listar()
  elif opcao == "4":
    print("Saindo do sistema... Até logo!")
    break
  else:
    print("Opção inválida! Digite um número de 1 a 4")