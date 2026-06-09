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
