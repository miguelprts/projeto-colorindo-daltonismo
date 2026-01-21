# Registro de Liberação (GCO 4)
**Projeto:** Colorindo o Daltonismo  
**Versão:** v1.0.0-beta  
**Data da Liberação:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Escopo desta Versão
Esta liberação consolida a inteligência de backend e a interface básica, representando o marco final da Sprint 3.

### 1.1 Funcionalidades Implementadas (Baseline)
* **Módulo de Identificação:** Cálculo de distância perceptual HSL com trava de **95% de precisão** (RD05).
* **Módulo de Tradução:** Integração com API externa e sistema de Cache `@lru_cache` (RD03).
* **Interface Web:** Páginas responsivas para captura de Hexadecimal e exibição de resultados (RI01, RI02).

## 2. Histórico de Modificações (SMs Incorporadas)
As seguintes Solicitações de Mudança foram fechadas e integradas nesta versão:
* **SM-001:** Setup inicial da arquitetura SOLID.
* **SM-002:** Ajuste da trava de similaridade de 60% para 95% (Melhoria de Qualidade).
* **SM-003:** Correção da injeção de dependência nos testes unitários (Bugfix).

## 3. Composição da Release (Itens de Configuração)
A versão v1.0.0 é composta pelo estado atual dos seguintes ICs:
* `app/core/` (v1.2.4)
* `app/api/` (v1.1.0)
* `color_names.csv` (v1.0.1)
* `requirements.txt` (v1.0.0)

## 4. Problemas Conhecidos e Limitações
* A performance da busca pode degradar se o CSV ultrapassar 50.000 registros (Risco R06).
* O feedback visual de "Copiado para o Clipboard" (RI05) está em fase de refinamento.

## 5. Instruções de Instalação
1. Clonar repositório: `git clone [url] -b v1.0.0`
2. Instalar dependências: `pip install -r requirements.txt`
3. Executar: `python -m uvicorn app.main:app`