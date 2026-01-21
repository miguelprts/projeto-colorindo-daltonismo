# Cronograma Detalhado do Projeto (GPR 8)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data Inicial:** 12/01/2026 | **Data Final Prevista:** 23/01/2026  
**Responsáveis:** Miguel e Clark (Atuação em Par)

## 1. Definição de Sprints e Marcos (Milestones)
O projeto foi dividido em 3 sprints principais, utilizando o esforço total de 40h estimado no GPR 4.

### Sprint 1: Fundação e Dados (12/01 a 14/01)
*Foco: Infraestrutura, Requisitos de Dados e Arquitetura SOLID.*
* **Segunda (12/01):** Setup de infraestrutura (GPR 16), scripts de automação e configuração Git (GCO).
* **Terça (13/01):** Definição de Escopo (GPR 1) e Matriz de Rastreabilidade (GRE).
* **Quarta (14/01):** Implementação do `color_names.csv` (RD01) e Normalização (RD02).
* **Entregável:** Estrutura de pastas e dados bruta.

### Sprint 2: Lógica e Inteligência (15/01 a 19/01)
*Foco: Requisitos Funcionais de Cálculo e Tradução.*
* **Quinta (15/01):** Desenvolvimento da lógica de distância HSL (RF06) e interfaces SOLID.
* **Sexta (16/01):** Implementação da Busca Fuzzy com trava de 95% (RF05, RD05).
* **Segunda (19/01):** Integração com API de Tradução e Cache (RF03, RD03).
* **Entregável:** Backend funcional e API testada via terminal.

### Sprint 3: Interface e Qualidade (20/01 a 23/01)
*Foco: Requisitos de Interface e Auditoria Sonar.*
* **Terça (20/01):** Desenvolvimento das páginas Web responsivas (RI01, RI02, RF08).
* **Quarta (21/01):** Implementação de feedbacks visuais e tratamento de erros (RI03, RI05), e execução de testes unitários (GQA) e análise de cobertura no Sonar (MED).
* **Quinta (22/01):**Encerramento do projeto e consolidação das evidências MPS.Br.
* **Entregável:** Sistema completo e Relatório de Medição.

## 2. Dependências Críticas
1.  **Cálculo HSL (RF06)** depende da **Normalização de Dados (RD02)**.
2.  **Interface Web (RI)** depende do **Gerenciador de Cores (Backend)** estar estável.
3.  **Análise Sonar (MED)** depende da **Suíte de Testes (GQA)** estar concluída.

## 3. Manutenção do Cronograma
Qualidade e prazos são monitorados diariamente. Atrasos superiores a 4h em qualquer requisito geram uma revisão no plano de riscos (GPR 9).