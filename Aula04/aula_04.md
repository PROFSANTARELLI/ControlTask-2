Aula 4 - Entrega, Publicação e Evolução do ControlTask - Engenharia de Software Orientada à IA

Objetivos: Nesta última aula iremos concluir o projeto **ControlTask**, realizando atividades típicas do encerramento de um projeto de software profissional.

Ao final da aula você será capaz de:
* Revisar tecnicamente uma aplicação completa;
* Refatorar código utilizando Inteligência Artificial;
* Produzir documentação profissional;
* Publicar aplicações na nuvem;
* Realizar demonstrações técnicas;
* Compreender o papel da IA na Engenharia de Software moderna.

# Cenário
Durante as aulas anteriores realizamos:

## Aula 1
Planejamento do sistema. Produzimos:

* Documento de requisitos;
* User Stories;
* Casos de Uso;
* Backlog;
* Arquitetura;
* Modelo de Dados.

---

## Aula 2
Implementação do sistema. Produzimos:

* Backend FastAPI;
* Frontend Streamlit;
* Banco SQLite;
* Integração completa.

---

## Aula 3
Garantia da qualidade. Produzimos:

* Testes automatizados;
* Integração contínua;
* Revisão de código;
* Refatoração.

---

# Objetivo da Aula 4
Transformar o ControlTask em um produto pronto para ser entregue.

---

# Fluxo Geral da Aula

Revisão Técnica
        ↓
Refatoração Final
        ↓
Documentação
        ↓
Publicação na Nuvem
        ↓
Validação Final
        ↓
Apresentação Técnica
```

---

# Etapa 1 - Atualizando o Projeto Local

Antes de iniciar qualquer atividade devemos garantir que todos estão utilizando a versão mais recente do sistema.

Abra o terminal do VS Code.

Atualize o repositório:
git pull

Verifique se existem alterações pendentes:
git status

Resultado esperado:
```
On branch main
nothing to commit, working tree clean
```

Explicação:
O comando `git pull` sincroniza o projeto local com o repositório remoto.
O comando `git status` informa o estado atual do projeto.

---

# Etapa 2 - Revisão Técnica da Estrutura do Projeto
Analisar toda a estrutura construída.

Estrutura esperada:
controltask/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│
├── frontend/
│   └── app.py
│
├── tests/
│
├── docs/
│
├── .github/
│   └── workflows/
│
├── requirements.txt
├── README.md
└── .gitignore
```

Objetivos desta revisão:
* Identificar arquivos desnecessários;
* Confirmar organização das pastas;
* Garantir separação de responsabilidades.

Perguntas para discussão:
* O frontend está isolado do backend?
* A API está desacoplada da interface?
* O banco está separado da lógica de negócio?

---
# Etapa 3 - Revisão Arquitetural Assistida por IA

Ferramenta:
**Gemini**

Prompt sugerido:
Atue como Arquiteto de Software Sênior. Analise toda a estrutura do projeto ControlTask. Considere:
- Arquitetura do projeto;
- Organização de pastas;
- Boas práticas Python;
- Reutilização de código;
- Legibilidade;
- Escalabilidade;
- Segurança.

Classifique as melhorias em:
Alta prioridade;
Média prioridade;
Baixa prioridade.

Explique cada melhoria.
```

Objetivo:
Demonstrar que a IA pode atuar como revisora técnica.
---

# Etapa 4 - Refatoração Final
Após receber as sugestões do Gemini, aplicar pequenas melhorias.


## Remover código duplicado

Verificar:

* Funções repetidas;
* Trechos similares;
* Importações desnecessárias.

---

# Etapa 5 - Executando Testes Finais

Executar:
pytest
```

Resultado esperado:

```text
====================

5 passed

====================
```

Caso existam falhas:

Corrigir antes da publicação.

Explicação:

Nunca devemos publicar software sem executar testes finais.

---

# Etapa 6 - Revisando o GitHub Actions

Abrir:

```text
GitHub → Actions
```

Verificar:

* Última execução;
* Status dos testes;
* Histórico de execuções.

Resultado esperado:

```text
✔ Workflow completed successfully
```

Objetivo:

Garantir que o projeto continua íntegro.

---

# Etapa 7 - Produzindo Documentação Profissional

Abrir:

```text
README.md
```

O README deve conter:

## Descrição do projeto

O que é o ControlTask?

---

## Tecnologias utilizadas

Exemplo:

* Python
* FastAPI
* Streamlit
* SQLite
* SQLAlchemy
* Pytest
* GitHub Actions

---

## Arquitetura

Exemplo:
Usuário
   ↓
Streamlit
   ↓
FastAPI
   ↓
SQLite

---

## Como executar

Exemplo:
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run frontend/app.py
---

## Como executar testes

pytest

---

## Capturas de tela

Adicionar imagens:
* Tela principal;
* Swagger;
* GitHub Actions.

## Autor
Inserir informações dos desenvolvedores.

# Etapa 8 - Gerando Evidências do Projeto

Registrar evidências para documentação.

Sugestões:

## Captura da Interface

Executar:

streamlit run frontend/app.py

Capturar:

* Tela principal.

## Captura da API

Abrir:
http://localhost:8000/docs

Capturar:
* Endpoints disponíveis.
---
## Captura dos Testes

Executar:
pytest -v

Capturar:
Resultado dos testes.
---

## Captura do GitHub Actions

Capturar:
Workflow completed successfully
---

# Etapa 9 - Preparando o Deploy

Antes da publicação verificar:

## Arquivo requirements.txt

Atualizar:
pip freeze > requirements.txt

Explicação:
O arquivo contém todas as dependências necessárias para execução na nuvem.
---

## Commit Final

Adicionar alterações:
git add .

Criar commit:
git commit -m "Versão final do ControlTask"

Enviar:
git push

---

# Etapa 10 - Publicando no Streamlit Community Cloud

Acessar:

https://share.streamlit.io/

Realizar login utilizando GitHub.

Selecionar:

Repository:
controltask-2

Selecionar:
Branch:
main

Arquivo principal:
frontend/app.py

Clique em:
Deploy

Aguardar publicação.

# Etapa 11 - Validando o Deploy

Após a publicação:

Acessar a URL pública.

Executar:

* Cadastro de tarefas;
* Consulta;
* Atualização;
* Exclusão.

Validar:

* Interface funcionando;
* API respondendo corretamente;
* Persistência de dados.

---

# Etapa 12 - Apresentação Técnica do Projeto

# Reflexão Final

Responder:

## Como a Inteligência Artificial impactou o desenvolvimento deste projeto?

## Quais atividades a IA executou melhor?

## Quais atividades exigiram maior supervisão humana?

## Como você imagina o futuro da Engenharia de Software orientada à IA?

---

# Conclusão

Ao longo das quatro aulas percorremos todo o ciclo de vida de desenvolvimento de software:

Ideia
 ↓
Requisitos
 ↓
Projeto
 ↓
Implementação
 ↓
Testes
 ↓
Automação
 ↓
Deploy
 ↓
Entrega
```

O projeto ControlTask demonstrou que a Engenharia de Software continua sendo essencial.

A Inteligência Artificial não substitui o engenheiro de software.

Ela potencializa sua capacidade de construir soluções de maior qualidade, em menos tempo e com maior produtividade.

# Parabéns!

Você concluiu a construção de uma aplicação completa utilizando Engenharia de Software Orientada à IA.
