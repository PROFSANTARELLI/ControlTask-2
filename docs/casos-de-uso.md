Snippet de código
@startuml
skinparam packageStyle rectangle
skinparam actorStyle awesome

title ControlTask - Diagrama de Casos de Uso (UML)

left to right direction

actor "Usuário" as user
actor "Provedor de IA" as ia << Sistema Externo >>

rectangle "Sistema ControlTask" {
    usecase "UC-001: Manter Conta de Usuário" as uc_conta
    usecase "UC-002: Autenticar Usuário" as uc_login
    usecase "UC-003: Criar Tarefa Manualmente" as uc_criar
    usecase "UC-004: Editar Tarefa" as uc_editar
    usecase "UC-005: Excluir Tarefa" as uc_excluir
    usecase "UC-006: Visualizar Dashboard" as uc_dash
    
    usecase "UC-007: Solicitar Geração de Descrição via IA" as uc_ia_desc
    usecase "UC-008: Solicitar Sugestão de Prioridade via IA" as uc_ia_prio
}

' Associações dos Atores com os Casos de Uso Principais
user --> uc_conta
user --> uc_login
user --> uc_criar
user --> uc_editar
user --> uc_excluir
user --> uc_dash

' Relacionamentos de Extensão (IA é opcional ao criar ou editar)
uc_ia_desc .--> uc_criar : <<extend>>
uc_ia_desc .--> uc_editar : <<extend>>

uc_ia_prio .--> uc_criar : <<extend>>
uc_ia_prio .--> uc_editar : <<extend>>

' Interação com o Sistema Externo de IA
uc_ia_desc --> ia
uc_ia_prio --> ia

@enduml
