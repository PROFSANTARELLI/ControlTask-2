1. Dicionário de Dados (Entidades, Atributos e Chaves)
Entidade: users (Usuários)
Responsável por armazenar as credenciais e informações de perfil dos utilizadores.

id (PK): INTEGER — Chave primária com autoincremento.

name: VARCHAR(100) — Nome completo do usuário. Não nulo.

email: VARCHAR(150) — E-mail utilizado para login. Único e não nulo.

password_hash: VARCHAR(255) — Senha criptografada (padrão bcrypt). Não nulo.

created_at: TIMESTAMP — Data e hora de criação da conta. Padrão CURRENT_TIMESTAMP.

Entidade: tasks (Tarefas)
Responsável por armazenar as tarefas de cada usuário, suportando a exclusão lógica.

id (PK): INTEGER — Chave primária com autoincremento.

user_id (FK): INTEGER — Referencia users(id). Não nulo.

title: VARCHAR(100) — Título da tarefa. Não nulo.

description: TEXT — Descrição detalhada ou subtarefas geradas. Opcional (Pode ser nulo).

due_date: DATE — Data de vencimento da tarefa. Não nulo.

status: VARCHAR(20) — Estados possíveis: 'PENDING', 'IN_PROGRESS', 'COMPLETED'. Não nulo. Padrão 'PENDING'.

priority: VARCHAR(10) — Níveis: 'LOW', 'MEDIUM', 'HIGH'. Não nulo.

is_ai_prioritized: BOOLEAN — Flag que indica se a prioridade atual veio da IA. Não nulo. Padrão FALSE.

is_deleted: BOOLEAN — Flag para exclusão lógica. Não nulo. Padrão FALSE (tarefa ativa).

created_at: TIMESTAMP — Data e hora de criação. Padrão CURRENT_TIMESTAMP.

updated_at: TIMESTAMP — Data e hora da última alteração. Padrão CURRENT_TIMESTAMP.

Entidade: ai_usage_logs (Histórico de Utilização da IA)
Responsável por auditar o uso dos recursos de IA e validar a regra de negócio de limite diário (rate limit).

id (PK): INTEGER — Chave primária com autoincremento.

user_id (FK): INTEGER — Referencia users(id). Não nulo.

feature_used: VARCHAR(30) — Tipo de recurso: 'GENERATE_DESCRIPTION' ou 'SUGGEST_PRIORITY'. Não nulo.

prompt_tokens_estimated: INTEGER — Métrica interna opcional para estimativa de custo.

created_at: DATE — Data de utilização (armazenada como DATE ou TIMESTAMP para agrupamento diário). Padrão CURRENT_TIMESTAMP.

2. Relacionamentos e Regras de Integridade
Relacionamentos
users para tasks (1:N): Um usuário pode ter muitas tarefas. Uma tarefa pertence obrigatoriamente a um único usuário.

Regra de remoção: Se um usuário for excluído fisicamente, todas as suas tarefas serão excluídas em cascata (ON DELETE CASCADE).

users para ai_usage_logs (1:N): Um usuário pode gerar muitos logs de uso da IA. Um log pertence a um único usuário.

Regra de remoção: Exclusão em cascata (ON DELETE CASCADE).

Regras de Integridade e Restrições (Constraints)
Integridade de Chave Única: O campo email na tabela users possui uma restrição UNIQUE, impedindo cadastros duplicados.

Integridade de Domínio (Check Constraints):

tasks.status só aceita os valores: 'PENDING', 'IN_PROGRESS', 'COMPLETED'.

tasks.priority só aceita os valores: 'LOW', 'MEDIUM', 'HIGH'.

ai_usage_logs.feature_used só aceita: 'GENERATE_DESCRIPTION', 'SUGGEST_PRIORITY'.

Exclusão Lógica: O sistema não executará comandos DELETE na tabela tasks. Em vez disso, fará um UPDATE tasks SET is_deleted = TRUE. As listagens comuns e os gráficos do Dashboard devem sempre filtrar por WHERE is_deleted = FALSE.


4. DER Textual (Mapeamento de Chaves)
USERS(id, name, email, password_hash, created_at)

TASKS(id, user_id, title, description, due_date, status, priority, is_ai_prioritized, is_deleted, created_at, updated_at)

user_id referencia USERS(id)

AI_USAGE_LOGS(id, user_id, feature_used, prompt_tokens_estimated, created_at)

user_id referencia USERS(id)

5. Script SQL de Criação (Compatível com SQLite)
Este script cria as tabelas aplicando todas as restrições de integridade, seguidas pela criação de índices estratégicos para garantir a performance da aplicação.

SQL
-- Habilitar suporte a Chaves Estrangeiras no SQLite (necessário executar por conexão)
PRAGMA foreign_keys = ON;

-- 1. Criação da Tabela de Usuários
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Criação da Tabela de Tarefas
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    priority VARCHAR(10) NOT NULL,
    is_ai_prioritized BOOLEAN NOT NULL DEFAULT 0, -- 0 = False, 1 = True (SQLite usa inteiros para booleanos)
    is_deleted BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT chk_status CHECK (status IN ('PENDING', 'IN_PROGRESS', 'COMPLETED')),
    CONSTRAINT chk_priority CHECK (priority IN ('LOW', 'MEDIUM', 'HIGH'))
);

-- 3. Criação da Tabela de Histórico/Logs da IA
CREATE TABLE ai_usage_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    feature_used VARCHAR(30) NOT NULL,
    prompt_tokens_estimated INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT chk_feature CHECK (feature_used IN ('GENERATE_DESCRIPTION', 'SUGGEST_PRIORITY'))
);

-- =========================================================================
-- Otimização: Criação de Índices (Crucial para performance)
-- =========================================================================

-- Otimiza a busca e filtros de tarefas do usuário ativo ignorando itens deletados (Usado no Dashboard e Listas)
CREATE INDEX idx_tasks_user_active ON tasks (user_id, is_deleted, due_date);

-- Otimiza a query de verificação do Rate Limit diário de IA (Conta quantos logs o usuário gerou no dia atual)
CREATE INDEX idx_ai_logs_user_date ON ai_usage_logs (user_id, created_at);
Justificativa dos Índices Criados:
idx_tasks_user_active: O Streamlit e o Dashboard vão consultar as tarefas ativas do usuário a todo momento. Esse índice composto garante que o SQLite encontre diretamente as tarefas do user_id onde is_deleted = 0 ordenadas por data, sem precisar escanear a tabela inteira (Full Table Scan).

idx_ai_logs_user_date: Toda vez que o usuário clicar em um botão de IA, o Backend executará uma query de contagem (COUNT) para validar a regra de negócio dos 30 usos diários. Esse índice torna a verificação instantânea.
