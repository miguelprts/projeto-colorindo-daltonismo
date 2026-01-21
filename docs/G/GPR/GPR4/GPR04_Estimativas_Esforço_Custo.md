# Planejamento de Esforço e Custos (GPR 4)
**Projeto:** Colorindo o Daltonismo
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark

## 1. Metodologia de Estimativa de Esforço
As estimativas foram baseadas no julgamento técnico dos desenvolvedores, considerando a produtividade média em ambiente Python/FastAPI e a necessidade de implementação de testes unitários para cada requisito.

## 2. Estimativa de Esforço por Módulo (Fase de Planejamento)
O esforço total foi distribuído entre os 23 requisitos, agrupados por categorias de entrega:

| Categoria | Requisitos Relacionados | Esforço Estimado (Horas) | Justificativa |
| :--- | :--- | :--- | :--- |
| **Arquitetura & Setup** | RNF01, RNF03, GPR16, RD01 | 6h | Definição da estrutura SOLID e automação de pastas. |
| **Núcleo Matemático** | RF06, RD02 | 8h | Implementação e validação da distância HSL. |
| **Dados e Tradução** | RF03, RF04, RF05, RD03, RD05 | 10h | Integração com API, Cache e busca Fuzzy 95%. |
| **Interface & UX** | RI01 - RI05, RF08 | 6h | Desenvolvimento Web responsivo e feedbacks. |
| **Qualidade & Docs** | RNF05, GRE2, GPR1, MED | 10h | Documentação MPS.Br, Testes Unitários e Sonar. |
| **TOTAL ESTIMADO** | | **40h** | 1 semana de trabalho para 1 desenvolvedor. |

## 3. Estimativa de Custos (Custo de Oportunidade)
Considerando o caráter acadêmico, o custo financeiro direto é zero. No entanto, para fins de simulação de nível G, estabelece-se o custo baseado na hora/homem:
* **Valor da Hora:** R$ 50,00 (Simulação Júnior)
* **Custo Total Estimado:** R$ 2.000,00
* **Recursos de Aquisição (RAP):** Uso de ferramentas Open Source (0,00).

## 4. Monitoramento e Manutenção do Esforço
O esforço real foi monitorado via **Log de Commits**. Observou-se que o esforço de "Qualidade & Docs" superou a estimativa inicial devido ao rigor exigido para a integração do SonarQube com a cobertura XML.

---
**Aprovado por:** Miguel e Clark
**Data da Última Revisão:** 21/01/2026