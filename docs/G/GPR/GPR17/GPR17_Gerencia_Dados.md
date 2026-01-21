# Gerência de Dados do Projeto (GPR 17)
**Projeto:** Colorindo o Daltonismo
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Identificação dos Dados Críticos
Os dados essenciais para o funcionamento do sistema foram identificados e classificados:

* **D01 (Catálogo de Cores):** Arquivo `color_names.csv` contendo nomes em inglês e valores Hexadecimais.
* **D02 (Cache de Tradução):** Estrutura em memória (`lru_cache`) para otimização de performance.
* **D03 (Dicionário de Tradução):** Mapeamento interno de termos técnicos de cores.

## 2. Estratégia de Armazenamento e Integridade
Dado que o projeto utiliza **arquivos planos (CSV)**, as seguintes medidas de segurança foram adotadas:

* **Normalização na Carga:** Ao ler o CSV via Pandas, o sistema aplica limpeza de strings e conversão de Hex para Uppercase para evitar duplicidade.
* **Proteção de Acesso:** O acesso ao arquivo é centralizado na classe `ColorRepository` (SOLID), impedindo que outros módulos alterem o arquivo diretamente.
* **Validação de Estrutura:** O sistema verifica se as colunas `name` e `hex` existem no arquivo antes de iniciar o serviço. Caso contrário, uma exceção é lançada (RD02).

## 3. Privacidade e Backup
* **Segurança:** O projeto não armazena dados sensíveis de usuários (PII), apenas dados técnicos de cores, atendendo à LGPD por design.
* **Backup e Versionamento:** O arquivo `color_names.csv` é gerenciado pelo **Git**. Qualquer alteração acidental no catálogo pode ser revertida via `git checkout`.
* **Disponibilidade:** O cache em memória garante que, mesmo com falhas momentâneas na API de tradução, os dados já processados permaneçam disponíveis durante a sessão.

## 4. Plano de Descarte
Os dados de cache são voláteis e descartados ao encerrar o servidor Uvicorn. O arquivo CSV é mantido como base histórica do projeto.