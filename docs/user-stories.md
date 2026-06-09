Documento de Especificação e Backlog
- ControlTask
Autor: Analista de Requisitos Sênior & Product Owner
Versão: 1.0 (MVP)
Status: Aprovado para Desenvolvimento

1. Visão do Produto
O ControlTask é um sistema web de gerenciamento de tarefas pessoais que transforma a
produtividade individual por meio da Inteligência Artificial. Diferente dos gerenciadores
tradicionais, que exigem preenchimento manual exaustivo, o ControlTask atua como um
assistente ativo. Ele reduz a sobrecarga cognitiva do usuário ao automatizar a criação de
descrições detalhadas e ao sugerir prioridades dinâmicas com base no contexto, permitindo
que o usuário foque no que realmente importa: a execução.
2. Objetivos de Negócio
● Retenção de Usuários: Alcançar uma taxa de engajamento semanal (WAU) de pelo
menos 40% nos primeiros seis meses.
● Eficiência de Cadastro: Reduzir em 60% o tempo gasto pelo usuário na criação e
detalhamento de uma tarefa complexa utilizando os recursos de IA.
● Conversão de IA: Garantir que 70% das sugestões de prioridade geradas pela IA sejam
aceitas ou mantidas pelos usuários sem alteração manual.
3. Perfis de Usuário (Personas)
● Lucas (32 anos) - O Profissional Sobrecarregado: Gerente de projetos que lida com
dezenas de microtarefas diárias. Precisa esvaziar a mente rápido. Utiliza a IA para ditar
ou digitar uma frase curta e espera que o sistema organize o resto.
● Beatriz (21 anos) - A Estudante Autônoma: Estudante universitária e estagiária.
Precisa de ajuda para priorizar o que é urgente versus o que é importante. Depende do
Dashboard e das sugestões de prioridade da IA para saber exatamente o que executar.
4. Requisitos do Sistema
Requisitos Funcionais (RF)
● RF-001 (Cadastro): O sistema deve permitir que novos usuários se cadastrem
informando Nome, E-mail e Senha.
● RF-002 (Autenticação): O sistema deve permitir o login de usuários cadastrados via
e-mail/senha.

● RF-003 (Criar Tarefa): O sistema deve permitir a criação de tarefas contendo: Título,
Descrição, Data de Vencimento, Status e Prioridade.
● RF-004 (Visualizar/Editar Tarefa): O usuário deve poder alterar qualquer atributo de
uma tarefa criada.
● RF-005 (Excluir Tarefa): O sistema deve permitir a exclusão lógica de uma tarefa, com
confirmação prévia.
● RF-006 (Geração de Descrição via IA): A partir do título, a IA deve gerar uma descrição
estruturada com passos recomendados.
● RF-007 (Sugestão de Prioridade via IA): Com base no título, descrição e data de
vencimento, a IA deve sugerir o nível de prioridade.
● RF-008 (Dashboard): O sistema deve exibir métricas visuais na tela inicial (tarefas
concluídas, pendentes e focos do dia).
Requisitos Não Funcionais (RNF)
● RNF-001 (Desempenho da IA): O tempo de resposta para a geração de IA não deve
exceder 3 segundos.
● RNF-002 (Interface): A interface web deve ser 100% responsiva (Mobile e Desktop).
● RNF-003 (Segurança): Senhas criptografadas com bcrypt e comunicação integral via
HTTPS.
● RNF-004 (Disponibilidade): SLA mínimo de 99.5%.
5. Regras de Negócio, Premissas e Restrições
● RN-001: A prioridade sugerida pela IA é apenas uma recomendação; o usuário pode
alterá-la manualmente.
● RN-002: Limite de 30 requisições de IA gratuitas por usuário/dia para controle de custos
de API.
● RN-003: Não é permitido salvar tarefas com data de vencimento retroativa.
● Restrição: Conformidade estrita com a LGPD para exclusão definitiva de dados a pedido
do usuário.
6. Product Backlog (User Stories)
Abaixo encontra-se a especificação ágil das histórias de usuário prontas para o planejamento
das Sprints.
ID Título História de
Usuário

Critérios de
Aceitação

Prioridade

US-001 Cadastro de
Conta

Como novo
usuário,
Quero me
cadastrar com
e-mail e senha,
Para ter um
espaço exclusivo
e seguro.

• Validação de
formato de e-mail.
• Senha mínima
de 8 caracteres (1
letra, 1 número).
• Criptografia hash
de senha.
• Redirecionar ao
Dashboard após
Alta

ID Título História de
Usuário

Critérios de
Aceitação

Prioridade

sucesso.

US-002 Autenticação Como usuário
cadastrado,
Quero realizar
login,
Para acessar
minhas tarefas
com segurança.

• Bloquear
acessos com
credenciais
incorretas.
• Mensagem de
erro genérica por
segurança.
• Link para
recuperação de
senha disponível.
Alta

US-003 Criação de
Tarefas

Como usuário
focado,
Quero criar uma
tarefa
manualmente,
Para organizar
meus
compromissos.

• Título obrigatório
(máx. 100
caracteres).
• Bloquear data
retroativa.
• Status inicial
padrão:
"Pendente".
• Exibir notificação
de sucesso.

Alta

US-004 Gestão de Status Como usuário
dinâmico,
Quero editar
tarefas e status,
Para manter meu
progresso
atualizado.

• Pré-preencher
campos na
edição.
• Seletor visual
simples para os
status.
• Atualização
imediata em base
de dados.

Alta

US-005 Exclusão Lógica Como usuário
organizado,
Quero excluir
tarefas obsoletas,
Para limpar minha
lista de foco.

• Exibir modal de
confirmação antes
de deletar.
• Exclusão lógica
(preservar
métricas no
histórico).

Média

US-006 Dashboard Como usuário
focado,
Quero visualizar
gráficos de
desempenho,
Para entender
minha
produtividade.

• Totalizadores de
Pendentes vs
Concluídas.
• Lista visível dos
focos do dia atual.
• Atualização
reativa de
componentes.
Alta

ID Título História de
Usuário

Critérios de
Aceitação

Prioridade

US-007 Descrição por IA Como usuário
com pressa,
Quero que a IA
gere a descrição,
Para poupar
tempo de
planejamento.

• Botão "Gerar
com IA" ao lado
do campo.
• Exibir loader
durante a
requisição.
• Tempo limite de
resposta de 3
segundos.
• Permitir edição
do texto gerado.
Média

US-008 Prioridade por IA Como usuário
sobrecarregado,
Quero sugestão
de prioridade via
IA,
Para focar no que
é mais crítico.

• Análise
contextual de
título e data.
• Exibir tag
identificadora
"Sugerido por IA".
• Remover tag se
o usuário alterar
manualmente.

Média

US-009 Rate Limit IA Como
Administrador,
Quero limitar o
uso diário da IA,
Para controlar
custos de API.

• Travar recursos
de IA após 30
requisições
diárias.
• Exibir
mensagem
amigável de limite
atingido.

Baixa

7. Critérios de Sucesso
1. Estabilidade Técnica: Menos de 1% de falhas ou timeout nas integrações de IA.
2. Adoção do Recurso: Mais de 60% dos utilizadores ativos a usar as funcionalidades de
IA semanalmente.
3. Satisfação (NPS): Nota superior a 75 pontos na percepção de economia de tempo.
