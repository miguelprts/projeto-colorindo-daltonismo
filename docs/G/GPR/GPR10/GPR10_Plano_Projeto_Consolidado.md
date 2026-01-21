# Plano de Projeto Consolidado (GPR 10)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data da Versão:** 21/01/2026  
**Responsáveis:** Miguel e Clark  
**Status:** Aprovado e em Execução

---

## 1. Visão Geral e Escopo (GPR 1)
O projeto visa a identificação e conversão cromática com rigor de 95% de similaridade, utilizando arquitetura SOLID e FastAPI. Estão mapeados 23 requisitos (8 RF, 5 RNF, 5 RD e 5 RI).

## 2. Abordagem de Desenvolvimento (GPR 2)
Adotado o ciclo de vida **Incremental e Iterativo**, com entregas divididas em 3 Sprints (Fundação, Lógica e Interface).

## 3. Estimativas e Recursos (GPR 3, 4 e 5)
* **Esforço Total:** 40 horas-homem.
* **Complexidade:** Alta para os módulos de distância HSL e Tradução.
* **Equipe:** Miguel (Líder/Dev) e Clark (Líder/Dev) com responsabilidades compartilhadas via Matriz RACI (GPR 7).
* **Infraestrutura:** Servidor Debian, MariaDB, Python 3.14.2 e SonarQube.

## 4. Planejamento Financeiro (GPR 6)
Orçamento total de **R$ 2.200,00**, incluindo 10% de reserva de contingência para mitigação de riscos.

## 5. Cronograma e Marcos (GPR 8)
* **Início:** 12/01/2026.
* **Marco de Lógica (M1):** 19/01/2026 (Backend Completo).
* **Marco de Encerramento (M2):** 23/01/2026 (Sistema e Auditoria).

## 6. Gestão de Riscos (GPR 9)
Foco na mitigação de latência de API (Cache) e imprecisão de dados (Trava de 95% e Normalização Pandas).

## 7. Mecanismos de Controle e Qualidade (GPR 11, 12 e MED)
* **Monitoramento:** Via Issues e Pull Requests no GitHub.
* **Métrica de Sucesso:** Cobertura de testes unitários > 80% reportada no SonarQube.
* **Rastreabilidade:** Mantida pela Matriz de Rastreabilidade (GRE 3) vinculando código a requisitos.

---

### 8. Aprovação das Partes Interessadas
Ao dar continuidade ao projeto, os responsáveis declaram estar de acordo com este plano.

**Assinado eletronicamente por:**
* Miguel - Líder de Projeto
* Clark - Líder de Projeto