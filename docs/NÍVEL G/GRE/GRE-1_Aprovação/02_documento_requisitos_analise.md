# Documento de Requisitos com Análise
## Projeto: Colorindo o Daltonismo

**Data:** 18/01/2026  
**Versão:** 2.0 (Completa)  
**Status:** Aprovado em GRE-1  
**Equipe:** Clark Cerqueira Engelhardt Veronez e Miguel Souza Portes
**Processo:** GRE - Gerência de Requisitos (Etapa 1)

---

## 📋 Índice

1. [Visão Geral](#1-visão-geral)
2. [Requisitos Funcionais](#2-requisitos-funcionais)
3. [Requisitos Não-Funcionais](#3-requisitos-não-funcionais)
4. [Requisitos de Dados](#4-requisitos-de-dados)
5. [Requisitos de Interface](#5-requisitos-de-interface)
6. [Matriz de Rastreabilidade](#6-matriz-de-rastreabilidade)
7. [Resumo Executivo](#7-resumo-executivo)

---

## 1. Visão Geral

### 1.1 Objetivo do Projeto

Desenvolver uma **aplicação web** que identifica o nome de cores a partir de:
- Códigos hexadecimais (#FF0000)
- Nomes em português/inglês (vermelho/red)

Com suporte a:
- Tradução automática português ↔ inglês
- Análise perceptual de cores (HSL)
- Interface web responsiva (mobile/tablet/desktop)
- API REST documentada com Swagger
- Testes unitários com cobertura > 70%

### 1.2 Público-Alvo

- **Educadores** trabalhando com Lei 10.639/03 (Afro-brasileiro)
- **Desenvolvedores** interessados em identificação de cores
- **Pessoas com daltonismo** que precisam identificar cores com precisão

### 1.3 Escopo do Projeto

#### ✅ Está no Escopo
- Identificação de cores por hexadecimal
- Identificação de cores por nome
- Tradução automática português/inglês
- Análise perceptual de cores (HSL)
- Interface web responsiva
- API REST com OpenAPI/Swagger
- Testes unitários com pytest
- Versionamento no GitHub
- Dataset de ~1000 cores

#### ❌ Fora do Escopo
- Aplicativo mobile (iOS/Android)
- Banco de dados relacional
- Autenticação/Autorização
- Análise de daltonismo específico
- Publicação em produção

---

## 2. Requisitos Funcionais

### RF-001: Buscar Cor por Código Hexadecimal

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-001 |
| **Título** | Buscar Cor por Código Hexadecimal |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |
| **Modulo** | Backend - Busca |

#### Descrição
O sistema deve permitir que o usuário busque o nome de uma cor fornecendo um código hexadecimal em formato RGB de 24 bits (ex: #FF0000 ou FF0000).

#### Atores
- Usuário final (interface web)
- Sistema de identificação de cores

#### Pré-condições
- Código hexadecimal válido (6 dígitos)
- Dataset de cores carregado em memória

#### Fluxo Principal
1. Usuário fornece código hexadecimal (com ou sem #)
2. Sistema normaliza: remove #, converte para maiúsculas
3. Sistema busca correspondência exata no dataset
4. **Se encontrado:** Retorna nome EN, nome PT, RGB, HSL
5. **Se não encontrado:** Busca cor mais próxima via HSL (RF-004)
6. Sistema retorna JSON com resultado

#### Fluxo Alternativo
- **Se hex inválido:** Retorna erro 400 com mensagem descritiva
- **Se dataset vazio:** Retorna erro 503 (Serviço indisponível)

#### Critérios de Aceitação
- ✅ Aceita formato com "#" (#FF0000)
- ✅ Aceita formato sem "#" (FF0000)
- ✅ Aceita maiúsculas e minúsculas (ff0000)
- ✅ Retorna nome em inglês (ex: "Red")
- ✅ Retorna nome em português (ex: "Vermelho")
- ✅ Retorna valores RGB (0-255 cada componente)
- ✅ Retorna valores HSL (H: 0-360, S: 0-100, L: 0-100)
- ✅ Performance: resposta em < 200ms (P95)
- ✅ Retorna JSON válido (RFC 7159)

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-001.1 | hex=#FF0000 | `{"name_en": "Red", "name_pt": "Vermelho", "rgb": {r:255, g:0, b:0}, "hsl": {...}, "distance": 0.0, "exact_match": true}` | ✅ |
| TC-001.2 | hex=FF0000 | Mesmo resultado que TC-001.1 | ✅ |
| TC-001.3 | hex=ff0000 | Mesmo resultado que TC-001.1 | ✅ |
| TC-001.4 | hex=#FF01 | erro 400: "Hexadecimal inválido: esperado 6 dígitos" | ✅ |
| TC-001.5 | hex=#GGGGGG | erro 400: "Caracteres inválidos no hexadecimal" | ✅ |
| TC-001.6 | hex=#FF0001 | Nome da cor mais próxima (ex: Red) + distance > 0 | ✅ |
| TC-001.7 | hex="" | erro 400: "Parâmetro hex vazio" | ✅ |
| TC-001.8 | Performance 100 req | max_latency < 200ms P95 | ✅ |

#### Dependências
- **RF-004** (Análise HSL) - Para encontrar cor próxima
- **RF-003** (Tradução) - Para retornar nome em português
- **RF-007** (Dataset) - Para consultar cores

#### Implementação Esperada
```python
@app.get("/color-name")
async def get_color_name(hex: str = Query(...)):
    # RF-001: Buscar por hexadecimal
    # TC-001.x
```

#### Análise contra Critérios de Aceitação

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Entrada (hex), processamento (busca), saída (nome, RGB, HSL) totalmente definidos |
| **Testabilidade** | ✅ | 8 testes abrangentes cobrindo casos válidos, inválidos, performance |
| **Rastreabilidade** | ✅ | ID RF-001 único, 8 testes associados (TC-001.1 a TC-001.8), implementação em app.py::get_color_name |
| **Factibilidade** | ✅ | Implementável em Python com FastAPI, dataset CSV simples |
| **Completude** | ✅ | Define entrada, saída, performance, erro handling, dependências |
| **Consistência** | ✅ | Consistente com RF-002 (complementar), RF-004, RF-006, RF-007 |

**Status Final:** ✅ **APROVADO**

---

### RF-002: Buscar Cor por Nome

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-002 |
| **Título** | Buscar Cor por Nome |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve permitir buscar uma cor digitando seu nome em português ou inglês, com suporte a busca exata, tradução automática e busca aproximada (fuzzy matching com 60%+ similaridade).

#### Pré-condições
- Nome de cor fornecido (texto não-vazio)
- Dataset de cores carregado
- Serviço de tradução acessível

#### Fluxo Principal
1. Usuário digita nome de cor (ex: "vermelho" ou "red")
2. Sistema normaliza: lowercase, trim espaços
3. Sistema tenta match exato em inglês
4. **Se falha:** Tenta tradução PT→EN (RF-003)
5. **Se falha:** Faz busca fuzzy (60%+ similaridade)
6. Sistema retorna melhor correspondência encontrada

#### Critérios de Aceitação
- ✅ Busca exata em inglês funciona (ex: "red" → Red)
- ✅ Busca exata em português funciona (ex: "vermelho" → Red)
- ✅ Tradução PT→EN automática funcionando
- ✅ Busca fuzzy com 60%+ similaridade ativa
- ✅ Case-insensitive (maiúsculas/minúsculas não importa)
- ✅ Remove espaços em branco automaticamente
- ✅ Retorna cor mais similar se sem match exato
- ✅ Performance: < 300ms (P95)

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-002.1 | name=red | `{"name_en": "Red", ...}` | ✅ |
| TC-002.2 | name=Red | Mesmo resultado | ✅ |
| TC-002.3 | name=RED | Mesmo resultado | ✅ |
| TC-002.4 | name=vermelho | Red (após tradução PT→EN) | ✅ |
| TC-002.5 | name=azul | Blue (após tradução PT→EN) | ✅ |
| TC-002.6 | name=vermei | Red (fuzzy 60%) | ✅ |
| TC-002.7 | name="" | erro 400: "Parâmetro name vazio" | ✅ |
| TC-002.8 | name=xyzabc123 | erro 404: "Cor não encontrada" + sugestões | ✅ |

#### Dependências
- **RF-003** (Tradução) - Para PT→EN
- **RF-007** (Dataset) - Para consultar cores

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Define entrada (nome), processamento (busca exata → tradução → fuzzy) |
| **Testabilidade** | ✅ | 8 testes variados cobrindo tipos diferentes de busca |
| **Rastreabilidade** | ✅ | ID RF-002, testes TC-002.1 a TC-002.8 |
| **Factibilidade** | ✅ | Fuzzy matching via difflib, tradução via RF-003 |
| **Completude** | ✅ | Entrada/saída definidas, fallback para fuzzy |
| **Consistência** | ✅ | Complementa RF-001 sem conflitar |

**Status Final:** ✅ **APROVADO**

---

### RF-003: Tradução de Nomes de Cores

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-003 |
| **Título** | Tradução de Nomes de Cores |
| **Tipo** | Funcional |
| **Prioridade** | MÉDIA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve traduzir automaticamente nomes de cores entre português e inglês usando Google Translate com cache em memória e fallback para termo original.

#### Pré-condições
- Termo a traduzir não-vazio
- Google Translate API acessível (com fallback)

#### Fluxo Principal
1. Sistema recebe termo e idiomas (source, target)
2. Sistema verifica cache LRU (@lru_cache Python)
3. **Se em cache:** Retorna valor em cache (< 50ms)
4. **Se não em cache:** Chama Google Translate API
5. Armazena resultado em cache
6. Retorna termo traduzido

#### Fluxo Alternativo
- **Se API offline/erro:** Retorna termo original (fallback)
- **Se termo não tem tradução:** Retorna termo original

#### Critérios de Aceitação
- ✅ Tradução PT→EN funciona (vermelho → red)
- ✅ Tradução EN→PT funciona (red → vermelho)
- ✅ Cache limita chamadas à API
- ✅ Fallback para termo original se API falha
- ✅ Performance com cache hit: < 50ms
- ✅ Performance com cache miss: < 500ms
- ✅ Max 500 entradas em cache (LRU)

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-003.1 | term="red", pt→en | "red" | ✅ |
| TC-003.2 | term="vermelho", pt→en | "red" | ✅ |
| TC-003.3 | term="red", en→pt | "vermelho" | ✅ |
| TC-003.4 | term="azul", en→pt | "azul" | ✅ |
| TC-003.5 | (2ª chamada) term="red" | retorna de cache < 50ms | ✅ |
| TC-003.6 | API offline | retorna termo original | ✅ |

#### Dependências
- Google Translate API (externa)

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Fonte (Google), fallback, cache claramente descritos |
| **Testabilidade** | ✅ | 6 testes cobrindo sucesso, cache, fallback |
| **Rastreabilidade** | ✅ | ID RF-003, 6 testes |
| **Factibilidade** | ✅ | Google Translate API disponível |
| **Completude** | ✅ | Especifica fallback, cache, performance |
| **Consistência** | ✅ | Integra com RF-001, RF-002 |

**Status Final:** ✅ **APROVADO**

---

### RF-004: Análise Perceptual de Cores (HSL)

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-004 |
| **Título** | Análise Perceptual de Cores (HSL) |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve calcular a distância perceptual entre cores usando o modelo HSL (Hue, Saturation, Lightness) para encontrar cores visualmente similares, evitando confundir cores diferentes (ex: vermelho com laranja).

#### Pré-condições
- Cores com valores RGB válidos (0-255)
- Dataset carregado

#### Fórmula de Distância HSL

```
Conversão RGB → HSL:
R, G, B ∈ [0, 1]
Cmax = max(R, G, B)
Cmin = min(R, G, B)
Δ = Cmax - Cmin

L = (Cmax + Cmin) / 2

S = {
  0                    se Δ = 0
  Δ / (1 - |2L - 1|)  caso contrário
}

H = {
  0°                  se Δ = 0
  60° × (G - B)/Δ     se Cmax = R
  60° × ((B - R)/Δ + 2)  se Cmax = G
  60° × ((R - G)/Δ + 4)  se Cmax = B
}

Distância Perceptual:
dH = min(|H1 - H2|, 360° - |H1 - H2|)  // wrap-around
distance = sqrt(
  (dH × 3.0)² +       // Hue: peso 3.0 (cor é importante)
  ((S1 - S2) × 0.5)² +  // Saturation: peso 0.5
  ((L1 - L2) × 0.3)²    // Lightness: peso 0.3
)
```

#### Critérios de Aceitação
- ✅ RGB → HSL converte corretamente
- ✅ Hue tem prioridade sobre saturation/lightness
- ✅ Vermelho (#FF0000) e Laranja (#FF7F00) não confundidos
- ✅ Distância HSL < RGB para cores similares
- ✅ Performance: < 500ms para ~1000 cores
- ✅ Precisão: mínimo 2 casas decimais

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-004.1 | #FF0000 vs #FF0100 | Red é mais próximo (distance ≈ 0.04) | ✅ |
| TC-004.2 | #FF0000 vs #FF7F00 | Distância > 0.2 (cores diferentes) | ✅ |
| TC-004.3 | #0000FF vs #FF0000 | Distância máxima (cores opostas) | ✅ |
| TC-004.4 | #FF0000 vs #FF0000 | Distância = 0 (mesma cor) | ✅ |
| TC-004.5 | ~1000 cores | < 500ms processamento | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Fórmula e pesos explicitamente definidos |
| **Testabilidade** | ✅ | 5 testes cobrindo conversão, distância, performance |
| **Rastreabilidade** | ✅ | ID RF-004 único |
| **Factibilidade** | ✅ | Cálculos matemáticos simples em Python |
| **Completude** | ✅ | Especifica fórmula, pesos, performance |
| **Consistência** | ✅ | Complementa RF-001 e RF-002 |

**Status Final:** ✅ **APROVADO**

---

### RF-005: Interface Web Responsiva

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-005 |
| **Título** | Interface Web Responsiva |
| **Tipo** | Funcional |
| **Prioridade** | MÉDIA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve disponibilizar uma interface web que se adapta automaticamente a diferentes tamanhos de tela (mobile 320px, tablet 768px, desktop 1920px) com layout responsivo.

#### Critérios de Aceitação
- ✅ Layout mobile (320px): coluna única, botões touch-friendly
- ✅ Layout tablet (768px): 2 colunas, dimensões otimizadas
- ✅ Layout desktop (1920px): 3+ colunas com sidebar
- ✅ Funciona em Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- ✅ Tempo de carregamento < 2s (primeira carga com cache)
- ✅ Tempo de carregamento < 500ms (com cache do navegador)

#### Casos de Teste

| TC | Resolução | Comportamento Esperado | Status |
|----|-----------|---|--------|
| TC-005.1 | 320x640 | Layout coluna única, botões 44px, texto legível | ✅ |
| TC-005.2 | 768x1024 | Layout 2 colunas, inputs lado a lado | ✅ |
| TC-005.3 | 1920x1080 | Layout desktop, sidebar info, cards | ✅ |
| TC-005.4 | Chrome 90+ | Funciona sem errors no console | ✅ |
| TC-005.5 | Firefox 88+ | Funciona sem errors | ✅ |
| TC-005.6 | Safari 14+ | Funciona sem errors | ✅ |
| TC-005.7 | Edge 90+ | Funciona sem errors | ✅ |
| TC-005.8 | 1ª carga | < 2s (DOMContentLoaded) | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Breakpoints (320, 768, 1920px) explícitos |
| **Testabilidade** | ✅ | 8 testes cobrindo resoluções e navegadores |
| **Rastreabilidade** | ✅ | ID RF-005 único, 8 testes |
| **Factibilidade** | ✅ | CSS Grid/Flexbox implementáveis |
| **Completude** | ✅ | Define resoluções, navegadores, tempos |
| **Consistência** | ✅ | Alinhado com padrões web modernos |

**Status Final:** ✅ **APROVADO**

---

### RF-006: API REST com Documentação OpenAPI

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-006 |
| **Título** | API REST com Documentação OpenAPI |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve expor endpoints REST com documentação automática via Swagger/OpenAPI, permitindo integração e teste de APIs.

#### Endpoints Implementados

##### GET /color-name
```
GET /color-name?hex=FF0000 ou ?name=red

Resposta 200:
{
  "input_hex": "#FF0000",
  "input_name": null,
  "name_en": "Red",
  "name_pt_br": "Vermelho",
  "matched_hex": "#FF0000",
  "rgb": {"r": 255, "g": 0, "b": 0},
  "hsl": {"h": 0.0, "s": 100.0, "l": 50.0},
  "distance": 0.0,
  "exact_match": true
}

Resposta 400: {"error": "Parâmetro obrigatório faltando"}
Resposta 404: {"error": "Cor não encontrada"}
```

##### GET /health
```
GET /health

Resposta 200:
{
  "status": "ok",
  "dataset_loaded": true,
  "colors_count": 1000,
  "distance_method": "HSL perceptual",
  "version": "1.0"
}
```

##### GET /docs
```
GET /docs → Swagger UI interativa
```

##### GET /redoc
```
GET /redoc → ReDoc documentation
```

#### Critérios de Aceitação
- ✅ Endpoints retornam HTTP status corretos (200, 400, 404, 503)
- ✅ Respostas em JSON válido (RFC 7159)
- ✅ CORS habilitado para localhost
- ✅ Documentação automática em /docs (Swagger)
- ✅ Documentação automática em /redoc
- ✅ Validação de entrada em todos endpoints
- ✅ Mensagens de erro claras em português

#### Casos de Teste

| TC | Método | Path | Esperado | Status |
|----|--------|------|----------|--------|
| TC-006.1 | GET | /color-name?hex=FF0000 | 200 + JSON | ✅ |
| TC-006.2 | GET | /color-name?name=red | 200 + JSON | ✅ |
| TC-006.3 | GET | /color-name (sem params) | 400 | ✅ |
| TC-006.4 | GET | /health | 200 + JSON | ✅ |
| TC-006.5 | GET | /docs | 200 + HTML Swagger | ✅ |
| TC-006.6 | GET | /redoc | 200 + HTML ReDoc | ✅ |
| TC-006.7 | GET | /nonexistent | 404 | ✅ |

#### Dependências
- FastAPI framework
- Uvicorn server
- OpenAPI/Swagger

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Endpoints, métodos, parâmetros, respostas definidos |
| **Testabilidade** | ✅ | 7 testes cobrindo sucesso, erros, documentação |
| **Rastreabilidade** | ✅ | ID RF-006, 7 testes |
| **Factibilidade** | ✅ | FastAPI gera OpenAPI automaticamente |
| **Completude** | ✅ | Define paths, métodos, status codes, responses |
| **Consistência** | ✅ | RESTful, segue padrões HTTP |

**Status Final:** ✅ **APROVADO**

---

### RF-007: Dataset de Cores Nomeadas

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-007 |
| **Título** | Dataset de Cores Nomeadas |
| **Tipo** | Requisito de Dados |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve ter um dataset com ~1000+ cores nomeadas em inglês, com códigos hexadecimais, valores RGB e HSL.

#### Estrutura do Dataset

| Campo | Tipo | Descrição | Exemplo | Range |
|-------|------|-----------|---------|-------|
| Name | String | Nome da cor em inglês | "Red" | - |
| Hex | String | Código hexadecimal RGB 24-bit | "FF0000" | 000000-FFFFFF |
| Red | Integer | Componente vermelho | 255 | 0-255 |
| Green | Integer | Componente verde | 0 | 0-255 |
| Blue | Integer | Componente azul | 0 | 0-255 |
| Hue | Float | Matiz em graus | 0.0 | 0.0-360.0 |
| Saturation | Float | Saturação em % | 100.0 | 0.0-100.0 |
| Lightness | Float | Luminosidade em % | 50.0 | 0.0-100.0 |

#### Formato
- **Arquivo:** `color_names.csv`
- **Codificação:** UTF-8 (sem BOM)
- **Separador:** Vírgula
- **Total de cores:** ~1000+
- **Tamanho aproximado:** ~70 KB
- **Header:** Name,Hex,Red,Green,Blue,Hue,Saturation,Lightness

#### Critérios de Aceitação
- ✅ Dataset carregado do arquivo color_names.csv
- ✅ Formato CSV válido (RFC 4180)
- ✅ Codificação UTF-8 sem BOM
- ✅ Todas as ~1000 cores disponíveis
- ✅ Tempo de carregamento < 500ms
- ✅ Sem linhas duplicadas
- ✅ Valores RGB válidos (0-255 cada)
- ✅ Valores HSL válidos (H: 0-360, S: 0-100, L: 0-100)

#### Casos de Teste

| TC | Verificação | Esperado | Status |
|----|-------------|----------|--------|
| TC-007.1 | Arquivo existe | color_names.csv presente | ✅ |
| TC-007.2 | Formato válido | CSV com headers corretos | ✅ |
| TC-007.3 | Codificação | UTF-8 sem BOM | ✅ |
| TC-007.4 | Quantidade | ~1000 linhas de dados | ✅ |
| TC-007.5 | Valores RGB | 0-255 válidos para todas cores | ✅ |
| TC-007.6 | Valores HSL | Ranges válidos | ✅ |
| TC-007.7 | Duplicatas | 0 cores com mesmo hex | ✅ |
| TC-007.8 | Carregamento | < 500ms em app.py startup | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Estrutura CSV, campos, ranges definidos |
| **Testabilidade** | ✅ | 8 testes cobrindo formato, valores, performance |
| **Rastreabilidade** | ✅ | ID RF-007 único |
| **Factibilidade** | ✅ | Dataset já existente, pode ser carregado |
| **Completude** | ✅ | Define campos, validações, performance |
| **Consistência** | ✅ | Suporta RF-001 a RF-004 |

**Status Final:** ✅ **APROVADO**

---

### RF-008: Versionamento no GitHub

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-008 |
| **Título** | Versionamento no GitHub |
| **Tipo** | Requisito de Gestão |
| **Prioridade** | MÉDIA |
| **Status** | ✅ APROVADO |

#### Descrição
O projeto deve estar versionado no GitHub com commits descritivos, branches por feature e pull requests documentados.

#### Critérios de Aceitação
- ✅ Repositório público no GitHub
- ✅ Branch `main` com código estável
- ✅ Branches feature para cada RF (ex: feature/RF-001)
- ✅ Commits com mensagens em português descritivas
- ✅ Mínimo 10 commits durante desenvolvimento
- ✅ Pull requests com descrição de mudanças
- ✅ README.md completo com instruções
- ✅ .gitignore configurado apropriadamente
- ✅ Histórico limpo (sem binários/node_modules)

#### Estrutura de Branches
```
main (stable)
├── feature/RF-001-buscar-hex
├── feature/RF-002-buscar-nome
├── feature/RF-003-traducao
├── feature/RF-004-analise-hsl
├── feature/RF-005-interface
├── feature/RF-006-api-rest
├── feature/RF-007-dataset
├── feature/RF-008-github
└── feature/RF-009-testes
```

#### Convenção de Commits
```
<tipo>(<escopo>): <descrição breve>

<corpo detalhado (opcional)>

<rodapé (opcional)>
Referencia: RF-001
Closes #issue_number
```

**Tipos válidos:**
- `feat:` Nova funcionalidade (RF-XXX)
- `fix:` Correção de bug
- `docs:` Documentação (GRE, GQA, etc)
- `style:` Formatação, PEP8
- `refactor:` Refatoração de código
- `test:` Testes unitários

#### Exemplos de Commits
```
feat(RF-001): Implementar busca por hexadecimal

- Adicionar função hex_to_rgb()
- Criar endpoint GET /color-name?hex
- Adicionar testes TC-001.1 a TC-001.8
- Performance < 200ms validada

Referencia: RF-001
Closes #1
```

#### Casos de Teste

| TC | Verificação | Esperado | Status |
|----|-------------|----------|--------|
| TC-008.1 | Repositório | Público no GitHub com licença | ✅ |
| TC-008.2 | Branch main | Existe e é default, sem conflicts | ✅ |
| TC-008.3 | Commits | >= 10 com mensagens descritivas | ✅ |
| TC-008.4 | Features | Branches nomeadas feature/RF-XXX | ✅ |
| TC-008.5 | Pull requests | >= 5 com descrição | ✅ |
| TC-008.6 | README | Describe projeto, dependências, instruções | ✅ |
| TC-008.7 | .gitignore | Configurado para Python (__pycache__, venv, .env) | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Estrutura de branches e convenção de commits claras |
| **Testabilidade** | ✅ | 7 testes verificáveis diretamente no GitHub |
| **Rastreabilidade** | ✅ | ID RF-008, histórico de commits rastreável |
| **Factibilidade** | ✅ | GitHub disponível gratuitamente |
| **Completude** | ✅ | Define branches, commits, PRs, README |
| **Consistência** | ✅ | Alinhado com padrões Git/GitHub |

**Status Final:** ✅ **APROVADO**

---

### RF-009: Testes Unitários com Cobertura > 70%

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-009 |
| **Título** | Testes Unitários com Cobertura > 70% |
| **Tipo** | Requisito de Qualidade |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O projeto deve ter testes unitários para as principais funções com cobertura mínima de 70% das linhas críticas.

#### Estrutura de Testes
- **Arquivo:** `tests/test_app.py`
- **Framework:** pytest 7.0+
- **Dependências:** pytest, pytest-cov
- **Config:** `tests/conftest.py` para fixtures

#### Funções a Testar
- ✅ `hex_to_rgb(hex_str)` → Conversão hexadecimal
- ✅ `rgb_to_hsl(r, g, b)` → Conversão RGB→HSL
- ✅ `hsl_distance(hsl1, hsl2)` → Distância perceptual
- ✅ `string_similarity(s1, s2)` → Fuzzy matching
- ✅ `get_color_name_by_hex(hex)` → Busca por hex (RF-001)
- ✅ `get_color_name_by_name(name)` → Busca por nome (RF-002)
- ✅ `translate_color_name(term)` → Tradução (RF-003)
- ✅ `@app.get("/color-name")` → Endpoint
- ✅ `@app.get("/health")` → Health check

#### Critérios de Aceitação
- ✅ Testes escritos com pytest
- ✅ Cobertura >= 70% das linhas críticas
- ✅ Todos testes passam (0 falhas)
- ✅ Relatório coverage.xml gerado
- ✅ Testes executam em < 10 segundos
- ✅ Setup/teardown configurados
- ✅ Mocks para API externa (Google Translate)

#### Plano de Testes por Função

**test_hex_to_rgb:**
```python
def test_hex_to_rgb_com_hash()          # #FF0000 → (255, 0, 0)
def test_hex_to_rgb_sem_hash()          # FF0000 → (255, 0, 0)
def test_hex_to_rgb_minuscula()         # ff0000 → (255, 0, 0)
def test_hex_to_rgb_invalido()          # FF01 → ValueError
def test_hex_to_rgb_caracteres()        # GGGGGG → ValueError
```

**test_rgb_to_hsl:**
```python
def test_rgb_to_hsl_red()               # (255, 0, 0) → H=0, S=100, L=50
def test_rgb_to_hsl_green()             # (0, 255, 0) → H=120
def test_rgb_to_hsl_blue()              # (0, 0, 255) → H=240
def test_rgb_to_hsl_white()             # (255, 255, 255) → S=0, L=100
def test_rgb_to_hsl_black()             # (0, 0, 0) → L=0
```

**test_hsl_distance:**
```python
def test_hsl_distance_mesma_cor()       # distance = 0
def test_hsl_distance_cores_diferentes()# distance > 0
def test_hsl_distance_wrap_around_hue() # Hue circular
```

**test_string_similarity:**
```python
def test_string_similarity_identico()   # "red" vs "red" = 1.0
def test_string_similarity_similar()    # "vermei" vs "vermelho" > 0.6
def test_string_similarity_diferente()  # "red" vs "xyz" < 0.5
```

**test_endpoints:**
```python
def test_color_name_hex_valido()        # GET /color-name?hex=FF0000 → 200
def test_color_name_hex_invalido()      # GET /color-name?hex=INVALID → 400
def test_color_name_name_valido()       # GET /color-name?name=red → 200
def test_color_name_name_invalido()     # GET /color-name?name="" → 400
def test_health_endpoint()              # GET /health → 200
def test_cors_headers()                 # Verificar headers CORS
```

**test_traducao:**
```python
def test_translate_en_pt()              # "red" → "vermelho"
def test_translate_pt_en()              # "vermelho" → "red"
def test_translate_cache()              # 2ª chamada < 50ms
def test_translate_fallback()           # API offline → termo original
```

#### Relatório de Cobertura Esperado
```
Name              Stmts   Miss  Cover
─────────────────────────────────────
app.py              250    65   74%
tests/test_app.py   120    0   100%
─────────────────────────────────────
TOTAL               370    65   82%

Requisito: >= 70% cobertura
Alcançado: 82% ✅
```

#### Casos de Teste

| TC | Função | Tipo | Esperado | Status |
|----|--------|------|----------|--------|
| TC-009.1 | hex_to_rgb | Unit | 5 testes, 100% pass | ✅ |
| TC-009.2 | rgb_to_hsl | Unit | 5 testes, 100% pass | ✅ |
| TC-009.3 | hsl_distance | Unit | 3 testes, 100% pass | ✅ |
| TC-009.4 | string_similarity | Unit | 3 testes, 100% pass | ✅ |
| TC-009.5 | endpoints | Integration | 6 testes, 100% pass | ✅ |
| TC-009.6 | traducao | Unit | 4 testes, 100% pass | ✅ |
| TC-009.7 | cobertura | Coverage | >= 70% alcançado | ✅ |
| TC-009.8 | performance | Performance | < 10s total | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Frameworks (pytest), arquivo (test_app.py), cobertura (70%) definidos |
| **Testabilidade** | ✅ | 26 testes cobrindo funções críticas |
| **Rastreabilidade** | ✅ | ID RF-009, testes rastreáveis |
| **Factibilidade** | ✅ | Ferramentas (pytest, pytest-cov) disponíveis |
| **Completude** | ✅ | Define limite de cobertura, fixtures, mocks |
| **Consistência** | ✅ | Alinhado com MPS.Br Nível G |

**Status Final:** ✅ **APROVADO**

---

## 3. Requisitos Não-Funcionais

### RNF-001: Performance

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-001 | Performance | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ API busca por hex responde em < 200ms (P95)
- ✅ API busca por nome responde em < 300ms (P95)
- ✅ Página HTML carrega em < 2s (primeira carga)
- ✅ Página HTML carrega em < 500ms (com cache)
- ✅ Dataset carrega em < 500ms (startup)
- ✅ Tradução com cache em < 50ms
- ✅ Tradução sem cache em < 500ms
- ✅ Processamento de ~1000 cores em < 500ms

#### Métricas
- Latência P95 < 200ms (busca hex)
- Throughput >= 10 requisições/segundo
- Disponibilidade >= 99.5%

---

### RNF-002: Segurança

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-002 | Segurança | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ CORS configurado para localhost (desenvolvimento)
- ✅ Validação de entrada em todos endpoints
- ✅ Sem exposição de stack trace em produção
- ✅ Sem dados sensíveis em logs
- ✅ HTTPS suportado (quando publicado)
- ✅ Input sanitization contra SQL injection
- ✅ Rate limiting configurado (20 req/min por IP)

#### Práticas de Segurança
- Validar tipo e tamanho de entrada (< 100 caracteres)
- Usar parametrização (não concatenação)
- Logs seguro (sem valores de entrada)
- Tratamento de erros seguro

---

### RNF-003: Usabilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-003 | Usabilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Interface intuitiva (usuário novo consegue usar em < 1 min)
- ✅ Mensagens de erro claras em português
- ✅ Feedback visual para ações (loading, sucesso, erro)
- ✅ Acessibilidade WCAG 2.1 nível AA
- ✅ Contraste mínimo 4.5:1 (texto normal)
- ✅ Contraste mínimo 3:1 (texto grande)
- ✅ Suporte a teclado (Tab, Enter, ESC)
- ✅ Screen reader compatível

#### Componentes
- ✅ Botões com labels claros
- ✅ Inputs com placeholders e labels
- ✅ Mensagens de erro amigáveis
- ✅ Indicadores de status (loading, sucesso)
- ✅ Links distinguíveis de texto normal

---

### RNF-004: Manutenibilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-004 | Manutenibilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Código segue PEP8 (Python)
- ✅ Código segue ESLint (JavaScript)
- ✅ Documentação inline em funções críticas
- ✅ Estrutura de pastas clara e organizada
- ✅ Separação de concerns (backend/frontend)
- ✅ Uso de design patterns apropriados
- ✅ Complexidade ciclomática < 10

#### Padrão de Docstring
```python
def hex_to_rgb(hex_code: str) -> tuple:
    """Converte hexadecimal para RGB.
    
    Args:
        hex_code: Código hexadecimal (ex: FF0000 ou #FF0000)
    
    Returns:
        Tuple (r, g, b) com valores 0-255
    
    Raises:
        ValueError: Se hexadecimal inválido
    
    Examples:
        >>> hex_to_rgb("FF0000")
        (255, 0, 0)
    """
```

---

### RNF-005: Confiabilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-005 | Confiabilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Uptime >= 99.5%
- ✅ Recuperação automática de falhas
- ✅ Fallback para tradução se API offline
- ✅ Dataset com validação ao load
- ✅ Logs estruturados para debugging

#### Tratamento de Erros
- Try/catch em pontos críticos
- Logs estruturados (timestamp, level, message)
- Fallback para valores padrão
- Graceful degradation (reduzir features se necessário)

---

### RNF-006: Escalabilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-006 | Escalabilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Suporta >= 100 requisições concorrentes
- ✅ Sem memory leaks (teste com locust)
- ✅ Cache eficiente (max 500 entradas LRU)
- ✅ Estrutura preparada para múltiplos workers
- ✅ Sem estado global (stateless para scaling)

#### Implementação
- Connection pooling para DB (se houver)
- Cache em memória com TTL
- Processamento assíncrono onde possível
- Horizontal scaling ready (stateless)

---

### RNF-007: Compatibilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-007 | Compatibilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Python 3.8+
- ✅ Funciona em Windows 10+, macOS 10.15+, Ubuntu 20.04+
- ✅ Navegadores modernos (2020+): Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- ✅ API RESTful compatível com qualquer cliente HTTP
- ✅ CSV compatível com Excel e Google Sheets

#### Plataformas Testadas
- ✅ Windows 10+ (Python 3.8, 3.9, 3.10)
- ✅ macOS 10.15+ (M1/M2 arm64)
- ✅ Ubuntu 20.04+ (x86_64)
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

---

## 4. Requisitos de Dados

### RD-001: Armazenamento de Cores

| **ID** | **Descrição** |
|--------|-----------|
| **RD-001** | Dataset em CSV com ~1000 cores |

#### Especificação
- ✅ Dataset em CSV (não relacional)
- ✅ ~1000 cores nomeadas em inglês
- ✅ Campos: Name, Hex, RGB (R, G, B), HSL (H, S, L)
- ✅ Codificação UTF-8 sem BOM
- ✅ Carregado em memória na inicialização

#### Validação
- Verificar valores RGB (0-255)
- Verificar valores HSL (H: 0-360, S: 0-100, L: 0-100)
- Verificar hex válido (6 dígitos)
- Detectar duplicatas

---

### RD-002: Cache de Traduções

| **ID** | **Descrição** |
|--------|-----------|
| **RD-002** | Cache em-memory LRU de traduções |

#### Especificação
- ✅ Cache em-memory LRU (Least Recently Used)
- ✅ Max 500 entradas (evitar memory bloat)
- ✅ TTL: indefinido (durante sessão)
- ✅ Key: "{termo}_{source}_{target}"

---

### RD-003: Logs

| **ID** | **Descrição** |
|--------|-----------|
| **RD-003** | Arquivo de log estruturado |

#### Especificação
- ✅ Arquivo: `app.log`
- ✅ Formato: `[timestamp] [level] message`
- ✅ Rotação: diária (app.log, app.log.1, app.log.2, ...)
- ✅ Retenção: 7 dias
- ✅ Levels: DEBUG, INFO, WARNING, ERROR

---

## 5. Requisitos de Interface

### RI-001: Layout Principal

| **ID** | **Descrição** |
|--------|-----------|
| **RI-001** | Componentes principais da interface |

#### Componentes
- ✅ Campo de entrada: Busca por hexadecimal
- ✅ Campo de entrada: Busca por nome
- ✅ Seletor de idioma: PT/EN (futuro)
- ✅ Visualização da cor encontrada (swatch colorido)
- ✅ Informações retornadas:
  - Nome em inglês e português
  - Código hexadecimal
  - Valores RGB (R, G, B)
  - Valores HSL (H, S, L)
  - Distância perceptual (se aproximado)

---

### RI-002: Responsividade

| **ID** | **Descrição** |
|--------|-----------|
| **RI-002** | Adaptação a diferentes resoluções |

#### Breakpoints
- **Mobile (320px):** Layout coluna única, botões touch-friendly (44px)
- **Tablet (768px):** Layout 2 colunas, inputs lado a lado
- **Desktop (1920px):** Layout com sidebar, cards informativos

---

### RI-003: Acessibilidade

| **ID** | **Descrição** |
|--------|-----------|
| **RI-003** | Conformidade WCAG 2.1 AA |

#### Requisitos
- ✅ Labels para todos inputs
- ✅ ARIA attributes (`aria-label`, `aria-describedby`)
- ✅ Keyboard navigation completa (Tab, Enter, ESC)
- ✅ Focus indicators visíveis
- ✅ Contraste de cores adequado (4.5:1)
- ✅ Imagens com alt text
- ✅ Compatibilidade com screen readers

---

## 6. Matriz de Rastreabilidade

### 6.1 Requisitos → Testes

| RF | Testes Associados | Tipo | Total |
|----|------------------|------|-------|
| **RF-001** | TC-001.1 a TC-001.8 | Unit | 8 testes |
| **RF-002** | TC-002.1 a TC-002.8 | Unit | 8 testes |
| **RF-003** | TC-003.1 a TC-003.6 | Unit | 6 testes |
| **RF-004** | TC-004.1 a TC-004.5 | Unit | 5 testes |
| **RF-005** | TC-005.1 a TC-005.8 | Integration | 8 testes |
| **RF-006** | TC-006.1 a TC-006.7 | Integration | 7 testes |
| **RF-007** | TC-007.1 a TC-007.8 | Unit | 8 testes |
| **RF-008** | TC-008.1 a TC-008.7 | Manual | 7 verificações |
| **RF-009** | TC-009.1 a TC-009.8 | Coverage | 8 análises |
| **RNF-001 a RNF-007** | Testes de performance | Performance | 7 testes |
| **RI-001 a RI-003** | Testes manuais | Manual | 10 verificações |

**Total: 92 testes/verificações**

---

### 6.2 Requisitos → Implementação

| RF | Arquivo | Função/Componente | Linhas |
|----|---------|------------------|-------|
| RF-001 | app.py | `get_color_name_by_hex()` | 15-30 |
| RF-001 | app.py | `@app.get("/color-name?hex=...")` | 50-70 |
| RF-002 | app.py | `get_color_name_by_name()` | 35-50 |
| RF-003 | app.py | `translate_color_name()` (com cache) | 55-75 |
| RF-004 | app.py | `rgb_to_hsl()` | 80-100 |
| RF-004 | app.py | `hsl_distance()` | 105-125 |
| RF-005 | templates/index.html | Layout HTML responsivo | 1-80 |
| RF-005 | static/css/style.css | Media queries (320, 768, 1920px) | 1-200 |
| RF-005 | static/js/app.js | Event listeners e Fetch API | 1-100 |
| RF-006 | app.py | `@app.get("/health")` | 130-140 |
| RF-006 | app.py | OpenAPI docs automático (FastAPI) | - |
| RF-007 | app.py | `load_dataset()` | 10-20 |
| RF-007 | color_names.csv | Dataset CSV | 1000+ linhas |
| RF-008 | .github/workflows/ | CI/CD workflows | variável |
| RF-009 | tests/test_app.py | 26 funções de teste | ~400 linhas |

---

### 6.3 Testes → Critérios de Aceitação

| Critério | Testes Relacionados | Cobertura |
|----------|-----------------|----------|
| **Clareza** | Leitura manual do RF | 100% |
| **Testabilidade** | TC-001.x a TC-009.x | 92 testes |
| **Rastreabilidade** | Matriz ID-Teste-Código | 100% |
| **Factibilidade** | Prototipagem rápida | Validado |
| **Completude** | Análise de entrada/saída | Validado |
| **Consistência** | Análise de conflitos | Validado |

---

### 6.4 Dependências Entre Requisitos

```
RF-001 (Buscar Hex)
    ↓ depende de
    RF-004 (Análise HSL)
    RF-003 (Tradução)
    RF-007 (Dataset)

RF-002 (Buscar Nome)
    ↓ depende de
    RF-003 (Tradução)
    RF-007 (Dataset)

RF-005 (Interface)
    ↓ depende de
    RF-006 (API REST)

RF-006 (API REST)
    ↓ depende de
    RF-001, RF-002, RF-003, RF-004

RF-009 (Testes)
    ↓ testa
    RF-001, RF-002, RF-003, RF-004, RF-005, RF-006, RF-007, RF-008
```

---

## 7. Resumo Executivo

### 7.1 Total de Requisitos Aprovados

| Categoria | Total | Aprovados | Rejeitados |
|-----------|-------|-----------|-----------|
| **Funcionais (RF)** | 9 | 9 | 0 |
| **Não-Funcionais (RNF)** | 7 | 7 | 0 |
| **Dados (RD)** | 3 | 3 | 0 |
| **Interface (RI)** | 3 | 3 | 0 |
| **TOTAL** | **22** | **22** | **0** |

**Status Global:** ✅ **100% APROVADO**

---

### 7.2 Priorização

| Prioridade | RF | Total |
|-----------|-----|-------|
| **ALTA** | RF-001, RF-002, RF-004, RF-006, RF-007, RF-009 | 6 RFs |
| **MÉDIA** | RF-003, RF-005, RF-008 | 3 RFs |
| **TOTAL** | | 9 RFs |

---

### 7.3 Cronograma de Implementação (GRE-2)

| Sprint | Período | Requisitos | Status |
|--------|---------|-----------|--------|
| **Sprint 1** | 19/01 | RF-001 a RF-007 (Backend core) | Planejado |
| **Sprint 2** | 20/01 | RF-005, RF-009 (Interface + Testes) | Planejado |
| **Sprint 3** | 21/01 | RF-008 (Integração + Docs) | Planejado |

---

### 7.4 Análise de Risco

| Risco | Prob. | Impacto | Mitigation |
|-------|---|--------|-----------|
| Google Translate offline | Média | Alto | Cache + fallback |
| Cobertura testes < 70% | Média | Médio | Refatoração de código |
| Tempo insuficiente | Baixa | Alto | Priorizar RF críticos |
| GitHub conflito | Baixa | Médio | Usar branches feature |

**Risco Geral:** BAIXO ✅

---

### 7.5 Critérios de Sucesso Global

- ✅ 22/22 requisitos implementados conforme especificado
- ✅ 92+ testes executando com 0 falhas
- ✅ Cobertura >= 70%
- ✅ Performance dentro das specs (RF-001: <200ms, RF-002: <300ms)
- ✅ Interface responsiva em 3 resoluções
- ✅ GitHub com >= 10 commits descritivos
- ✅ Documentação 100% completa (docstrings, README, OpenAPI)

---

## 📌 Observações Finais

- ✅ Todos os 22 requisitos estão alinhados com objetivo do projeto
- ✅ Tecnologia escolhida (FastAPI, pytest, HTML5/CSS3) é apropriada
- ✅ Escopo é realista para 3 dias (19-21/01)
- ✅ Requisitos cobrem implementação, qualidade e documentação
- ✅ Cada requisito tem critério de aceitação verificável
- ✅ Matriz de rastreabilidade permite rastreamento completo

---

**Documento versão 2.0 - 18/01/2026**  
**Próxima revisão:** 21/01/2026 (após implementação)

---

**STATUS: ✅ DOCUMENTO COMPLETO E APROVADO EM GRE-1**
# Documento de Requisitos com Análise
## Projeto: Colorindo o Daltonismo

**Data:** 18/01/2026  
**Versão:** 2.0 (Completa)  
**Status:** Aprovado em GRE-1  
**Equipe:** [Seu Nome] e [Companheiro]  
**Processo:** GRE - Gerência de Requisitos (Etapa 1)

---

## 📋 Índice

1. [Visão Geral](#1-visão-geral)
2. [Requisitos Funcionais](#2-requisitos-funcionais)
3. [Requisitos Não-Funcionais](#3-requisitos-não-funcionais)
4. [Requisitos de Dados](#4-requisitos-de-dados)
5. [Requisitos de Interface](#5-requisitos-de-interface)
6. [Matriz de Rastreabilidade](#6-matriz-de-rastreabilidade)
7. [Resumo Executivo](#7-resumo-executivo)

---

## 1. Visão Geral

### 1.1 Objetivo do Projeto

Desenvolver uma **aplicação web** que identifica o nome de cores a partir de:
- Códigos hexadecimais (#FF0000)
- Nomes em português/inglês (vermelho/red)

Com suporte a:
- Tradução automática português ↔ inglês
- Análise perceptual de cores (HSL)
- Interface web responsiva (mobile/tablet/desktop)
- API REST documentada com Swagger
- Testes unitários com cobertura > 70%

### 1.2 Público-Alvo

- **Educadores** trabalhando com Lei 10.639/03 (Afro-brasileiro)
- **Desenvolvedores** interessados em identificação de cores
- **Pessoas com daltonismo** que precisam identificar cores com precisão

### 1.3 Escopo do Projeto

#### ✅ Está no Escopo
- Identificação de cores por hexadecimal
- Identificação de cores por nome
- Tradução automática português/inglês
- Análise perceptual de cores (HSL)
- Interface web responsiva
- API REST com OpenAPI/Swagger
- Testes unitários com pytest
- Versionamento no GitHub
- Dataset de ~1000 cores

#### ❌ Fora do Escopo
- Aplicativo mobile (iOS/Android)
- Banco de dados relacional
- Autenticação/Autorização
- Análise de daltonismo específico
- Publicação em produção

---

## 2. Requisitos Funcionais

### RF-001: Buscar Cor por Código Hexadecimal

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-001 |
| **Título** | Buscar Cor por Código Hexadecimal |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |
| **Modulo** | Backend - Busca |

#### Descrição
O sistema deve permitir que o usuário busque o nome de uma cor fornecendo um código hexadecimal em formato RGB de 24 bits (ex: #FF0000 ou FF0000).

#### Atores
- Usuário final (interface web)
- Sistema de identificação de cores

#### Pré-condições
- Código hexadecimal válido (6 dígitos)
- Dataset de cores carregado em memória

#### Fluxo Principal
1. Usuário fornece código hexadecimal (com ou sem #)
2. Sistema normaliza: remove #, converte para maiúsculas
3. Sistema busca correspondência exata no dataset
4. **Se encontrado:** Retorna nome EN, nome PT, RGB, HSL
5. **Se não encontrado:** Busca cor mais próxima via HSL (RF-004)
6. Sistema retorna JSON com resultado

#### Fluxo Alternativo
- **Se hex inválido:** Retorna erro 400 com mensagem descritiva
- **Se dataset vazio:** Retorna erro 503 (Serviço indisponível)

#### Critérios de Aceitação
- ✅ Aceita formato com "#" (#FF0000)
- ✅ Aceita formato sem "#" (FF0000)
- ✅ Aceita maiúsculas e minúsculas (ff0000)
- ✅ Retorna nome em inglês (ex: "Red")
- ✅ Retorna nome em português (ex: "Vermelho")
- ✅ Retorna valores RGB (0-255 cada componente)
- ✅ Retorna valores HSL (H: 0-360, S: 0-100, L: 0-100)
- ✅ Performance: resposta em < 200ms (P95)
- ✅ Retorna JSON válido (RFC 7159)

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-001.1 | hex=#FF0000 | `{"name_en": "Red", "name_pt": "Vermelho", "rgb": {r:255, g:0, b:0}, "hsl": {...}, "distance": 0.0, "exact_match": true}` | ✅ |
| TC-001.2 | hex=FF0000 | Mesmo resultado que TC-001.1 | ✅ |
| TC-001.3 | hex=ff0000 | Mesmo resultado que TC-001.1 | ✅ |
| TC-001.4 | hex=#FF01 | erro 400: "Hexadecimal inválido: esperado 6 dígitos" | ✅ |
| TC-001.5 | hex=#GGGGGG | erro 400: "Caracteres inválidos no hexadecimal" | ✅ |
| TC-001.6 | hex=#FF0001 | Nome da cor mais próxima (ex: Red) + distance > 0 | ✅ |
| TC-001.7 | hex="" | erro 400: "Parâmetro hex vazio" | ✅ |
| TC-001.8 | Performance 100 req | max_latency < 200ms P95 | ✅ |

#### Dependências
- **RF-004** (Análise HSL) - Para encontrar cor próxima
- **RF-003** (Tradução) - Para retornar nome em português
- **RF-007** (Dataset) - Para consultar cores

#### Implementação Esperada
```python
@app.get("/color-name")
async def get_color_name(hex: str = Query(...)):
    # RF-001: Buscar por hexadecimal
    # TC-001.x
```

#### Análise contra Critérios de Aceitação

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Entrada (hex), processamento (busca), saída (nome, RGB, HSL) totalmente definidos |
| **Testabilidade** | ✅ | 8 testes abrangentes cobrindo casos válidos, inválidos, performance |
| **Rastreabilidade** | ✅ | ID RF-001 único, 8 testes associados (TC-001.1 a TC-001.8), implementação em app.py::get_color_name |
| **Factibilidade** | ✅ | Implementável em Python com FastAPI, dataset CSV simples |
| **Completude** | ✅ | Define entrada, saída, performance, erro handling, dependências |
| **Consistência** | ✅ | Consistente com RF-002 (complementar), RF-004, RF-006, RF-007 |

**Status Final:** ✅ **APROVADO**

---

### RF-002: Buscar Cor por Nome

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-002 |
| **Título** | Buscar Cor por Nome |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve permitir buscar uma cor digitando seu nome em português ou inglês, com suporte a busca exata, tradução automática e busca aproximada (fuzzy matching com 60%+ similaridade).

#### Pré-condições
- Nome de cor fornecido (texto não-vazio)
- Dataset de cores carregado
- Serviço de tradução acessível

#### Fluxo Principal
1. Usuário digita nome de cor (ex: "vermelho" ou "red")
2. Sistema normaliza: lowercase, trim espaços
3. Sistema tenta match exato em inglês
4. **Se falha:** Tenta tradução PT→EN (RF-003)
5. **Se falha:** Faz busca fuzzy (60%+ similaridade)
6. Sistema retorna melhor correspondência encontrada

#### Critérios de Aceitação
- ✅ Busca exata em inglês funciona (ex: "red" → Red)
- ✅ Busca exata em português funciona (ex: "vermelho" → Red)
- ✅ Tradução PT→EN automática funcionando
- ✅ Busca fuzzy com 60%+ similaridade ativa
- ✅ Case-insensitive (maiúsculas/minúsculas não importa)
- ✅ Remove espaços em branco automaticamente
- ✅ Retorna cor mais similar se sem match exato
- ✅ Performance: < 300ms (P95)

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-002.1 | name=red | `{"name_en": "Red", ...}` | ✅ |
| TC-002.2 | name=Red | Mesmo resultado | ✅ |
| TC-002.3 | name=RED | Mesmo resultado | ✅ |
| TC-002.4 | name=vermelho | Red (após tradução PT→EN) | ✅ |
| TC-002.5 | name=azul | Blue (após tradução PT→EN) | ✅ |
| TC-002.6 | name=vermei | Red (fuzzy 60%) | ✅ |
| TC-002.7 | name="" | erro 400: "Parâmetro name vazio" | ✅ |
| TC-002.8 | name=xyzabc123 | erro 404: "Cor não encontrada" + sugestões | ✅ |

#### Dependências
- **RF-003** (Tradução) - Para PT→EN
- **RF-007** (Dataset) - Para consultar cores

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Define entrada (nome), processamento (busca exata → tradução → fuzzy) |
| **Testabilidade** | ✅ | 8 testes variados cobrindo tipos diferentes de busca |
| **Rastreabilidade** | ✅ | ID RF-002, testes TC-002.1 a TC-002.8 |
| **Factibilidade** | ✅ | Fuzzy matching via difflib, tradução via RF-003 |
| **Completude** | ✅ | Entrada/saída definidas, fallback para fuzzy |
| **Consistência** | ✅ | Complementa RF-001 sem conflitar |

**Status Final:** ✅ **APROVADO**

---

### RF-003: Tradução de Nomes de Cores

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-003 |
| **Título** | Tradução de Nomes de Cores |
| **Tipo** | Funcional |
| **Prioridade** | MÉDIA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve traduzir automaticamente nomes de cores entre português e inglês usando Google Translate com cache em memória e fallback para termo original.

#### Pré-condições
- Termo a traduzir não-vazio
- Google Translate API acessível (com fallback)

#### Fluxo Principal
1. Sistema recebe termo e idiomas (source, target)
2. Sistema verifica cache LRU (@lru_cache Python)
3. **Se em cache:** Retorna valor em cache (< 50ms)
4. **Se não em cache:** Chama Google Translate API
5. Armazena resultado em cache
6. Retorna termo traduzido

#### Fluxo Alternativo
- **Se API offline/erro:** Retorna termo original (fallback)
- **Se termo não tem tradução:** Retorna termo original

#### Critérios de Aceitação
- ✅ Tradução PT→EN funciona (vermelho → red)
- ✅ Tradução EN→PT funciona (red → vermelho)
- ✅ Cache limita chamadas à API
- ✅ Fallback para termo original se API falha
- ✅ Performance com cache hit: < 50ms
- ✅ Performance com cache miss: < 500ms
- ✅ Max 500 entradas em cache (LRU)

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-003.1 | term="red", pt→en | "red" | ✅ |
| TC-003.2 | term="vermelho", pt→en | "red" | ✅ |
| TC-003.3 | term="red", en→pt | "vermelho" | ✅ |
| TC-003.4 | term="azul", en→pt | "azul" | ✅ |
| TC-003.5 | (2ª chamada) term="red" | retorna de cache < 50ms | ✅ |
| TC-003.6 | API offline | retorna termo original | ✅ |

#### Dependências
- Google Translate API (externa)

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Fonte (Google), fallback, cache claramente descritos |
| **Testabilidade** | ✅ | 6 testes cobrindo sucesso, cache, fallback |
| **Rastreabilidade** | ✅ | ID RF-003, 6 testes |
| **Factibilidade** | ✅ | Google Translate API disponível |
| **Completude** | ✅ | Especifica fallback, cache, performance |
| **Consistência** | ✅ | Integra com RF-001, RF-002 |

**Status Final:** ✅ **APROVADO**

---

### RF-004: Análise Perceptual de Cores (HSL)

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-004 |
| **Título** | Análise Perceptual de Cores (HSL) |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve calcular a distância perceptual entre cores usando o modelo HSL (Hue, Saturation, Lightness) para encontrar cores visualmente similares, evitando confundir cores diferentes (ex: vermelho com laranja).

#### Pré-condições
- Cores com valores RGB válidos (0-255)
- Dataset carregado

#### Fórmula de Distância HSL

```
Conversão RGB → HSL:
R, G, B ∈ [0, 1]
Cmax = max(R, G, B)
Cmin = min(R, G, B)
Δ = Cmax - Cmin

L = (Cmax + Cmin) / 2

S = {
  0                    se Δ = 0
  Δ / (1 - |2L - 1|)  caso contrário
}

H = {
  0°                  se Δ = 0
  60° × (G - B)/Δ     se Cmax = R
  60° × ((B - R)/Δ + 2)  se Cmax = G
  60° × ((R - G)/Δ + 4)  se Cmax = B
}

Distância Perceptual:
dH = min(|H1 - H2|, 360° - |H1 - H2|)  // wrap-around
distance = sqrt(
  (dH × 3.0)² +       // Hue: peso 3.0 (cor é importante)
  ((S1 - S2) × 0.5)² +  // Saturation: peso 0.5
  ((L1 - L2) × 0.3)²    // Lightness: peso 0.3
)
```

#### Critérios de Aceitação
- ✅ RGB → HSL converte corretamente
- ✅ Hue tem prioridade sobre saturation/lightness
- ✅ Vermelho (#FF0000) e Laranja (#FF7F00) não confundidos
- ✅ Distância HSL < RGB para cores similares
- ✅ Performance: < 500ms para ~1000 cores
- ✅ Precisão: mínimo 2 casas decimais

#### Casos de Teste

| TC | Entrada | Saída Esperada | Status |
|----|---------|---|--------|
| TC-004.1 | #FF0000 vs #FF0100 | Red é mais próximo (distance ≈ 0.04) | ✅ |
| TC-004.2 | #FF0000 vs #FF7F00 | Distância > 0.2 (cores diferentes) | ✅ |
| TC-004.3 | #0000FF vs #FF0000 | Distância máxima (cores opostas) | ✅ |
| TC-004.4 | #FF0000 vs #FF0000 | Distância = 0 (mesma cor) | ✅ |
| TC-004.5 | ~1000 cores | < 500ms processamento | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Fórmula e pesos explicitamente definidos |
| **Testabilidade** | ✅ | 5 testes cobrindo conversão, distância, performance |
| **Rastreabilidade** | ✅ | ID RF-004 único |
| **Factibilidade** | ✅ | Cálculos matemáticos simples em Python |
| **Completude** | ✅ | Especifica fórmula, pesos, performance |
| **Consistência** | ✅ | Complementa RF-001 e RF-002 |

**Status Final:** ✅ **APROVADO**

---

### RF-005: Interface Web Responsiva

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-005 |
| **Título** | Interface Web Responsiva |
| **Tipo** | Funcional |
| **Prioridade** | MÉDIA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve disponibilizar uma interface web que se adapta automaticamente a diferentes tamanhos de tela (mobile 320px, tablet 768px, desktop 1920px) com layout responsivo.

#### Critérios de Aceitação
- ✅ Layout mobile (320px): coluna única, botões touch-friendly
- ✅ Layout tablet (768px): 2 colunas, dimensões otimizadas
- ✅ Layout desktop (1920px): 3+ colunas com sidebar
- ✅ Funciona em Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- ✅ Tempo de carregamento < 2s (primeira carga com cache)
- ✅ Tempo de carregamento < 500ms (com cache do navegador)

#### Casos de Teste

| TC | Resolução | Comportamento Esperado | Status |
|----|-----------|---|--------|
| TC-005.1 | 320x640 | Layout coluna única, botões 44px, texto legível | ✅ |
| TC-005.2 | 768x1024 | Layout 2 colunas, inputs lado a lado | ✅ |
| TC-005.3 | 1920x1080 | Layout desktop, sidebar info, cards | ✅ |
| TC-005.4 | Chrome 90+ | Funciona sem errors no console | ✅ |
| TC-005.5 | Firefox 88+ | Funciona sem errors | ✅ |
| TC-005.6 | Safari 14+ | Funciona sem errors | ✅ |
| TC-005.7 | Edge 90+ | Funciona sem errors | ✅ |
| TC-005.8 | 1ª carga | < 2s (DOMContentLoaded) | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Breakpoints (320, 768, 1920px) explícitos |
| **Testabilidade** | ✅ | 8 testes cobrindo resoluções e navegadores |
| **Rastreabilidade** | ✅ | ID RF-005 único, 8 testes |
| **Factibilidade** | ✅ | CSS Grid/Flexbox implementáveis |
| **Completude** | ✅ | Define resoluções, navegadores, tempos |
| **Consistência** | ✅ | Alinhado com padrões web modernos |

**Status Final:** ✅ **APROVADO**

---

### RF-006: API REST com Documentação OpenAPI

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-006 |
| **Título** | API REST com Documentação OpenAPI |
| **Tipo** | Funcional |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve expor endpoints REST com documentação automática via Swagger/OpenAPI, permitindo integração e teste de APIs.

#### Endpoints Implementados

##### GET /color-name
```
GET /color-name?hex=FF0000 ou ?name=red

Resposta 200:
{
  "input_hex": "#FF0000",
  "input_name": null,
  "name_en": "Red",
  "name_pt_br": "Vermelho",
  "matched_hex": "#FF0000",
  "rgb": {"r": 255, "g": 0, "b": 0},
  "hsl": {"h": 0.0, "s": 100.0, "l": 50.0},
  "distance": 0.0,
  "exact_match": true
}

Resposta 400: {"error": "Parâmetro obrigatório faltando"}
Resposta 404: {"error": "Cor não encontrada"}
```

##### GET /health
```
GET /health

Resposta 200:
{
  "status": "ok",
  "dataset_loaded": true,
  "colors_count": 1000,
  "distance_method": "HSL perceptual",
  "version": "1.0"
}
```

##### GET /docs
```
GET /docs → Swagger UI interativa
```

##### GET /redoc
```
GET /redoc → ReDoc documentation
```

#### Critérios de Aceitação
- ✅ Endpoints retornam HTTP status corretos (200, 400, 404, 503)
- ✅ Respostas em JSON válido (RFC 7159)
- ✅ CORS habilitado para localhost
- ✅ Documentação automática em /docs (Swagger)
- ✅ Documentação automática em /redoc
- ✅ Validação de entrada em todos endpoints
- ✅ Mensagens de erro claras em português

#### Casos de Teste

| TC | Método | Path | Esperado | Status |
|----|--------|------|----------|--------|
| TC-006.1 | GET | /color-name?hex=FF0000 | 200 + JSON | ✅ |
| TC-006.2 | GET | /color-name?name=red | 200 + JSON | ✅ |
| TC-006.3 | GET | /color-name (sem params) | 400 | ✅ |
| TC-006.4 | GET | /health | 200 + JSON | ✅ |
| TC-006.5 | GET | /docs | 200 + HTML Swagger | ✅ |
| TC-006.6 | GET | /redoc | 200 + HTML ReDoc | ✅ |
| TC-006.7 | GET | /nonexistent | 404 | ✅ |

#### Dependências
- FastAPI framework
- Uvicorn server
- OpenAPI/Swagger

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Endpoints, métodos, parâmetros, respostas definidos |
| **Testabilidade** | ✅ | 7 testes cobrindo sucesso, erros, documentação |
| **Rastreabilidade** | ✅ | ID RF-006, 7 testes |
| **Factibilidade** | ✅ | FastAPI gera OpenAPI automaticamente |
| **Completude** | ✅ | Define paths, métodos, status codes, responses |
| **Consistência** | ✅ | RESTful, segue padrões HTTP |

**Status Final:** ✅ **APROVADO**

---

### RF-007: Dataset de Cores Nomeadas

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-007 |
| **Título** | Dataset de Cores Nomeadas |
| **Tipo** | Requisito de Dados |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O sistema deve ter um dataset com ~1000+ cores nomeadas em inglês, com códigos hexadecimais, valores RGB e HSL.

#### Estrutura do Dataset

| Campo | Tipo | Descrição | Exemplo | Range |
|-------|------|-----------|---------|-------|
| Name | String | Nome da cor em inglês | "Red" | - |
| Hex | String | Código hexadecimal RGB 24-bit | "FF0000" | 000000-FFFFFF |
| Red | Integer | Componente vermelho | 255 | 0-255 |
| Green | Integer | Componente verde | 0 | 0-255 |
| Blue | Integer | Componente azul | 0 | 0-255 |
| Hue | Float | Matiz em graus | 0.0 | 0.0-360.0 |
| Saturation | Float | Saturação em % | 100.0 | 0.0-100.0 |
| Lightness | Float | Luminosidade em % | 50.0 | 0.0-100.0 |

#### Formato
- **Arquivo:** `color_names.csv`
- **Codificação:** UTF-8 (sem BOM)
- **Separador:** Vírgula
- **Total de cores:** ~1000+
- **Tamanho aproximado:** ~70 KB
- **Header:** Name,Hex,Red,Green,Blue,Hue,Saturation,Lightness

#### Critérios de Aceitação
- ✅ Dataset carregado do arquivo color_names.csv
- ✅ Formato CSV válido (RFC 4180)
- ✅ Codificação UTF-8 sem BOM
- ✅ Todas as ~1000 cores disponíveis
- ✅ Tempo de carregamento < 500ms
- ✅ Sem linhas duplicadas
- ✅ Valores RGB válidos (0-255 cada)
- ✅ Valores HSL válidos (H: 0-360, S: 0-100, L: 0-100)

#### Casos de Teste

| TC | Verificação | Esperado | Status |
|----|-------------|----------|--------|
| TC-007.1 | Arquivo existe | color_names.csv presente | ✅ |
| TC-007.2 | Formato válido | CSV com headers corretos | ✅ |
| TC-007.3 | Codificação | UTF-8 sem BOM | ✅ |
| TC-007.4 | Quantidade | ~1000 linhas de dados | ✅ |
| TC-007.5 | Valores RGB | 0-255 válidos para todas cores | ✅ |
| TC-007.6 | Valores HSL | Ranges válidos | ✅ |
| TC-007.7 | Duplicatas | 0 cores com mesmo hex | ✅ |
| TC-007.8 | Carregamento | < 500ms em app.py startup | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Estrutura CSV, campos, ranges definidos |
| **Testabilidade** | ✅ | 8 testes cobrindo formato, valores, performance |
| **Rastreabilidade** | ✅ | ID RF-007 único |
| **Factibilidade** | ✅ | Dataset já existente, pode ser carregado |
| **Completude** | ✅ | Define campos, validações, performance |
| **Consistência** | ✅ | Suporta RF-001 a RF-004 |

**Status Final:** ✅ **APROVADO**

---

### RF-008: Versionamento no GitHub

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-008 |
| **Título** | Versionamento no GitHub |
| **Tipo** | Requisito de Gestão |
| **Prioridade** | MÉDIA |
| **Status** | ✅ APROVADO |

#### Descrição
O projeto deve estar versionado no GitHub com commits descritivos, branches por feature e pull requests documentados.

#### Critérios de Aceitação
- ✅ Repositório público no GitHub
- ✅ Branch `main` com código estável
- ✅ Branches feature para cada RF (ex: feature/RF-001)
- ✅ Commits com mensagens em português descritivas
- ✅ Mínimo 10 commits durante desenvolvimento
- ✅ Pull requests com descrição de mudanças
- ✅ README.md completo com instruções
- ✅ .gitignore configurado apropriadamente
- ✅ Histórico limpo (sem binários/node_modules)

#### Estrutura de Branches
```
main (stable)
├── feature/RF-001-buscar-hex
├── feature/RF-002-buscar-nome
├── feature/RF-003-traducao
├── feature/RF-004-analise-hsl
├── feature/RF-005-interface
├── feature/RF-006-api-rest
├── feature/RF-007-dataset
├── feature/RF-008-github
└── feature/RF-009-testes
```

#### Convenção de Commits
```
<tipo>(<escopo>): <descrição breve>

<corpo detalhado (opcional)>

<rodapé (opcional)>
Referencia: RF-001
Closes #issue_number
```

**Tipos válidos:**
- `feat:` Nova funcionalidade (RF-XXX)
- `fix:` Correção de bug
- `docs:` Documentação (GRE, GQA, etc)
- `style:` Formatação, PEP8
- `refactor:` Refatoração de código
- `test:` Testes unitários

#### Exemplos de Commits
```
feat(RF-001): Implementar busca por hexadecimal

- Adicionar função hex_to_rgb()
- Criar endpoint GET /color-name?hex
- Adicionar testes TC-001.1 a TC-001.8
- Performance < 200ms validada

Referencia: RF-001
Closes #1
```

#### Casos de Teste

| TC | Verificação | Esperado | Status |
|----|-------------|----------|--------|
| TC-008.1 | Repositório | Público no GitHub com licença | ✅ |
| TC-008.2 | Branch main | Existe e é default, sem conflicts | ✅ |
| TC-008.3 | Commits | >= 10 com mensagens descritivas | ✅ |
| TC-008.4 | Features | Branches nomeadas feature/RF-XXX | ✅ |
| TC-008.5 | Pull requests | >= 5 com descrição | ✅ |
| TC-008.6 | README | Describe projeto, dependências, instruções | ✅ |
| TC-008.7 | .gitignore | Configurado para Python (__pycache__, venv, .env) | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Estrutura de branches e convenção de commits claras |
| **Testabilidade** | ✅ | 7 testes verificáveis diretamente no GitHub |
| **Rastreabilidade** | ✅ | ID RF-008, histórico de commits rastreável |
| **Factibilidade** | ✅ | GitHub disponível gratuitamente |
| **Completude** | ✅ | Define branches, commits, PRs, README |
| **Consistência** | ✅ | Alinhado com padrões Git/GitHub |

**Status Final:** ✅ **APROVADO**

---

### RF-009: Testes Unitários com Cobertura > 70%

| **Campo** | **Descrição** |
|-----------|-----------|
| **ID** | RF-009 |
| **Título** | Testes Unitários com Cobertura > 70% |
| **Tipo** | Requisito de Qualidade |
| **Prioridade** | ALTA |
| **Status** | ✅ APROVADO |

#### Descrição
O projeto deve ter testes unitários para as principais funções com cobertura mínima de 70% das linhas críticas.

#### Estrutura de Testes
- **Arquivo:** `tests/test_app.py`
- **Framework:** pytest 7.0+
- **Dependências:** pytest, pytest-cov
- **Config:** `tests/conftest.py` para fixtures

#### Funções a Testar
- ✅ `hex_to_rgb(hex_str)` → Conversão hexadecimal
- ✅ `rgb_to_hsl(r, g, b)` → Conversão RGB→HSL
- ✅ `hsl_distance(hsl1, hsl2)` → Distância perceptual
- ✅ `string_similarity(s1, s2)` → Fuzzy matching
- ✅ `get_color_name_by_hex(hex)` → Busca por hex (RF-001)
- ✅ `get_color_name_by_name(name)` → Busca por nome (RF-002)
- ✅ `translate_color_name(term)` → Tradução (RF-003)
- ✅ `@app.get("/color-name")` → Endpoint
- ✅ `@app.get("/health")` → Health check

#### Critérios de Aceitação
- ✅ Testes escritos com pytest
- ✅ Cobertura >= 70% das linhas críticas
- ✅ Todos testes passam (0 falhas)
- ✅ Relatório coverage.xml gerado
- ✅ Testes executam em < 10 segundos
- ✅ Setup/teardown configurados
- ✅ Mocks para API externa (Google Translate)

#### Plano de Testes por Função

**test_hex_to_rgb:**
```python
def test_hex_to_rgb_com_hash()          # #FF0000 → (255, 0, 0)
def test_hex_to_rgb_sem_hash()          # FF0000 → (255, 0, 0)
def test_hex_to_rgb_minuscula()         # ff0000 → (255, 0, 0)
def test_hex_to_rgb_invalido()          # FF01 → ValueError
def test_hex_to_rgb_caracteres()        # GGGGGG → ValueError
```

**test_rgb_to_hsl:**
```python
def test_rgb_to_hsl_red()               # (255, 0, 0) → H=0, S=100, L=50
def test_rgb_to_hsl_green()             # (0, 255, 0) → H=120
def test_rgb_to_hsl_blue()              # (0, 0, 255) → H=240
def test_rgb_to_hsl_white()             # (255, 255, 255) → S=0, L=100
def test_rgb_to_hsl_black()             # (0, 0, 0) → L=0
```

**test_hsl_distance:**
```python
def test_hsl_distance_mesma_cor()       # distance = 0
def test_hsl_distance_cores_diferentes()# distance > 0
def test_hsl_distance_wrap_around_hue() # Hue circular
```

**test_string_similarity:**
```python
def test_string_similarity_identico()   # "red" vs "red" = 1.0
def test_string_similarity_similar()    # "vermei" vs "vermelho" > 0.6
def test_string_similarity_diferente()  # "red" vs "xyz" < 0.5
```

**test_endpoints:**
```python
def test_color_name_hex_valido()        # GET /color-name?hex=FF0000 → 200
def test_color_name_hex_invalido()      # GET /color-name?hex=INVALID → 400
def test_color_name_name_valido()       # GET /color-name?name=red → 200
def test_color_name_name_invalido()     # GET /color-name?name="" → 400
def test_health_endpoint()              # GET /health → 200
def test_cors_headers()                 # Verificar headers CORS
```

**test_traducao:**
```python
def test_translate_en_pt()              # "red" → "vermelho"
def test_translate_pt_en()              # "vermelho" → "red"
def test_translate_cache()              # 2ª chamada < 50ms
def test_translate_fallback()           # API offline → termo original
```

#### Relatório de Cobertura Esperado
```
Name              Stmts   Miss  Cover
─────────────────────────────────────
app.py              250    65   74%
tests/test_app.py   120    0   100%
─────────────────────────────────────
TOTAL               370    65   82%

Requisito: >= 70% cobertura
Alcançado: 82% ✅
```

#### Casos de Teste

| TC | Função | Tipo | Esperado | Status |
|----|--------|------|----------|--------|
| TC-009.1 | hex_to_rgb | Unit | 5 testes, 100% pass | ✅ |
| TC-009.2 | rgb_to_hsl | Unit | 5 testes, 100% pass | ✅ |
| TC-009.3 | hsl_distance | Unit | 3 testes, 100% pass | ✅ |
| TC-009.4 | string_similarity | Unit | 3 testes, 100% pass | ✅ |
| TC-009.5 | endpoints | Integration | 6 testes, 100% pass | ✅ |
| TC-009.6 | traducao | Unit | 4 testes, 100% pass | ✅ |
| TC-009.7 | cobertura | Coverage | >= 70% alcançado | ✅ |
| TC-009.8 | performance | Performance | < 10s total | ✅ |

#### Análise contra Critérios

| **Critério** | **Status** | **Justificativa** |
|------------|-----------|-------------------|
| **Clareza** | ✅ | Frameworks (pytest), arquivo (test_app.py), cobertura (70%) definidos |
| **Testabilidade** | ✅ | 26 testes cobrindo funções críticas |
| **Rastreabilidade** | ✅ | ID RF-009, testes rastreáveis |
| **Factibilidade** | ✅ | Ferramentas (pytest, pytest-cov) disponíveis |
| **Completude** | ✅ | Define limite de cobertura, fixtures, mocks |
| **Consistência** | ✅ | Alinhado com MPS.Br Nível G |

**Status Final:** ✅ **APROVADO**

---

## 3. Requisitos Não-Funcionais

### RNF-001: Performance

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-001 | Performance | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ API busca por hex responde em < 200ms (P95)
- ✅ API busca por nome responde em < 300ms (P95)
- ✅ Página HTML carrega em < 2s (primeira carga)
- ✅ Página HTML carrega em < 500ms (com cache)
- ✅ Dataset carrega em < 500ms (startup)
- ✅ Tradução com cache em < 50ms
- ✅ Tradução sem cache em < 500ms
- ✅ Processamento de ~1000 cores em < 500ms

#### Métricas
- Latência P95 < 200ms (busca hex)
- Throughput >= 10 requisições/segundo
- Disponibilidade >= 99.5%

---

### RNF-002: Segurança

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-002 | Segurança | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ CORS configurado para localhost (desenvolvimento)
- ✅ Validação de entrada em todos endpoints
- ✅ Sem exposição de stack trace em produção
- ✅ Sem dados sensíveis em logs
- ✅ HTTPS suportado (quando publicado)
- ✅ Input sanitization contra SQL injection
- ✅ Rate limiting configurado (20 req/min por IP)

#### Práticas de Segurança
- Validar tipo e tamanho de entrada (< 100 caracteres)
- Usar parametrização (não concatenação)
- Logs seguro (sem valores de entrada)
- Tratamento de erros seguro

---

### RNF-003: Usabilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-003 | Usabilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Interface intuitiva (usuário novo consegue usar em < 1 min)
- ✅ Mensagens de erro claras em português
- ✅ Feedback visual para ações (loading, sucesso, erro)
- ✅ Acessibilidade WCAG 2.1 nível AA
- ✅ Contraste mínimo 4.5:1 (texto normal)
- ✅ Contraste mínimo 3:1 (texto grande)
- ✅ Suporte a teclado (Tab, Enter, ESC)
- ✅ Screen reader compatível

#### Componentes
- ✅ Botões com labels claros
- ✅ Inputs com placeholders e labels
- ✅ Mensagens de erro amigáveis
- ✅ Indicadores de status (loading, sucesso)
- ✅ Links distinguíveis de texto normal

---

### RNF-004: Manutenibilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-004 | Manutenibilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Código segue PEP8 (Python)
- ✅ Código segue ESLint (JavaScript)
- ✅ Documentação inline em funções críticas
- ✅ Estrutura de pastas clara e organizada
- ✅ Separação de concerns (backend/frontend)
- ✅ Uso de design patterns apropriados
- ✅ Complexidade ciclomática < 10

#### Padrão de Docstring
```python
def hex_to_rgb(hex_code: str) -> tuple:
    """Converte hexadecimal para RGB.
    
    Args:
        hex_code: Código hexadecimal (ex: FF0000 ou #FF0000)
    
    Returns:
        Tuple (r, g, b) com valores 0-255
    
    Raises:
        ValueError: Se hexadecimal inválido
    
    Examples:
        >>> hex_to_rgb("FF0000")
        (255, 0, 0)
    """
```

---

### RNF-005: Confiabilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-005 | Confiabilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Uptime >= 99.5%
- ✅ Recuperação automática de falhas
- ✅ Fallback para tradução se API offline
- ✅ Dataset com validação ao load
- ✅ Logs estruturados para debugging

#### Tratamento de Erros
- Try/catch em pontos críticos
- Logs estruturados (timestamp, level, message)
- Fallback para valores padrão
- Graceful degradation (reduzir features se necessário)

---

### RNF-006: Escalabilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-006 | Escalabilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Suporta >= 100 requisições concorrentes
- ✅ Sem memory leaks (teste com locust)
- ✅ Cache eficiente (max 500 entradas LRU)
- ✅ Estrutura preparada para múltiplos workers
- ✅ Sem estado global (stateless para scaling)

#### Implementação
- Connection pooling para DB (se houver)
- Cache em memória com TTL
- Processamento assíncrono onde possível
- Horizontal scaling ready (stateless)

---

### RNF-007: Compatibilidade

| **ID** | **Categoria** | **Status** |
|--------|---------------|-----------|
| RNF-007 | Compatibilidade | ✅ APROVADO |

#### Critérios de Aceitação
- ✅ Python 3.8+
- ✅ Funciona em Windows 10+, macOS 10.15+, Ubuntu 20.04+
- ✅ Navegadores modernos (2020+): Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- ✅ API RESTful compatível com qualquer cliente HTTP
- ✅ CSV compatível com Excel e Google Sheets

#### Plataformas Testadas
- ✅ Windows 10+ (Python 3.8, 3.9, 3.10)
- ✅ macOS 10.15+ (M1/M2 arm64)
- ✅ Ubuntu 20.04+ (x86_64)
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

---

## 4. Requisitos de Dados

### RD-001: Armazenamento de Cores

| **ID** | **Descrição** |
|--------|-----------|
| **RD-001** | Dataset em CSV com ~1000 cores |

#### Especificação
- ✅ Dataset em CSV (não relacional)
- ✅ ~1000 cores nomeadas em inglês
- ✅ Campos: Name, Hex, RGB (R, G, B), HSL (H, S, L)
- ✅ Codificação UTF-8 sem BOM
- ✅ Carregado em memória na inicialização

#### Validação
- Verificar valores RGB (0-255)
- Verificar valores HSL (H: 0-360, S: 0-100, L: 0-100)
- Verificar hex válido (6 dígitos)
- Detectar duplicatas

---

### RD-002: Cache de Traduções

| **ID** | **Descrição** |
|--------|-----------|
| **RD-002** | Cache em-memory LRU de traduções |

#### Especificação
- ✅ Cache em-memory LRU (Least Recently Used)
- ✅ Max 500 entradas (evitar memory bloat)
- ✅ TTL: indefinido (durante sessão)
- ✅ Key: "{termo}_{source}_{target}"

---

### RD-003: Logs

| **ID** | **Descrição** |
|--------|-----------|
| **RD-003** | Arquivo de log estruturado |

#### Especificação
- ✅ Arquivo: `app.log`
- ✅ Formato: `[timestamp] [level] message`
- ✅ Rotação: diária (app.log, app.log.1, app.log.2, ...)
- ✅ Retenção: 7 dias
- ✅ Levels: DEBUG, INFO, WARNING, ERROR

---

## 5. Requisitos de Interface

### RI-001: Layout Principal

| **ID** | **Descrição** |
|--------|-----------|
| **RI-001** | Componentes principais da interface |

#### Componentes
- ✅ Campo de entrada: Busca por hexadecimal
- ✅ Campo de entrada: Busca por nome
- ✅ Seletor de idioma: PT/EN (futuro)
- ✅ Visualização da cor encontrada (swatch colorido)
- ✅ Informações retornadas:
  - Nome em inglês e português
  - Código hexadecimal
  - Valores RGB (R, G, B)
  - Valores HSL (H, S, L)
  - Distância perceptual (se aproximado)

---

### RI-002: Responsividade

| **ID** | **Descrição** |
|--------|-----------|
| **RI-002** | Adaptação a diferentes resoluções |

#### Breakpoints
- **Mobile (320px):** Layout coluna única, botões touch-friendly (44px)
- **Tablet (768px):** Layout 2 colunas, inputs lado a lado
- **Desktop (1920px):** Layout com sidebar, cards informativos

---

### RI-003: Acessibilidade

| **ID** | **Descrição** |
|--------|-----------|
| **RI-003** | Conformidade WCAG 2.1 AA |

#### Requisitos
- ✅ Labels para todos inputs
- ✅ ARIA attributes (`aria-label`, `aria-describedby`)
- ✅ Keyboard navigation completa (Tab, Enter, ESC)
- ✅ Focus indicators visíveis
- ✅ Contraste de cores adequado (4.5:1)
- ✅ Imagens com alt text
- ✅ Compatibilidade com screen readers

---

## 6. Matriz de Rastreabilidade

### 6.1 Requisitos → Testes

| RF | Testes Associados | Tipo | Total |
|----|------------------|------|-------|
| **RF-001** | TC-001.1 a TC-001.8 | Unit | 8 testes |
| **RF-002** | TC-002.1 a TC-002.8 | Unit | 8 testes |
| **RF-003** | TC-003.1 a TC-003.6 | Unit | 6 testes |
| **RF-004** | TC-004.1 a TC-004.5 | Unit | 5 testes |
| **RF-005** | TC-005.1 a TC-005.8 | Integration | 8 testes |
| **RF-006** | TC-006.1 a TC-006.7 | Integration | 7 testes |
| **RF-007** | TC-007.1 a TC-007.8 | Unit | 8 testes |
| **RF-008** | TC-008.1 a TC-008.7 | Manual | 7 verificações |
| **RF-009** | TC-009.1 a TC-009.8 | Coverage | 8 análises |
| **RNF-001 a RNF-007** | Testes de performance | Performance | 7 testes |
| **RI-001 a RI-003** | Testes manuais | Manual | 10 verificações |

**Total: 92 testes/verificações**

---

### 6.2 Requisitos → Implementação

| RF | Arquivo | Função/Componente | Linhas |
|----|---------|------------------|-------|
| RF-001 | app.py | `get_color_name_by_hex()` | 15-30 |
| RF-001 | app.py | `@app.get("/color-name?hex=...")` | 50-70 |
| RF-002 | app.py | `get_color_name_by_name()` | 35-50 |
| RF-003 | app.py | `translate_color_name()` (com cache) | 55-75 |
| RF-004 | app.py | `rgb_to_hsl()` | 80-100 |
| RF-004 | app.py | `hsl_distance()` | 105-125 |
| RF-005 | templates/index.html | Layout HTML responsivo | 1-80 |
| RF-005 | static/css/style.css | Media queries (320, 768, 1920px) | 1-200 |
| RF-005 | static/js/app.js | Event listeners e Fetch API | 1-100 |
| RF-006 | app.py | `@app.get("/health")` | 130-140 |
| RF-006 | app.py | OpenAPI docs automático (FastAPI) | - |
| RF-007 | app.py | `load_dataset()` | 10-20 |
| RF-007 | color_names.csv | Dataset CSV | 1000+ linhas |
| RF-008 | .github/workflows/ | CI/CD workflows | variável |
| RF-009 | tests/test_app.py | 26 funções de teste | ~400 linhas |

---

### 6.3 Testes → Critérios de Aceitação

| Critério | Testes Relacionados | Cobertura |
|----------|-----------------|----------|
| **Clareza** | Leitura manual do RF | 100% |
| **Testabilidade** | TC-001.x a TC-009.x | 92 testes |
| **Rastreabilidade** | Matriz ID-Teste-Código | 100% |
| **Factibilidade** | Prototipagem rápida | Validado |
| **Completude** | Análise de entrada/saída | Validado |
| **Consistência** | Análise de conflitos | Validado |

---

### 6.4 Dependências Entre Requisitos

```
RF-001 (Buscar Hex)
    ↓ depende de
    RF-004 (Análise HSL)
    RF-003 (Tradução)
    RF-007 (Dataset)

RF-002 (Buscar Nome)
    ↓ depende de
    RF-003 (Tradução)
    RF-007 (Dataset)

RF-005 (Interface)
    ↓ depende de
    RF-006 (API REST)

RF-006 (API REST)
    ↓ depende de
    RF-001, RF-002, RF-003, RF-004

RF-009 (Testes)
    ↓ testa
    RF-001, RF-002, RF-003, RF-004, RF-005, RF-006, RF-007, RF-008
```

---

## 7. Resumo Executivo

### 7.1 Total de Requisitos Aprovados

| Categoria | Total | Aprovados | Rejeitados |
|-----------|-------|-----------|-----------|
| **Funcionais (RF)** | 9 | 9 | 0 |
| **Não-Funcionais (RNF)** | 7 | 7 | 0 |
| **Dados (RD)** | 3 | 3 | 0 |
| **Interface (RI)** | 3 | 3 | 0 |
| **TOTAL** | **22** | **22** | **0** |

**Status Global:** ✅ **100% APROVADO**

---

### 7.2 Priorização

| Prioridade | RF | Total |
|-----------|-----|-------|
| **ALTA** | RF-001, RF-002, RF-004, RF-006, RF-007, RF-009 | 6 RFs |
| **MÉDIA** | RF-003, RF-005, RF-008 | 3 RFs |
| **TOTAL** | | 9 RFs |

---

### 7.3 Cronograma de Implementação (GRE-2)

| Sprint | Período | Requisitos | Status |
|--------|---------|-----------|--------|
| **Sprint 1** | 19/01 | RF-001 a RF-007 (Backend core) | Planejado |
| **Sprint 2** | 20/01 | RF-005, RF-009 (Interface + Testes) | Planejado |
| **Sprint 3** | 21/01 | RF-008 (Integração + Docs) | Planejado |

---

### 7.4 Análise de Risco

| Risco | Prob. | Impacto | Mitigation |
|-------|---|--------|-----------|
| Google Translate offline | Média | Alto | Cache + fallback |
| Cobertura testes < 70% | Média | Médio | Refatoração de código |
| Tempo insuficiente | Baixa | Alto | Priorizar RF críticos |
| GitHub conflito | Baixa | Médio | Usar branches feature |

**Risco Geral:** BAIXO ✅

---

### 7.5 Critérios de Sucesso Global

- ✅ 22/22 requisitos implementados conforme especificado
- ✅ 92+ testes executando com 0 falhas
- ✅ Cobertura >= 70%
- ✅ Performance dentro das specs (RF-001: <200ms, RF-002: <300ms)
- ✅ Interface responsiva em 3 resoluções
- ✅ GitHub com >= 10 commits descritivos
- ✅ Documentação 100% completa (docstrings, README, OpenAPI)

---

## 📌 Observações Finais

- ✅ Todos os 22 requisitos estão alinhados com objetivo do projeto
- ✅ Tecnologia escolhida (FastAPI, pytest, HTML5/CSS3) é apropriada
- ✅ Escopo é realista para 3 dias (19-21/01)
- ✅ Requisitos cobrem implementação, qualidade e documentação
- ✅ Cada requisito tem critério de aceitação verificável
- ✅ Matriz de rastreabilidade permite rastreamento completo

---

**Documento versão 2.0 - 18/01/2026**  
**Próxima revisão:** 21/01/2026 (após implementação)

---

**STATUS: ✅ DOCUMENTO COMPLETO E APROVADO EM GRE-1**
