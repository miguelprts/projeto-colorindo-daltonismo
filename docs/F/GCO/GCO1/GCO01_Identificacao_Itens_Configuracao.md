# Identificação de Itens de Configuração (GCO 1)
**Projeto:** Colorindo o Daltonismo
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Critérios de Seleção
Para que um item seja considerado um **Item de Configuração (IC)** neste projeto, ele deve atender a pelo menos um dos seguintes critérios:
* Ser essencial para a reconstrução do ambiente de software (**Reprodutibilidade**).
* Ser um produto de trabalho exigido pelo modelo **MPS.Br Nível F** (**Conformidade**).
* Conter a lógica de negócio ou dados fundamentais para os **23 requisitos** (**Funcionalidade**).

## 2. Inventário de Itens de Configuração (ICs)
A tabela abaixo lista os itens que estão sob controle de versão rigoroso no repositório Git/GitHub.

| ID do IC | Nome do Item | Descrição | Formato | Categoria |
| :--- | :--- | :--- | :---: | :--- |
| **IC-01** | Código Fonte Core | Pasta `/app` (Lógica, API e Serviços). | .py | Software |
| **IC-02** | Suíte de Testes | Pasta `/tests` (Unitários e Integração). | .py | Software |
| **IC-03** | Catálogo de Cores | Arquivo `color_names.csv`. | .csv | Dados |
| **IC-04** | Documentação GPR | Planos de Projeto (GPR 01 a 19). | .md | Documento |
| **IC-05** | Matriz de Rastreabilidade| Vínculo Requisito x Código (GRE 03). | .md / .xlsx| Documento |
| **IC-06** | Gestão de Dependências | Arquivo `requirements.txt`. | .txt | Infraestrutura|
| **IC-07** | Configuração de Qualidade| Arquivo `sonar-project.properties`. | .properties| Infraestrutura|

## 3. Esquema de Identificação e Versão
Cada item acima segue a convenção de nomenclatura do projeto e é versionado automaticamente pelo Git através de **SHA-1 Hashes**. 
* **Linhas de Base (Baselines):** São estabelecidas ao final de cada Sprint (Sprint 1, 2 e 3) e identificadas via **Tags** no GitHub (ex: `v1.0.0-alpha`).

## 4. Responsabilidade
Miguel e Clark são responsáveis por garantir que nenhum IC seja alterado fora do processo de controle de mudanças (GCO 3).