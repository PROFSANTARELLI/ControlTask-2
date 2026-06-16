# Aula 2 – Construindo o ControlTask - Engenharia de Software Orientada à IA

Na Aula 1 realizamos toda a fase de planejamento do projeto:

* Levantamento de requisitos
* User Stories
* Casos de Uso
* Backlog do Produto
* Arquitetura da Solução
* Modelo de Dados

Agora chegou o momento de transformar esses artefatos em software.

Ao final desta aula teremos uma aplicação funcional composta por:

* Frontend Streamlit
* Backend FastAPI
* Banco de Dados SQLite
* ORM SQLAlchemy
* Versionamento GitHub

---

# Visão Geral da Arquitetura

```text
Usuário
   ↓
Streamlit
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
SQLite
```

Cada camada possui uma responsabilidade específica:

### Streamlit

Responsável pela interface do usuário.

Permite:

* Criar telas
* Capturar informações
* Exibir dados

### FastAPI

Responsável pelas regras de negócio.

Permite:

* Receber requisições
* Validar dados
* Processar informações
* Retornar resultados

### SQLAlchemy

Responsável pelo mapeamento objeto-relacional (ORM).

Permite:

* Trabalhar com classes Python
* Evitar SQL manual
* Facilitar manutenção

### SQLite

Responsável pela persistência dos dados.

---

# Ferramentas Utilizadas

## Desenvolvimento

* Python 3.12+
* Visual Studio Code

## IA

* Gemini

## Backend

* FastAPI

## Frontend

* Streamlit

## Banco de Dados

* SQLite
* SQLAlchemy

## Versionamento

* Git
* GitHub

---

# Etapa 1 – Clonando o Projeto

Abra o terminal.

Clone o repositório criado na Aula 1.

```bash
git clone https://github.com/SEU-USUARIO/controltask.git
```

Entre na pasta:

```bash
cd controltask
```

Abra no VS Code:

```bash
code .
```

---

# Etapa 2 – Criando o Ambiente Virtual

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

# Etapa 3 – Instalando Dependências

Instalar bibliotecas:

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install streamlit
pip install requests
 pip install email_validator
```

Gerar requirements.txt

```bash
pip freeze > requirements.txt
```

---

# Etapa 4 – Estrutura do Projeto

Criar estrutura:

```text
controltask/

├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│
├── frontend/
│   └── app.py
│
├── docs/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# Etapa 5 – Criando o Banco de Dados

Arquivo:

```text
backend/database.py
```

Responsável por:

* Conectar ao SQLite
* Criar sessão
* Inicializar banco

Prompt Gemini:

"Crie um arquivo database.py utilizando SQLAlchemy para conexão SQLite seguindo boas práticas."

Copie o código gerado.

---

# Etapa 6 – Criando os Modelos

Arquivo:

```text
backend/models.py
```

Modelos:

### Usuário

Campos:

* id
* nome
* email
* senha

### Tarefa

Campos:

* id
* titulo
* descricao
* prioridade
* status
* data_criacao

Prompt Gemini:

"Crie modelos SQLAlchemy para Usuário e Tarefa utilizando SQLite e relacionamentos adequados."

Copie o resultado.

---

# Etapa 7 – Criando a API

Arquivo:

```text
backend/main.py
```

Prompt Gemini:

"Crie uma API FastAPI para gerenciamento de tarefas contendo CRUD completo utilizando SQLAlchemy e SQLite."

Operações necessárias:

### Criar Tarefa

POST

```http
/tasks
```

---

### Listar Tarefas

GET

```http
/tasks
```

---

### Atualizar Tarefa

PUT

```http
/tasks/{id}
```

---

### Excluir Tarefa

DELETE

```http
/tasks/{id}
```

---

# Etapa 8 – Executando a API

No terminal:

```bash
uvicorn backend.main:app --reload
```

Resultado esperado:

```text
http://localhost:8000
```

---

# Etapa 9 – Testando com Swagger

Abrir:

```text
http://localhost:8000/docs
```

Validar:

* POST
* GET
* PUT
* DELETE

Criar algumas tarefas para teste.

Objetivo:

Verificar se a API está funcionando antes de construir a interface.

---

# Etapa 10 – Construindo o Frontend

Arquivo:

```text
frontend/app.py
```

Prompt Gemini:

"Crie uma interface Streamlit para consumir uma API FastAPI de gerenciamento de tarefas contendo cadastro, listagem, atualização e exclusão."

Funcionalidades:

* Campo Título
* Campo Descrição
* Campo Prioridade
* Botão Salvar
* Lista de tarefas

---

# Etapa 11 – Conectando Frontend e Backend

Fluxo:

```text
Usuário
 ↓
Streamlit
 ↓
Requests
 ↓
FastAPI
 ↓
SQLite
```

Toda ação realizada na interface deverá chamar os endpoints da API.

Exemplos:

### Criar

```python
requests.post()
```

### Listar

```python
requests.get()
```

### Atualizar

```python
requests.put()
```

### Excluir

```python
requests.delete()
```

---

# Etapa 12 – Executando a Interface

No terminal:

```bash
streamlit run frontend/app.py
```

Resultado esperado:

```text
http://localhost:8501
```

---

# Testes Funcionais

Validar:

## Cadastro

Criar tarefa.

Resultado esperado:

Dados gravados no SQLite.

---

## Consulta

Listar tarefas.

Resultado esperado:

Dados retornados pela API.

---

## Atualização

Editar tarefa.

Resultado esperado:

Registro alterado.

---

## Exclusão

Excluir tarefa.

Resultado esperado:

Registro removido.

---

# O que Aprendemos

Durante esta aula colocamos em prática diversos conceitos de Engenharia de Software:

* Arquitetura em Camadas
* APIs REST
* Persistência de Dados
* ORM
* CRUD
* Integração Frontend e Backend
* Desenvolvimento Assistido por IA

Percebemos que os artefatos produzidos durante a análise e projeto servem como guia para a implementação do sistema.

---

# Publicando no GitHub

Adicionar alterações:

```bash
git add .
```

Criar commit:

```bash
git commit -m "Aula 2 - Implementação inicial do ControlTask"
```

Enviar:

```bash
git push
```

---

# Entregas da Aula 2

Ao final desta aula teremos:

✅ Estrutura do projeto criada

✅ Banco SQLite funcionando

✅ Modelos SQLAlchemy implementados

✅ API FastAPI operacional

✅ CRUD completo de tarefas

✅ Interface Streamlit funcional

✅ Integração Frontend + Backend

✅ Código publicado no GitHub

---

# Preparação para a Aula 3

Na próxima aula iremos evoluir a qualidade do software através de:

* Git e GitHub
* Branches
* Boas práticas de desenvolvimento
* Testes automatizados com Pytest
* Refatoração assistida por IA
* Revisão de código utilizando Gemini
