# FII Monthly Data Pipeline

A data engineering pipeline that collects, transforms, and loads monthly financial reports from Brazilian Real Estate Investment Funds (FIIs) using public data from the Brazilian Securities Commission (CVM).

## Overview

The pipeline downloads monthly report files directly from the CVM public data portal, extracts financial data from ZIP archives, consolidates records across multiple years, loads the dataset into a PostgreSQL database, and exports analytical reports in CSV format.

## Tech Stack

- Python
- requests — automated file download from public API
- pandas — data transformation and analysis
- SQLAlchemy — database abstraction layer
- psycopg2 — PostgreSQL driver
- python-dotenv — environment variable management

## Project Structure

```
fii-monthly-pipeline/
│
├── data/
│   ├── top10_fundos.csv          # Top 10 funds by average total invested
│   └── evolucao_mensal.csv       # Monthly evolution of total invested
│
├── src/
│   └── web_scrapping.py          # Main pipeline script
│
├── .env.example                  # Environment variable template
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file based on `.env.example`:

```
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/WesleySr21/fii-monthly-pipeline.git
cd fii-monthly-pipeline
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure environment variables

```bash
cp .env.example .env
```

4. Run the pipeline

```bash
python src/web_scrapping.py
```

## Data Source

[CVM — Portal de Dados Abertos](https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/)

---

# Pipeline de Dados Mensais de FIIs

Pipeline de engenharia de dados que coleta, transforma e carrega informes mensais de Fundos de Investimento Imobiliário (FIIs) utilizando dados públicos da Comissão de Valores Mobiliários (CVM).

## Visao Geral

O pipeline realiza o download automatizado dos arquivos de informe mensal diretamente do portal de dados abertos da CVM, extrai os dados financeiros dos arquivos ZIP, consolida os registros de multiplos anos, carrega o dataset em um banco de dados PostgreSQL e exporta relatorios analiticos em formato CSV.

## Tecnologias

- Python
- requests — download automatizado de arquivos da API publica
- pandas — transformacao e analise dos dados
- SQLAlchemy — camada de abstracao do banco de dados
- psycopg2 — driver PostgreSQL
- python-dotenv — gerenciamento de variaveis de ambiente

## Estrutura do Projeto

```
fii-monthly-pipeline/
│
├── data/
│   ├── top10_fundos.csv          # Top 10 fundos por total investido medio
│   └── evolucao_mensal.csv       # Evolucao mensal do total investido
│
├── src/
│   └── web_scrapping.py          # Script principal do pipeline
│
├── .env.example                  # Modelo de variaveis de ambiente
├── requirements.txt
└── README.md
```

## Variaveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
```

## Como Executar

1. Clone o repositorio

```bash
git clone https://github.com/WesleySr21/fii-monthly-pipeline.git
cd fii-monthly-pipeline
```

2. Instale as dependencias

```bash
pip install -r requirements.txt
```

3. Configure as variaveis de ambiente

```bash
cp .env.example .env
```

4. Execute o pipeline

```bash
python src/web_scrapping.py
```

[CVM — Portal de Dados Abertos](https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/)
