4. Requisitos Funcionais (RF)
Gerenciamento de Acesso e Conta
RF-001 (Cadastro): O sistema deve permitir que novos usuários se cadastrem informando Nome, E-mail e Senha.

RF-002 (Autenticação): O sistema deve permitir o login de usuários cadastrados via e-mail/senha e oferecer opção de "Esqueci minha senha".

CRUD de Tarefas
RF-003 (Criar Tarefa): O sistema deve permitir a criação de tarefas contendo: Título, Descrição, Data de Vencimento, Status (Pendente, Em Andamento, Concluída) e Prioridade (Baixa, Média, Alta).

RF-004 (Visualizar/Editar Tarefa): O usuário deve poder alterar qualquer atributo de uma tarefa criada.

RF-005 (Excluir Tarefa): O sistema deve permitir a exclusão lógica de uma tarefa, com confirmação prévia do usuário.

Recursos de Inteligência Artificial
RF-006 (Geração de Descrição via IA): Ao digitar apenas o título da tarefa (ex: "Estudar para a prova de cálculo"), o usuário poderá acionar um botão para que a IA gere uma descrição estruturada com passos recomendados (subtarefas sugeridas).

RF-007 (Sugestão de Prioridade via IA): Com base no título, descrição e data de vencimento, a IA deve analisar o contexto e sugerir automaticamente o nível de prioridade (Alta, Média ou Baixa).

Visualização e Dashboard
RF-008 (Dashboard de Acompanhamento): O sistema deve exibir métricas visuais na tela inicial, incluindo: total de tarefas concluídas/pendentes, gráfico de produtividade semanal e lista de tarefas prioritárias do dia.

5. Requisitos Não Funcionais (RNF)
RNF-001 (Desempenho da IA): As requisições de IA para geração de descrição e prioridade não devem exceder 3 segundos de tempo de resposta para o usuário final.

RNF-002 (Interface/Responsividade): A interface web deve ser 100% responsiva, adaptando-se perfeitamente a dispositivos móveis (smartphones e tablets) e desktops.

RNF-003 (Segurança de Dados): Todas as senhas de usuários devem ser armazenadas utilizando criptografia forte (ex: bcrypt). A comunicação entre o cliente e o servidor deve utilizar protocolo HTTPS.

RNF-004 (Disponibilidade): A aplicação deve ter uma disponibilidade mínima (SLA) de 99.5% do tempo.

RNF-005 (Arquitetura): Integração com o provedor de IA (ex: OpenAI API ou similar) deve ser feita de forma assíncrona ou isolada por uma camada de serviço (Service Layer), garantindo que instabilidades na API externa não derrubem o sistema principal.

6. Regras de Negócio (RN)
RN-001 (Autonomia da Prioridade): A prioridade sugerida pela IA é apenas uma recomendação. O usuário tem a palavra final e pode alterá-la manualmente a qualquer momento.

RN-002 (Limite de Uso de IA): Para evitar abuso de custos com a API de IA, usuários em contas gratuitas terão um limite de 30 requisições de IA (geração de descrição/prioridade) por dia.

RN-003 (Consistência de Datas): Não deve ser permitido criar uma tarefa com data de vencimento retroativa (anterior ao dia atual).

RN-004 (Privacidade de Dados): Dados pessoais sensíveis informados nas tarefas não devem ser utilizados para retreinamento público de modelos de IA de terceiros (deve-se optar por políticas de API que garantam a privacidade dos dados enviados).

7. Premissas
Os usuários finais possuem acesso estável à internet para utilizar a aplicação web e disparar os recursos de IA.

Haverá disponibilidade de crédito e orçamento para o consumo de APIs de Large Language Models (LLMs) durante a fase de desenvolvimento e validação do MVP.

A equipe de desenvolvimento possui maturidade para integrar APIs Rest e manipular estados assíncronos no Front-end (indicadores de loading enquanto a IA processa).

8. Restrições
Orçamentária: O custo mensal com a infraestrutura de IA e Cloud não pode ultrapassar o teto estipulado para a fase de validação do MVP.

Tecnológica: O sistema deve ser desenvolvido utilizando tecnologias web padrão de mercado (ex: React/Next.js no Front-end e Node.js/Python no Back-end) para facilitar a manutenção e contratação de novos desenvolvedores.

Legal: O produto deve estar em estrita conformidade com a LGPD (Lei Geral de Proteção de Dados), garantindo a opção de exclusão definitiva da conta e dos dados do usuário.

9. Critérios de Sucesso
O projeto ControlTask será considerado bem-sucedido se, após 3 meses do lançamento em produção, atingir os seguintes marcos:

Estabilidade Técnica: Menos de 1% de erros de timeout ou falhas de integração com a API de IA reportados pelos usuários.

Engajamento da IA: Mais de 60% dos usuários ativos utilizando a funcionalidade de geração de descrição automática pelo menos 3 vezes por semana.

Aprovação do Usuário: Obter uma nota de satisfação (NPS ou avaliação interna) superior a 75 pontos no quesito "facilidade de uso e economia de tempo".
