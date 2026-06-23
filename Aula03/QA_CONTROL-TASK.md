Aula 3 – Qualidade de Software, Testes e Integração Contínua

Nesta atividade, iremos assumir o papel de um profissional de Qualidade de Software (QA/Tester) responsável por:

1 - Baixar o projeto do repositório central;
2 - Configurar o ambiente de testes;
3 - Executar testes automatizados utilizando Pytest;
4 - Identificar e provocar falhas intencionalmente;
5 - Corrigir problemas encontrados;
6 - Publicar as alterações no GitHub;
7 - Automatizar a execução dos testes utilizando GitHub Actions.

Ao final da atividade, todo o projeto estará preparado para executar testes automaticamente a cada alteração realizada no código.

Cenário: Existe um repositório central chamado: ControlTask

O tester deverá:

GitHub
   ↓
Clonar Projeto
   ↓
Executar Testes Locais
   ↓
Identificar Problemas
   ↓
Corrigir Problemas
   ↓
Executar Novamente
   ↓
Enviar Alterações
   ↓
GitHub Actions
   ↓
Testes Automáticos


Etapa 1 – Clonar o Projeto

Abra o terminal do VS Code.

Execute:

git clone https://github.com/SEU-USUARIO/controltask.git (substitua pelo seu usuário real)

Entre no projeto:
cd controltask

Abra o projeto:
code .


Etapa 2 – Criar Ambiente Virtual

Criar ambiente:
python -m venv venv

Ativar:
Windows
venv\Scripts\activate

Linux/Mac
source venv/bin/activate


Etapa 3 – Instalar Dependências do Projeto

Caso exista:
pip install -r requirements.txt

Caso não exista:
pip install fastapi
pip install sqlalchemy
pip install streamlit
pip install uvicorn
pip install requests


Etapa 4 – Instalar Ferramentas de Teste

Instalar Pytest:
pip install pytest

Instalar biblioteca de testes para FastAPI:
pip install httpx

Instalar cliente de testes:
pip install pytest-cov

Atualizar dependências:
pip freeze > requirements.txt


Etapa 5 – Criar Estrutura de Testes

Criar pasta:
tests/

Estrutura:
tests/
├── test_api.py
├── test_database.py
├── test_models.py
└── __init__.py


Etapa 6 – Criando Testes Funcionais da API

Arquivo:
tests/test_api.py

Exemplo:

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "titulo": "Teste Pytest",
            "descricao": "Executando teste automatizado",
            "prioridade": "Alta",
            "status": "Pendente"
        }
    )

    assert response.status_code == 200

def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_update_task():
    response = client.put(
        "/tasks/1",
        json={
            "titulo": "Atualizado",
            "descricao": "Descrição atualizada",
            "prioridade": "Média",
            "status": "Concluída"
        }
    )

    assert response.status_code == 200

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200


Etapa 7 – Executar os Testes

Executar:

pytest

Resultado esperado:

=================== test session starts ===================

4 passed

=================== 100% ===================


Etapa 8 – Gerar Relatório de Cobertura

Executar:
pytest --cov

Exemplo:

Name                  Stmts   Miss Cover
----------------------------------------
backend/main.py          50      5   90%
backend/models.py        20      0  100%
----------------------------------------
TOTAL                    70      5   93%

Quanto maior a cobertura, maior a confiança no software.
Cobertura não garante ausência de erros.


Etapa 9 – Simulando Erros no Sistema

Agora iremos provocar falhas intencionalmente.

Objetivo: Demonstrar o valor dos testes automatizados.

Exemplo 1 – Alterar endpoint

No arquivo:
backend/main.py

Alterar:
De:
@app.get("/tasks")

Para:
@app.get("/tarefas")

Executar novamente:
pytest

Resultado:
FAILED test_list_tasks

Exemplo 2 – Alterar nome de campo

Arquivo:
models.py

Alterar:
De:
titulo

Para:
titulo_tarefa

Executar:
pytest

Resultado:
FAILED test_create_task

Exemplo 3 – Alterar código HTTP

No endpoint POST:
Alterar:
return nova_tarefa

Para:
raise HTTPException(status_code=400)

Executar:
pytest

Resultado:
AssertionError
Etapa 10 – Corrigir Problemas

Após identificar os erros:
- Restaurar código original;
- Executar novamente:
pytest

Todos os testes deverão voltar a passar.


Etapa 11 – Versionando Alterações

Verificar alterações:
git status

Adicionar:
git add .

Criar commit:
git commit -m "Implementação dos testes automatizados"

Enviar:
git push


Etapa 12 – Automatizando Testes com GitHub Actions

Criar estrutura:
.github/workflows/python-tests.yml


Etapa 13 – Criando Workflow
Arquivo:
.github/workflows/python-tests.yml

Conteúdo:
name: ControlTask CI

on:
  push:
    branches:
      - main
      - develop

  pull_request:
    branches:
      - main

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

    - name: Baixar código
      uses: actions/checkout@v4

    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest
        pip install pytest-cov
        pip install httpx

    - name: Executar testes
      run: |
        pytest -v


Etapa 14 – Publicando Workflow

Adicionar:
git add .
Commit:
git commit -m "Configuração GitHub Actions"

Enviar:
git push


Etapa 15 – Acompanhar Execução

Acessar:

GitHub
→ Repositório
→ Actions

Será exibido:

ControlTask CI
Simulação 1 – Testes com Sucesso

Todos os testes aprovados:

✓ test_create_task
✓ test_list_tasks
✓ test_update_task
✓ test_delete_task

4 passed

Resultado no GitHub:

✔ Workflow completed successfully


Simulação 2 – Introduzindo Erro

Modificar:
@app.post("/tasks")

Para:
@app.post("/task")

Enviar:
git add .
git commit -m "Erro proposital"
git push

No GitHub Actions:
✖ test_create_task FAILED

Workflow:
X Workflow failed

Explicação:
A Integração Contínua detectou automaticamente a falha.


Simulação 3 – Corrigindo Erro

Restaurar:
@app.post("/tasks")

Executar:
git add .
git commit -m "Correção endpoint"
git push

Resultado:
✔ Workflow completed successfully


Explicações Finais

Durante esta atividade foram aplicados diversos conceitos fundamentais da Engenharia de Software:
- Qualidade de Software
- Garantir que o sistema funcione corretamente.
- Testes Automatizados
- Permitem validar rapidamente se alterações quebraram funcionalidades existentes.
- Integração Contínua (CI)

Executa automaticamente os testes sempre que uma alteração é enviada ao repositório Git e GitHub

Permitem colaboração, rastreabilidade e histórico das modificações.

GitHub Actions: Automatiza tarefas repetitivas e aumenta a confiabilidade do processo de desenvolvimento.

Conclusão

Ao final desta aula, o ControlTask evoluiu de uma aplicação funcional para uma aplicação profissional, preparada para crescer com segurança e qualidade, seguindo práticas amplamente adotadas pelo mercado de desenvolvimento de software.
