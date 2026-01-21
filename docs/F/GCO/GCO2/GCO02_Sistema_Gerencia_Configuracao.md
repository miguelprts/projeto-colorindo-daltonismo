# Sistema de Gerência de Configuração (GCO 2)
**Projeto:** Colorindo o Daltonismo  
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Ferramental Escolhido
O sistema de gerência de configuração (SGC) é composto por ferramentas que garantem o armazenamento seguro e o histórico de todos os Itens de Configuração (ICs).

* **Controle de Versão Local:** Git (v2.40+).
* **Repositório Remoto (Servidor de Configuração):** GitHub (Privado/Público).
* **Cliente de Interface:** Terminal PowerShell e VS Code Git Lens.

## 2. Estrutura do Repositório (Branches)
Para atender ao rigor do **Nível F**, adotamos uma estratégia de ramificação que protege a integridade do produto:

* **`main` (Produção):** Contém apenas código estável, testado e aprovado pelo Sonar. Linha de base final.
* **`develop` (Integração):** Onde as funcionalidades são unificadas e os testes de integração ocorrem.
* **`feature/` (Desenvolvimento):** Branches temporárias para requisitos específicos (ex: `feature/similaridade-95`).

## 3. Controle de Acesso e Permissões
A autoridade de modificação (GPR 7) é refletida nas configurações do GitHub:
* **Miguel & Clark:** Possuem permissões de *Maintainer*.
* **Branch Protection Rules:** Ativadas na `main`. É proibido fazer *push* direto. Toda alteração exige um **Pull Request (PR)** com aprovação do outro integrante e aprovação dos testes automáticos.

## 4. Manutenção e Backup
O sistema é mantido através da sincronização constante entre os repositórios locais e o GitHub. 
* **Backup Geográfico:** Garantido pela infraestrutura distribuída do GitHub.
* **Disponibilidade:** Acesso 24/7 via internet para ambos os líderes.

## 5. Auditoria do SGC
Semanalmente, a equipe verifica se o histórico de commits está limpo e se as Tags de versão (Baselines) foram criadas corretamente após cada Sprint.