# Relatório de Identificação e Resolução de Inconsistências (GRE 5)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data do Relatório:** 21/01/2026  
**Responsáveis:** Miguel e Clark (Garantia da Qualidade/Dev)

---

## 1. Objetivo
Este documento registra as inconsistências detectadas entre a especificação de requisitos, o plano de projeto e o produto final (código e interfaces), bem como as ações corretivas adotadas para garantir a conformidade com o Nível G do MPS.Br.

---

## 2. Log de Inconsistências Identificadas

| ID | Origem da Inconsistência | Descrição da Inconsistência | Impacto | Resolução / Ação Corretiva |
| :--- | :--- | :--- | :--- | :--- |
| **INC01** | Requisito vs. Produto | O **RF06** exigia cálculo HSL, mas a primeira versão do código usava distância Euclidiana RGB simples. | Precisão na identificação de cores para daltônicos abaixo do esperado. | Refatoração do módulo `app/core/math_utils.py` para implementar a lógica de Matiz (Hue-prioritized). |
| **INC02** | Requisito vs. Plano | O **RF03** (Tradução Online) não previa o tempo de latência de rede no Plano de Performance (**RNF02**). | O sistema travava a interface por 2 segundos, violando o limite de 200ms. | Introdução do **RD03** (Cache de Tradução) e atualização do Plano de Testes para incluir latência. |
| **INC03** | Plano vs. Produto | O Plano de Configuração previa o uso de **MariaDB**, mas o produto foi entregue utilizando apenas **Pandas/CSV**. | Divergência entre a arquitetura planejada e a implementação técnica. | Atualização do Plano de Projeto para justificar o uso de CSV como persistência de alto desempenho para o volume atual de dados. |
| **INC04** | Interface vs. Requisito | O requisito **RI03** previa alertas de erro, mas o código HTML não possuía o elemento visual para exibir a mensagem. | O usuário ficava sem feedback em caso de HEX inválido. | Implementação da função `showError` no arquivo `templates/index.html` e validação no Pull Request #08. |

---

## 3. Análise de Causa Raiz
A maioria das inconsistências (INC01 e INC04) ocorreu devido à transição de um protótipo inicial (Colab) para uma estrutura profissional (FastAPI/SOLID). A falta de um checklist de GQA no início do projeto permitiu que desvios técnicos fossem codificados.

---

## 4. Conclusão de Conformidade
Após as ações corretivas listadas acima:
- [X] Todos os 23 requisitos estão refletidos no produto final.
- [X] O plano de projeto foi atualizado para refletir a realidade técnica do uso de dados.
- [X] A Matriz de Rastreabilidade (GRE 3) foi revisada para confirmar as correções.

---
**Assinatura:** Clark e Miguel 
**Data de Fechamento:** 21/01/2026