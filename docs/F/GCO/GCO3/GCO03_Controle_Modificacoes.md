# Controle de Modificações (GCO 3)
**Projeto:** Colorindo o Daltonismo  
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Fluxo de Controle de Mudanças
Toda modificação nos Itens de Configuração (ICs) identificados no GCO 1 deve seguir o fluxo abaixo para garantir a integridade do produto:

1. **Solicitação de Mudança (SM):** Identificação de uma necessidade (bug ou melhoria).
2. **Análise de Impacto:** Avaliação de como a mudança afeta cronograma, custo e outros requisitos.
3. **Aprovação/Rejeição:** Decisão tomada pelos líderes (Miguel e Clark).
4. **Implementação:** Criação de uma branch `feature/` ou `hotfix/`.
5. **Revisão e Merge:** Pull Request com revisão de código e validação de testes.

## 2. Registro de Mudança Significativa (Exemplo Real)

| Campo | Detalhes da Modificação |
| :--- | :--- |
| **ID da Mudança** | SM-002 |
| **Item de Configuração** | IC-01 (Código Core) e IC-03 (Dados/Requisitos) |
| **Descrição** | Alterar trava de similaridade de 60% para 95% (RD05). |
| **Justificativa** | Mitigar o risco de falsos positivos na identificação de cores. |
| **Impacto Estimado** | +2h de esforço em testes e atualização da Matriz de Rastreabilidade. |
| **Status da Aprovação** | **Aprovado** por Miguel e Clark em 16/01/2026. |

## 3. Implementação Técnica (Rastreabilidade)
A modificação SM-002 foi implementada através do commit `feat(core): update similarity threshold to 0.95` e vinculada à Issue #12 no GitHub. O fechamento da mudança ocorreu após o sucesso dos testes unitários em `test_core.py`.

## 4. Controle de Versão de Documentos
Para documentos em Markdown (.md), o controle de modificações é mantido pela seção "Histórico de Revisões" no final de cada arquivo, além do histórico de diff do Git.