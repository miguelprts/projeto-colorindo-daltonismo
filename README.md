# 🎨 Colorindo o Daltonismo

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![Pytest](https://img.shields.io/badge/test-pytest-yellow.svg)](https://docs.pytest.org/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](#)

Uma aplicação web desenvolvida para auxiliar pessoas com daltonismo a identificar cores em tempo real através de imagens ou câmera, além de converter nomes de cores em seus respectivos códigos hexadecimais.



## 🚀 Funcionalidades

- **Identificador Visual:** Carregue imagens ou use sua câmera. Clique em qualquer ponto da imagem para saber o nome da cor (PT-BR/EN), o código HEX e a proximidade com cores padrão.
- **Conversor de Nomes:** Digite o nome de uma cor (ex: "Azul Marinho") e obtenha o código HEX, RGB e visualize a cor instantaneamente.
- **Interface Responsiva:** Menu adaptável para dispositivos móveis (o menu se transforma em colunas em telas pequenas).
- **Matemática Perceptual:** Cálculos de distância de cores no espaço HSL para garantir a melhor correspondência possível.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.12, Flask.
- **Frontend:** HTML5, CSS3 (Responsivo), JavaScript (ES6+).
- **Processamento:** Algoritmos de busca Fuzzy para nomes e Distância Euclidiana para cores.
- **Testes:** Pytest com foco em cobertura de 100% e precisão de ponto flutuante.

## 📦 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/miguelprts/projeto-colorindo-daltonismo.git](https://github.com/miguelprts/projeto-colorindo-daltonismo.git)
   cd projeto-colorindo-daltonismo
   python -m uvicorn app.main:app --reload
