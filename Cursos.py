from Campus import Campus

class Cursos():
  def __init__(self, campus):
    self.cursos = self.campus[campus]
    self.campus = campus

  def create(self, curso, campus):
    """Função para CRIAR um novo curso"""
    if curso in self.cursos:
      print(f"Curso '{curso}' já existe!")
    elif campus not in self.campus:
      print(f"Campus {campus} não existe!")
    else:
      self.cursos.append(curso)
      print(f"Curso '{curso}' cadastrado com sucesso!")

      self.cursos_por_campus[campus] = self.cursos

  def read(self):
    # Função para listar os cursos que já existem 
    if not self.cursos:
      print("Nenhum curso cadastrado!")
    else:
      cont = 0
      for i in self.cursos:
        cont+=1
        print(f"{cont}. {i}")

  def update(self,curso_antigo,curso_novo):
    if curso_antigo not in self.cursos:
      print(f"{curso_antigo} não é um curso!")
    else:
      for i in range(len(self.cursos)):
        if self.cursos[i] == curso_antigo:
          self.cursos[i] = curso_novo
          print(f"Curso '{curso_antigo}' modificado para '{curso_novo}' com sucesso!")
          break

  def delete(self,curso):
    if curso not in self.cursos:
      print(f"{curso} não é um curso!")
    else:
          self.cursos.remove(curso)
          print(f"Curso '{curso}' excluído com sucesso!")

cursos = Cursos("Pici")
cursos.read()