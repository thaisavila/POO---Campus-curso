# Sistema de Gerenciamento de Campus e Cursos (POO em Python)

Este projeto é a implementação de um CRUD desenvolvido em **Python** e utilizando **Programação Orientada a Objetos (POO)**, para gerenciar *cursos* pertencentes a diferentes *campus*.

---

## Estrutura do Projeto

```
Campus-Curso/
├── Campus.py
├── Cursos.py
├── main.py
└── README.md
```

### **Campus.py**

Contém a classe `Campus`, que armazena:
* Dicionário `cursos_por_campus` contendo os campus e os cursos de cada campus

É responsável por:
* Criar campus
* Listar campus
* Atualizar campus
* Remover campus

### **Cursos.py**

Contém a classe `Cursos`, responsável por:

* Criar um curso
* Listar cursos
* Atualizar/modificar curso
* Remover curso

Ela recebe um **objeto Campus** no construtor, permitindo acessar o dicionário `cursos_por_campus`.

### **main.py**

Arquivo principal que:

* Cria os objetos
* Mostra o menu no terminal
* Executa as funções de CRUD
* Interage diretamente com o usuário

---

## ▶ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone ou baixe o repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```
python main.py
```

---

## 👩‍💻 Autora

Projeto desenvolvido por **Thais Ávila**.
Objetivo: praticar Python, POO e estruturas de dados.