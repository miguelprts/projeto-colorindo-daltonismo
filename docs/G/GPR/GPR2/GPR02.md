# Definição do Modelo de Ciclo de Vida do Projeto (GPR 2)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data de Definição:** 21/01/2026  
**Responsável:** Miguel e Clark

---

## 1. Descrição do Ciclo de Vida
Para este projeto, foi adotado o modelo de **Desenvolvimento Incremental e Iterativo**. Esta escolha justifica-se pela necessidade de garantir a integridade da arquitetura **SOLID** enquanto novas funcionalidades de processamento de dados são adicionadas.

## 2. Fases do Ciclo de Vida
O projeto é dividido nas seguintes fases recorrentes (Iterações):

1.  **Análise e Refinamento:** Revisão do requisito específico (ex: RD05 - Similaridade Fuzzy).
2.  **Design e Arquitetura:** Definição das interfaces e contratos no módulo `app/core/` (Princípio DIP).
3.  **Implementação (Sprint):** Codificação da lógica de negócio e serviços de infraestrutura (Tradução/Pandas).
4.  **Verificação (GQA):** Execução de testes unitários e validação da normalização de dados.
5.  **Integração e Release:** Merge via Pull Request para a branch `main`.

## 3. Compatibilidade com o Projeto
A escolha deste modelo é compatível com o Nível G do MPS.Br por permitir:
* **Complexidade Controlada:** O cálculo de distância HSL foi implementado após a estabilização da estrutura de dados CSV, reduzindo riscos matemáticos.
* **Manutenibilidade:** O foco em SOLID exige revisões constantes, o que é facilitado por ciclos iterativos.
* **Gestão de Mudanças:** Facilita o cumprimento do **GRE 4**, pois cada incremento é isolado em uma branch e validado individualmente.

## 4. Manutenção do Modelo
Este modelo é mantido através da configuração do repositório no GitHub, onde as **Milestones** representam os incrementos do ciclo de vida. Caso a complexidade do projeto aumente (ex: migração de CSV para MariaDB), o ciclo de vida será revisado para incluir fases de migração de dados.

---
**Aprovado por:** Miguel e Clark
**Papel:** Gerentes de Projeto / Desenvolvedores