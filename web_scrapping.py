import requests
import pandas as pd
import zipfile
import io
import sqlalchemy
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
import psycopg2

print('Starting...')

anos = [2022, 2023, 2024]
def gera_url(anos):
    urls = []
    for ano in anos:
        url = f'https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/inf_mensal_fii_{ano}.zip'
        urls.append(url)
       
    return urls

url_full = gera_url(anos)

def zip_para_df(urls):
    success = []
    errors = []

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            names = zip_file.namelist()
            ano = url.split('_')[-1].split(".")[0]

            df = pd.read_csv(zip_file.open(f'inf_mensal_fii_ativo_passivo_{ano}.csv'), sep=';', encoding='latin-1')
           
            df.columns = df.columns.str.lower()
            df["data_referencia"] = pd.to_datetime(df["data_referencia"])
            success.append(df)
            print(f'[OK] {names[0]} - {df.shape[0]} registros coletados')

        else:
            print(f'[ERRO] {url} - {response.status_code}')
            errors.append({"arquivo": url, "status_code": response.status_code})

    return success, errors

print('Collecting data from link...')
all_dfs, errors = zip_para_df(url_full)

print('Creating a DF')
df_final = pd.concat(all_dfs).reset_index(drop=True)

df_for_sql = df_final[['cnpj_fundo_classe', 'data_referencia', 'total_investido', 'total_passivo', 'disponibilidades']]
df_for_sql

print('Conecting to DataBase...')

load_dotenv()
engine = sqlalchemy.create_engine(
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{quote_plus(os.getenv('DB_PASSWORD'))}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

try:
    with engine.connect() as conn:
        print("Connected to DB")
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()

print('Inserting data to the DB')
df_for_sql.to_sql('fiis', engine, index=False, if_exists='replace')

top_10 = (df_final.groupby(['cnpj_fundo_classe'])['total_investido']
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .reset_index())

print('Salving CSV of top 10 funds')
top_10.to_csv('top10_fundos.csv', sep=';', index=False)

#Evolução do Total_Investido total de todos os fundos por mês
m_evolution = (df_final.groupby(['data_referencia'])['total_investido']
                .sum()
                .reset_index())

print('Salving CSV monthly evolution')
m_evolution.to_csv('evolucao_mensal.csv', sep=';', index=False)

print('Fineshed!')