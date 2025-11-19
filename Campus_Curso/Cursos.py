from .Campus import Campus

class Cursos():
  def __init__(self, campus):
    self.campus = campus

  def create(self, curso, nome_campus):
    """Função para CRIAR um novo curso"""
    
    if curso in self.campus.cursos_por_campus[nome_campus]:
      print(f"Curso '{curso}' já existe!")
    elif nome_campus not in self.campus.cursos_por_campus:
      print(f"Campus {nome_campus} não existe!")
    else:
      self.campus.cursos_por_campus[nome_campus].append(curso)
      print(f"Curso '{curso}' cadastrado com sucesso!")

  def read(self, nome_campus):
    """ Função para listar os cursos que já existem """ 

    if not self.campus.cursos_por_campus[nome_campus]:
      print("Nenhum curso cadastrado nesse campus!")
    else:
      cont = 0
      for i in self.campus.cursos_por_campus[nome_campus]:
        cont+=1
        print(f"{cont}. {i}")

  def update(self,curso_antigo,curso_novo,nome_campus):
    if curso_antigo not in self.campus.cursos_por_campus[nome_campus]:
      print(f"{curso_antigo} não é um curso do campus {nome_campus}!")
    else:
      for i in range(len(self.campus.cursos_por_campus[nome_campus])):
        if self.campus.cursos_por_campus[nome_campus][i] == curso_antigo:
          self.campus.cursos_por_campus[nome_campus][i] = curso_novo
          print(f"Curso '{curso_antigo}' modificado para '{curso_novo}' com sucesso!")
          break

  def delete(self,curso,nome_campus):
    if curso not in self.campus.cursos_por_campus[nome_campus]:
      print(f"Não existe o curso {curso} no campus {nome_campus}!")
    else:
          self.campus.cursos_por_campus[nome_campus].remove(curso)
          print(f"Curso '{curso}' excluído com sucesso!")

cursos = Cursos("Pici")