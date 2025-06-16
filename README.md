# Projeto CyberShield

O **CyberShield** é um painel analítico interativo desenvolvido para analisar ameaças cibernéticas globais entre 2015 e 2024. Utilizando Python, Dash e bibliotecas de visualização, o projeto visa extrair insights relevantes sobre ataques cibernéticos.

O projeto é dividido em duas partes principais:
- 📘 Um arquivo notebook com a **exploração inicial dos dados e aplicação de testes estatísticos**.  
🔗 Acesse o notebook no Google Colab: [colab.research.google.com](colab.research.google.com)
- 📊 Um dashboard interativo construído com **Dash** para visualização dinâmica dos resultados.  
🌐 Acesse o dashboard online: 👉 [cybershield-j2bk.onrender.com](https://cybershield-j2bk.onrender.com/)

## 📁 Estrutura do Projeto

```
Projeto CyberShield/
│
├── assets/
│   └── styles.css                # Estilos personalizados do dashboard
│
├── data/
│   └── Global_Cybersecurity_Threats_2015-2024.csv  # Base de dados com ameaças cibernéticas
│
├── notebooks/
│   └── eda_and_statistical_tests.ipynb  # Análises exploratórias e testes estatísticos
│
├── app.py                      # Arquivo principal para executar o app Dash
├── callbacks.py                # Lógica de callbacks do Dash (interatividade)
├── cards.py                    # Componentes de resumo (cards de métricas)
├── graphs.py                   # Funções para gerar gráficos interativos
├── layout.py                   # Estrutura visual do dashboard
├── requirements.txt            # Dependências do projeto
```

## 📂 Dataset

Os dados utilizados neste projeto foram obtidos no Kaggle, através do seguinte link: [Global Cybersecurity Threats 2015-2024 - Kaggle](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024/data).

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/projeto-cybershield.git
cd projeto-cybershield
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o app:

```bash
python app.py
```

Acesse o app no navegador em: `http://127.0.0.1:8050`

## 🧠 Tecnologias Utilizadas

- Python
- Dash (Plotly)
- Pandas
- Scikit-learn
- CSS (customizado)
- Jupyter Notebook


## ✍️ Contato

Nicolli Freitas | nicollifreitas03@gmail.com