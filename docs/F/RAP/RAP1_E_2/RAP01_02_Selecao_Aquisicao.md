# Planejamento e Seleção de Aquisições (RAP 1 e 2)
**Projeto:** Colorindo o Daltonismo  
**Data:** 21/01/2026  
**Responsáveis:** Clark e Miguel

## 1. Identificação de Necessidades (RAP 1)
Identificamos a necessidade de componentes externos para evitar o desenvolvimento "do zero" de funcionalidades acessórias, focando o esforço no core de identificação cromática.

| Necessidade | Requisito Vinculado | Tipo de Aquisição |
| :--- | :---: | :--- |
| Tradução de termos (EN para PT-BR) | RD03 | API / Biblioteca Externa |
| Processamento de base CSV | RD02 | Biblioteca de Terceiros |
| Infraestrutura de Testes | GQA 2 | Ferramenta de Análise |

## 2. Critérios de Seleção (RAP 1)
Estabelecemos os seguintes pesos para a escolha dos fornecedores tecnológicos:
1. **Custo (Peso 5):** Preferência por licenças Open Source ou Free Tier.
2. **Manutenibilidade (Peso 4):** Documentação clara e estabilidade da versão.
3. **Compatibilidade (Peso 3):** Integração nativa com Python 3.10+.

## 3. Matriz de Seleção de Fornecedores (RAP 2)
Avaliamos as opções disponíveis no mercado antes da tomada de decisão:

### 3.1 Serviço de Tradução
| Candidato | Custo | Compatibilidade | Decisão |
| :--- | :--- | :--- | :--- |
| Google Translate API | Pago por caractere | Alta | Rejeitado (Custo) |
| **Deep-Translator** | **Free (Open Source)** | **Alta** | **Selecionado** |
| Tradução Manual | Alto (Tempo) | Baixa | Rejeitado (Escalabilidade) |

### 3.2 Processamento de Dados
| Candidato | Performance | Facilidade | Decisão |
| :--- | :--- | :--- | :--- |
| **Pandas** | **Alta** | **Alta** | **Selecionado** |
| SQL Nativo | Média | Média | Rejeitado (Complexidade Infra) |

## 4. Aprovação Técnica
A seleção do **Deep-Translator** e do **Pandas** foi aprovada por Miguel (Técnico) e Clark (Qualidade), garantindo que o projeto permaneça dentro do orçamento R$ 0,00 previsto no GPR 6.