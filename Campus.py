class Campus():
  def __init__(self):
    self.campus = ["Pici", "Itapajé", "Sobral"]
    self.cursos_por_campus = {"Pici":["Civil", "Musica"], "Itapajé":["ADS", "SI","CD"], "Sobral":["Medicina", "Psicologia"]}

  def create(self, nome_do_campus):
    """Função para CRIAR um novo campus"""
    if nome_do_campus in self.campus:
      print(f"Campus '{nome_do_campus}' já existe!")
    else:
      self.campus.append(nome_do_campus)
      print(f"Campus de {nome_do_campus} cadastrado com sucesso!")
    
  def read(self):
    # Função para listar os campus que já existem 
    if not self.campus:
      print("Nenhum campus cadastrado!")
    else:
      cont = 0
      for i in self.campus:
        cont+=1
        print(f"{cont}. {i}")


  def update(self, nome_do_campus_antigo, nome_do_campus_novo):
    if nome_do_campus_antigo not in self.campus:
      print(f"{nome_do_campus_antigo} não é um campus!")
    else:
      for i in range(len(self.campus)):
        if self.campus[i] == nome_do_campus_antigo:
          self.campus[i] = nome_do_campus_novo
          print(f"Campus '{nome_do_campus_antigo}' modificado para '{nome_do_campus_novo}' com sucesso!")
          break

  def delete(self, nome_do_campus):
    if nome_do_campus not in self.campus:
      print(f"{nome_do_campus} não é um campus!")
    else:
          self.campus.remove(nome_do_campus)
          print(f"Campus '{nome_do_campus}' excluído com sucesso!")

Poraganbuçu = Campus()
Poraganbuçu.create("Piauí")
Poraganbuçu.read()
Poraganbuçu.update("Pici","Acre")
Poraganbuçu.read
Poraganbuçu.delete("Itapajé")
Poraganbuçu.read()