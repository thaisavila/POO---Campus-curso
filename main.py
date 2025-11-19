from Campus import Campus
from Cursos import Cursos  

ufc = Campus()
curso = Cursos(ufc)

def create_campus():
  print("\n===Criar Novo Campus===")
  nome_do_campus = input("Digite o nome do novo campus: ")
  ufc.create(nome_do_campus)

def create_curso():
  print("\n===Criar Novo Curso===")
  nome_do_curso = input("Digite o nome do novo curso: ")
  nome_do_campus = input("Digite o nome do campus onde o curso será oferecido: ")
  curso.create(nome_do_curso, nome_do_campus)
  return

def read_campus():
  print("\n===Listar Campus===")
  ufc.read()

def read_cursos():
  print("\n===Listar Cursos de um Campus===")
  nome_do_campus = input("Digite o nome do campus: ")
  curso.read(nome_do_campus)

def read_all():
  print("\n===Listar Todos os Campus e Cursos===")
  ufc.read_all()

def update_campus():
  print("\n===Modificar Nome do Campus===")
  nome_do_campus_antigo = input("Digite o nome do campus que deseja modificar: ")
  nome_do_campus_novo = input("Digite o novo nome do campus: ")
  ufc.update(nome_do_campus_antigo, nome_do_campus_novo)

def update_curso():
  print("\n===Modificar Nome do Curso===")
  campus = input("Digite o nome do campus que  o curso pertence: ")
  curso_antigo = input("Digite o nome do curso que deseja modificar: ")
  curso_novo = input("Digite o novo nome do curso: ")
  curso.update(curso_antigo, curso_novo, campus)

def delete_campus():
    print("\n===Excluir Campus===")
    nome_do_campus = input("Digite o nome do campus que deseja excluir: ")
    ufc.delete(nome_do_campus)
  
def delete_curso():
    print("\n===Excluir Curso===")
    campus = input("Digite o nome do campus que o curso pertence: ")
    nome_do_curso = input("Digite o nome do curso que deseja excluir: ")
    curso.delete(nome_do_curso, campus)

while True:
  print("\n===============================")
  print("========== MENU UFC ===========")
  print("===============================\n")

  print("1. Criar novo Campus")
  print("2. Criar novo Curso")
  print("3. Listar campus existentes")
  print("4. Listar cursos de um campus")
  print("5. Listar todos os campus e cursos")
  print("6. Modificar nome do Campus")
  print("7. Modificar nome do Curso")
  print("8. Excluir campus")
  print("9. Excluir curso")
  print("10. Sair\n")

  opcao = input("Escolha uma opção de 1 a 10: ")
  if opcao == "1":
    create_campus()
  elif opcao == "2":
    create_curso()
  elif opcao == "3":
    read_campus()
  elif opcao == "4":
    read_cursos()
  elif opcao == "5":
    read_all()
  elif opcao == "6":
    update_campus()
  elif opcao == "7":
    update_curso()
  elif opcao == "8":
    delete_campus()
  elif opcao == "9":
    delete_curso()  
  elif opcao == "10":
    print("Saindo do sistema... Até logo!")
    break
  else:
    print("Opção inválida! Digite um número de 1 a 9")