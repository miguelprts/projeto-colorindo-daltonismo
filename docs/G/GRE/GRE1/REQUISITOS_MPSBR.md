# Documentação Técnica: Projeto Colorindo o Daltonismo 
**Mapeamento de Processos MPS.Br (Nível G) e Arquitetura SOLID**

---

## 1. Introdução
Este documento detalha o planejamento e a execução do software "Colorindo o Daltonismo", desenvolvido para auxiliar a identificação cromática através de algoritmos de similaridade e distância perceptual. O projeto segue os padrões de Engenharia de Software exigidos para o Nível G do MPS.Br.

---

## 2. Gerência de Requisitos (GRE)
Total de 23 requisitos levantados e revisados pela equipe de engenharia.

### 2.1 Requisitos Funcionais (RF)
| ID | Nome | Descrição |
| :--- | :--- | :--- |
| **RF01** | Busca por Hexadecimal | Identificar a cor mais próxima no dataset a partir de um código HEX. |
| **RF02** | Conversão por Nome | Retornar o valor HEX correspondente a um nome de cor fornecido. |
| **RF03** | Tradução EN/PT | Traduzir nomes de cores de inglês para português automaticamente. |
| **RF04** | Tradução PT/EN | Traduzir entradas em português para realizar buscas no banco de dados (EN). |
| **RF05** | Fuzzy Matching | Tolerar erros de digitação nos nomes usando algoritmos de similaridade. |
| **RF06** | Cálculo HSL | Priorizar a percepção visual humana através do cálculo de distância HSL. |
| **RF07** | Endpoint Health | Disponibilizar rota `/health` para monitorar o status do servidor. |
| **RF08** | Navegação Global | Permitir a transição fluida entre as páginas de Identificação e Conversão. |

### 2.2 Requisitos Não Funcionais (RNF)
| ID | Nome | Descrição |
| :--- | :--- | :--- |
| **RNF01** | Padrão SOLID | O design do sistema deve seguir obrigatoriamente os 5 princípios SOLID. |
| **RNF02** | Baixa Latência | Respostas da API devem ser entregues em menos de 200ms. |
| **RNF03** | Portabilidade | Compatibilidade garantida entre Windows, Linux e Google Colab. |
| **RNF04** | Modularidade | O núcleo do sistema deve ser independente de serviços de terceiros (Tradutor). |
| **RNF05** | Testabilidade | A arquitetura deve permitir testes unitários automatizados com Pytest. |

### 2.3 Requisitos de Dados (RD)
| ID | Nome | Descrição |
| :--- | :--- | :--- |
| **RD01** | Persistência CSV | O dataset de cores deve ser mantido e lido a partir de um arquivo `.csv`. |
| **RD02** | Normalização | Limpeza automática de caracteres especiais e espaços em códigos HEX. |
| **RD03** | Cache de Tradução | Uso de memória cache (`lru_cache`) para evitar requisições externas repetidas. |
| **RD04** | Validação de Carga | Impedir o início do servidor caso o dataset esteja ausente ou corrompido. |
| **RD05** | Filtro de Similaridade | Ignorar resultados de busca por nome com similaridade inferior a 60%. |

### 2.4 Requisitos de Interface (RI)
| ID | Nome | Descrição |
| :--- | :--- | :--- |
| **RI01** | Design Responsivo | A interface deve se adaptar corretamente a desktops e dispositivos móveis. |
| **RI02** | Visualização Visual | Exibir um quadrado de cor (swatch) dinâmico que reflete o resultado encontrado. |
| **RI03** | Feedback de Erro | Alertas visuais em vermelho para cores não encontradas ou parâmetros inválidos. |
| **RI04** | Feedback de Sucesso | Mensagens em verde indicando a precisão da cor encontrada. |
| **RI05** | Prevenção de Erro | Bloquear o botão de envio enquanto uma requisição está sendo processada. |

---

## 3. Arquitetura do Sistema (SOLID)
A estrutura de pastas e classes reflete a maturidade técnica do projeto:

* **`app/core/`**: Contém as interfaces (Abstrações) e lógica matemática pura.
* **`app/data/`**: Repositório de dados utilizando Pandas para processamento eficiente.
* **`app/services/`**: Serviços de infraestrutura (Tradução) e o Orquestrador (Manager).
* **`templates/`**: Camada de apresentação (Interface de Usuário).

---

## 4. Gerência de Projetos (GPR) e Configuração (GCO)
* **Versionamento**: Uso de branches específicas para cada requisito (Rastreabilidade).
* **Commits**: Padronizados com o ID do requisito correspondente (ex: `feat: implementa RF01`).
* **Garantia de Qualidade (GQA)**: Checklists internos para revisão de código antes de cada Pull Request.

---

## 5. Gerência de Aquisição (RAP)
Lista de dependências externas justificadas:
1.  **FastAPI**: Servidor web de alta performance.
2.  **Pandas**: Manipulação de dados (Data Science).
3.  **Deep-Translator**: Tradução dinâmica gratuita.
4.  **Uvicorn**: Executor ASGI para produção.

---