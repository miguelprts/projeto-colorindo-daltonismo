# Critérios de Aceitação de Requisitos
## Projeto: Colorindo o Daltonismo

Data: 18/01/2026
Versão: 1.0
Aprovado por: Clark Cerqueira Engelhardt Veronez e Miguel Souza Portes

---

## 6 Critérios Objetivos para Avaliar Requisitos

### 1. Clareza e Objetividade
**Definição:** O requisito está escrito de forma clara, sem ambiguidades semânticas, usando linguagem técnica apropriada.

**Checklist:**
- ✓ Requisito usa verbo no imperativo (ex: "O sistema deve...")
- ✓ Não há palavras vagas (rápido, bonito, fácil)
- ✓ Está em português claro e técnico
- ✓ Qualquer membro da equipe consegue entender

**Exemplo RUIM:** "O sistema deve ser rápido"  
**Exemplo BOM:** "O sistema deve retornar resultados em < 200ms (P95)"

---

### 2. Testabilidade
**Definição:** É possível criar testes automatizados para o requisito, com critérios mensuráveis.

**Checklist:**
- ✓ Possui critério de aceitação mensurável (ex: "API retorna JSON em < 100ms")
- ✓ Não é vago (evitar: "sistema deve ser seguro")
- ✓ Pode ser verificado automaticamente
- ✓ Cada requisito funcional tem mínimo 1 teste

**Exemplo RUIM:** "Sistema deve ser acessível"  
**Exemplo BOM:** "Contraste mínimo 4.5:1, suporte a keyboard (Tab, Enter)"

---

### 3. Rastreabilidade
**Definição:** Cada requisito tem identificador único e permite rastreamento até implementação e testes.

**Checklist:**
- ✓ Tem ID único (RF-001, RF-002, etc)
- ✓ Está vinculado a caso(s) de teste (TC-001.1, etc)
- ✓ Vinculado a arquivo de implementação
- ✓ Permite rastreamento bidirecional

**Exemplo:** RF-001 → TC-001.1 → app.py:get_color_name_by_hex()

---

### 4. Factibilidade
**Definição:** Requisito pode ser implementado com tecnologia disponível, dentro do escopo e prazo.

**Checklist:**
- ✓ Usa tecnologia disponível (FastAPI, React, Python 3.8+)
- ✓ Está dentro do escopo do projeto
- ✓ Não depende de recursos não alocados
- ✓ Pode ser completado em tempo hábil

**Exemplo RUIM:** "Integrar com modelo de IA ainda não treinado"  
**Exemplo BOM:** "Usar Google Translate API (já disponível)"

---

### 5. Completude
**Definição:** Requisito define completamente entrada, processamento, saída e restrições técnicas.

**Checklist:**
- ✓ Define entrada esperada (ex: hexadecimal)
- ✓ Define saída esperada (ex: JSON com nome)
- ✓ Especifica restrições técnicas (performance, segurança)
- ✓ Menciona dependências externas
- ✓ Suficiente para iniciar implementação

**Exemplo COMPLETO:**

Entrada: Código hexadecimal (com ou sem #)
Processamento: Buscar no dataset, calcular distância HSL se necessário
Saída: JSON com name_en, name_pt, RGB, HSL
Restrição: < 200ms (P95)
Dependência: RF-007 (Dataset), RF-004 (Análise HSL)


---

### 6. Consistência
**Definição:** Requisito não entra em conflito com outros, usa terminologia uniforme e está alinhado com arquitetura.

**Checklist:**
- ✓ Não duplica outro requisito
- ✓ Não entra em conflito com requisitos existentes
- ✓ Usa mesma terminologia do projeto
- ✓ Está alinhado com arquitetura geral

**Exemplo CONFLITO:** 
- RF-001: "Buscar por hex em < 200ms"
- RF-002: "Buscar por nome em < 100ms" ← Conflita com performance global

---

## ✅ Matriz de Aprovação

| Critério | Atendido? | Observação |
|----------|-----------|-----------|
| 1. Clareza | ✅ | Todos os RFs em linguagem técnica clara |
| 2. Testabilidade | ✅ | Todos têm casos de teste mapeados (TC-XXX) |
| 3. Rastreabilidade | ✅ | IDs RF-001 a RF-009 atribuídos |
| 4. Factibilidade | ✅ | Tecnologia FastAPI/React disponível |
| 5. Completude | ✅ | Entrada/saída especificadas em cada RF |
| 6. Consistência | ✅ | Sem conflitos detectados |

**Status:** ✅ TODOS OS REQUISITOS APROVADOS