Abaixo está o desenho arquitetural do ControlTask, projetado para garantir modularidade, separação de conceitos (Separation of Concerns) e facilidade de manutenção.

1. Arquitetura em Camadas e Componentes
Adotaremos uma Arquitetura Baseada em Serviços e Camadas, separando fisicamente o Frontend (Client-side em Streamlit) do Backend (Server-side em FastAPI). O Backend, por sua vez, é segmentado logicamente para isolar as rotas, as regras de negócio, a camada de dados e as integrações externas.

Snippet de código
graph TD
    subgraph Client [Camada de Apresentação - Frontend]
        ST[Streamlit App] --> Views[Views / Telas]
        Views --> ClientAPI[Client API / Requests]
    end

    subgraph Server [Camada de Aplicação - Backend FastAPI]
        ClientAPI --> |HTTP / JSON| Routers[Routers / Endpoints]
        
        subgraph Camada de Negócio
            Routers --> Controllers[Controllers / Services]
            Controllers --> IAService[Gemini IA Service]
        end

        subgraph Camada de Persistência
            Controllers --> Repositories[Repositories / Camada de Acesso a Dados]
            Repositories --> Models[SQLAlchemy Models]
            Models --> DB[(SQLite Database)]
        end
    end

    subgraph External [Serviços Externos]
        IAService --> |Google GenAI SDK| Gemini[Google AI Studio / Gemini]
    end

    style ST fill:#FF4B4B,stroke:#333,stroke-width:2px,color:#fff
    style Routers fill:#059669,stroke:#333,stroke-width:2px,color:#fff
    style DB fill:#1E3A8A,stroke:#333,stroke-width:2px,color:#fff
    style Gemini fill:#4285F4,stroke:#333,stroke-width:2px,color:#fff
2. Responsabilidades de Cada Camada
Camada de Apresentação (Frontend - Streamlit)
Views: Renderiza os componentes visuais (inputs, botões, tabelas, dashboards). Gerencia o estado da sessão local do usuário (st.session_state), como o token de autenticação.

Client API: Camada de serviço interna do frontend (utilizando a biblioteca requests). Nenhuma query ou lógica de banco de dados acontece aqui; o frontend apenas consome o backend via requisições HTTP REST.

Camada de Transporte/Entrada (Backend - FastAPI Routers)
Routers: Define as rotas/endpoints da API (ex: /tasks, /auth/login). É responsável pela validação dos dados de entrada e saída utilizando Pydantic Schemas (garantindo tipagem estrita e documentação automática via Swagger).

Camada de Negócio (Services / Controllers)
Services: Centraliza as Regras de Negócio do ControlTask (ex: verificar limite diário de uso de IA, impedir tarefas retroativas). É o cérebro da aplicação.

Gemini IA Service: Componente isolado dentro da camada de negócio responsável por interagir com o SDK do Google AI Studio. Ele constrói os prompts, configura a temperatura do modelo Gemini e trata possíveis falhas de integração sem afetar o fluxo principal do banco de dados.

Camada de Persistência (Repositories & ORM)
Repositories: Implementa o padrão Repository Pattern. Isola as consultas SQL e interações diretas do SQLAlchemy do restante da aplicação. Se no futuro o banco mudar de SQLite para PostgreSQL, apenas os repositórios serão alterados.

SQLAlchemy Models: Mapeamento objeto-relacional das tabelas do banco de dados SQLite.

3. Fluxo de Comunicação (Exemplo: Criar Tarefa com IA)
O diagrama de sequência abaixo ilustra o fluxo assíncrono e síncrono de comunicação entre os componentes quando o usuário solicita a criação de uma tarefa utilizando a Inteligência Artificial.

Snippet de código
sequenceDiagram
    autonumber
    actor Usuario as Usuário
    participant ST as Streamlit (View)
    participant API as FastAPI (Router)
    participant SVC as Task Service
    participant IA as Gemini Service
    participant REPO as Task Repository
    participant DB as SQLite

    Usuario->>ST: Digita título e clica em "Gerar com IA"
    ST->>API: POST /tasks/generate-ai (Payload)
    API->>SVC: generate_task_context(title)
    
    critical Integração com Google AI Studio
        SVC->>IA: request_description_and_priority(title)
        IA->>IA: Processa Prompt (Contexto)
        IA-->>SVC: Retorna Descrição e Prioridade Sugerida
    end

    SVC->>REPO: save_task(task_data)
    REPO->>DB: INSERT INTO tasks...
    DB-->>REPO: Confirmado (ID gerado)
    REPO-->>SVC: Objeto Task
    SVC-->>API: Pydantic Schema (TaskOut)
    API-->>ST: HTTP 201 Created (JSON)
    ST-->>Usuario: Renderiza a tarefa gerada no Dashboard
4. Estrutura de Diretórios do Projeto
Para garantir um repositório limpo no GitHub e facilitar o trabalho em equipe, utilizaremos uma estrutura de monorepo dividida entre frontend e backend, permitindo deploy isolado de ambos se necessário.

Plaintext
controltask/
│
├── .github/
│   └── workflows/            # Pipelines de CI/CD (Testes e Linter)
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/# Rotas (auth.py, tasks.py, dashboard.py)
│   │   │   │   └── api.py    # Agrupador de rotas (APIRouter)
│   │   ├── core/
│   │   │   ├── config.py     # Configurações globais (Pydantic Settings para .env)
│   │   │   └── security.py   # Utilitários de Hash (bcrypt) e JWT
│   │   ├── db/
│   │   │   ├── base.py       # Inicialização do SQLAlchemy (SessionLocal, Base)
│   │   │   └── models/       # Modelos do Banco (user.py, task.py)
│   │   ├── repositories/     # Consultas ao banco (user_repo.py, task_repo.py)
│   │   ├── schemas/          # Validação Pydantic (user_schema.py, task_schema.py)
│   │   └── services/         # Regras de Negócio e IA (task_service.py, gemini_service.py)
│   │   └── main.py           # Arquivo de inicialização do FastAPI
│   ├── tests/                # Testes automatizados (Pytest)
│   ├── .env.example          # Modelo de variáveis de ambiente do backend
│   └── requirements.txt      # Dependências do backend (fastapi, sqlalchemy, google-generativeai)
│
├── frontend/
│   ├── app.py                # Ponto de entrada principal do Streamlit
│   ├── core/
│   │   └── api_client.py     # Centralizador de requisições HTTP (requests)
│   ├── views/
│   │   ├── login.py          # Tela de Autenticação
│   │   ├── dashboard.py      # Tela de Métricas
│   │   └── tasks.py          # Tela de Gerenciamento de tarefas
│   ├── .env.example          # Modelo de variáveis de ambiente do frontend
│   └── requirements.txt      # Dependências do frontend (streamlit, requests)
│
├── .gitignore                # Regras de exclusão do Git (ignorar .env, .db, __pycache__)
└── README.md                 # Documentação de setup do projeto
5. Boas Práticas de Organização e Governança
Segurança e Segregação de Segredos: Nunca comitar arquivos .env ou o arquivo de banco local (controltask.db). As chaves da API do Google AI Studio (GEMINI_API_KEY) e a SECRET_KEY do JWT devem ser injetadas via variáveis de ambiente. O .gitignore deve estar configurado estritamente desde o primeiro commit.

Gerenciamento de Sessão no SQLite: Como o SQLite não lida nativamente de forma robusta com concorrência pesada de gravação, utilizaremos o Context Manager (yield) no FastAPI para garantir que cada requisição abra e feche sua conexão (db_session) imediatamente após o uso, evitando travamentos de banco (Database Locked).

Abstração de Dependências (Dependecy Injection): Utilizar intensamente o sistema do Depends() do FastAPI para injetar sessões de banco de dados e serviços nos endpoints, facilitando a criação de mocks em testes unitários.

Padrão de Git Branching: Adotar o padrão de ramificação baseado em Feature Branches. Ninguém commita direto na main. Cada User Story (ex: US-007) vira uma branch feature/US-007-descricao-ia, exigindo um Pull Request (PR) revisado antes de integrar à branch principal.
