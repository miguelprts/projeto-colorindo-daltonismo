# MED 3 - Procedimentos para Coleta e Armazenamento
**Projeto:** Colorindo o Daltonismo

## 1. Coleta Automatizada
* **Fonte de Dados Técnica:** O arquivo `coverage.xml` é gerado automaticamente pelo comando `pytest --cov=app --cov-report=xml`.
* **Fonte de Dados de Processo:** As métricas de commits, issues e workflows são extraídas diretamente da API de estatísticas do repositório no GitHub.

## 2. Armazenamento
* Os dados brutos (XML e Logs) são armazenados no repositório sob controle de configuração (GCO).
* O histórico de medições é mantido de forma imutável através do versionamento Git para garantir a rastreabilidade exigida no Nível F.

## 3. Periodicidade
* **Coleta Diária:** Realizada a cada Push via Workflow automatizado.
* **Consolidação Semanal:** Miguel e Clark revisam os KPIs ao final de cada ciclo para validar a saúde do projeto.