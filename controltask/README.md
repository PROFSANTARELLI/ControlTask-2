## Criando Aplicações com Engenharia de Software Orientada à IA

Projeto desenvolvido durante a disciplina prática de Engenharia de Software Orientada à Inteligência Artificial.

O objetivo da disciplina é demonstrar, na prática, como a Inteligência Artificial pode apoiar todas as etapas do ciclo de vida de desenvolvimento de software, desde a concepção da solução até sua publicação.

Ao longo de quatro aulas, será construído uma aplicação web completa chamada **ControlTask**, utilizando Python e ferramentas gratuitas amplamente utilizadas pelo mercado.

---

# Sobre a Disciplina

A disciplina foi concebida para apresentar uma abordagem moderna de desenvolvimento de software, onde a Inteligência Artificial atua como uma parceira na construção de produtos digitais. Mais do que gerar código, a proposta é mostrar como a IA pode auxiliar atividades de:

* Levantamento de requisitos
* Modelagem de sistemas
* Definição de arquitetura
* Construção de banco de dados
* Desenvolvimento de software
* Testes
* Refatoração
* Documentação
* Publicação da aplicação

Durante todo o processo utilizaremos o **Gemini** como assistente de IA para Engenharia de Software.

# Objetivos de Aprendizagem

* Compreender o ciclo de vida do desenvolvimento de software.
* Aplicar conceitos fundamentais de Engenharia de Software.
* Utilizar Inteligência Artificial para apoiar atividades de análise, projeto e implementação.
* Construir aplicações web utilizando Python.
* Desenvolver APIs REST com FastAPI.
* Construir interfaces utilizando Streamlit.
* Utilizar bancos de dados relacionais com SQLite.
* Aplicar versionamento com Git e GitHub.
* Criar testes automatizados.
* Publicar aplicações na nuvem.


# O Projeto ControlTask

O ControlTask é uma aplicação web para gerenciamento de tarefas pessoais.

A aplicação permitirá:

* Cadastro de usuários
* Login
* Cadastro de tarefas
* Consulta de tarefas
* Atualização de tarefas
* Exclusão de tarefas
* Dashboard de acompanhamento

O projeto foi escolhido por permitir a aplicação de diversos conceitos fundamentais de Engenharia de Software em um cenário simples e didático.

# Tecnologias Utilizadas

## Inteligência Artificial

* Gemini

## Linguagem

* Python

## Frontend

* Streamlit

## Backend

* FastAPI

## Banco de Dados

* SQLite
* SQLAlchemy

## Testes

* Pytest

## Documentação

* Markdown
* Mermaid

## Versionamento

* Git
* GitHub

## Deploy

* Streamlit Community Cloud


# Arquitetura da Solução

Usuário
   ↓
Streamlit
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
SQLite

### Frontend

Responsável pela interface do usuário.

### Backend

Responsável pelas regras de negócio e disponibilização da API.

### Banco de Dados

Responsável pela persistência das informações.


# Planejamento das Aulas

## Aula 1 – Descoberta e Planejamento

### Objetivo

Transformar uma ideia em um projeto estruturado.

### Atividades

* Visão do Produto
* Levantamento de Requisitos
* User Stories
* Casos de Uso
* Product Backlog
* Arquitetura da Solução
* Modelo de Dados
* DER
* Criação do Repositório GitHub

### Entregas

* Documento de Requisitos
* User Stories
* Casos de Uso
* Product Backlog
* Arquitetura
* Modelo de Dados
* Diagramas Mermaid


## Aula 2 – Implementação

### Objetivo

Transformar os artefatos da Engenharia de Software em código executável.

### Atividades

* Estruturação do Projeto
* Configuração do Ambiente
* Banco de Dados SQLite
* SQLAlchemy
* API FastAPI
* CRUD de Tarefas
* Interface Streamlit
* Integração Frontend e Backend

### Entregas

* Aplicação funcional local
* CRUD completo
* API documentada
* Código versionado

## Aula 3 – Qualidade de Software

### Objetivo

Garantir qualidade, organização e manutenção da solução.

### Atividades

* Git e GitHub
* Branches
* Commits
* Pull Requests
* Testes Automatizados
* Pytest
* Refatoração Assistida por IA
* Revisão de Código

### Entregas

* Testes automatizados
* Código refatorado
* Boas práticas aplicadas

## Aula 4 – Entrega e Publicação

### Objetivo

Preparar o sistema para disponibilização ao usuário final.

### Atividades

* Revisão Geral
* Ajustes Finais
* Documentação
* README Profissional
* Publicação no Streamlit Community Cloud

### Entregas

* Sistema publicado
* Documentação finalizada
* Projeto concluído

# Estrutura do Projeto

```text
controltask/

├── backend/
├── frontend/
├── tests/
├── docs/
├── diagrams/
├── requirements.txt
├── README.md
└── .gitignore

# Como Executar o Projeto

## Clonar Repositório

git clone <url-do-repositorio>

## Entrar na Pasta

cd controltask

## Criar Ambiente Virtual

python -m venv venv

## Ativar Ambiente

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

## Instalar Dependências

pip install -r requirements.txt

## Executar Backend

uvicorn backend.main:app --reload

## Executar Frontend

streamlit run frontend/app.py


# O Papel da IA Neste Projeto

A Inteligência Artificial não substitui os conceitos de Engenharia de Software.

Ela atua como uma ferramenta de apoio para:

* Análise de requisitos
* Modelagem
* Arquitetura
* Geração de código
* Testes
* Refatoração
* Documentação

O principal objetivo da disciplina é demonstrar como utilizar IA de forma crítica, produtiva e alinhada às boas práticas de desenvolvimento de software.

# Disciplina

**Criando Aplicações com Engenharia de Software Orientada à IA**

Projeto acadêmico desenvolvido para demonstrar, de forma prática, a construção de software moderno utilizando Inteligência Artificial como apoio em todo o ciclo de desenvolvimento.

