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
