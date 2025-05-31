# PRÉ-PROCESSAMENTO DOS DADOS

import pandas as pd
import numpy as np

# Caminho do arquivo (substitua pelo caminho correto do seu CSV)
caminho_arquivo = "caminho_arquivo"
df = pd.read_csv(caminho_arquivo, sep=';')

# Conversão coluna de datas
if 'Data_Medicao' in df.columns:
    df['Data_Medicao'] = df['Data_Medicao'].str.strip()
    df['Data_Medicao'] = pd.to_datetime(df['Data_Medicao'], format='%d/%m/%Y', errors='coerce')

# Remover coluna ponto de orvalho
coluna_remover = 'Temperatura_ponto_orvalho_media_diario(AUT)(°C)'
if coluna_remover in df.columns:
    df.drop(columns=[coluna_remover], inplace=True)

# Substituir vírgulas por pontos e converter para float
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.replace(',', '.', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Preencher valores ausentes
coluna_chuva = 'Precipitacao_total_diario(AUT)(mm)'
if coluna_chuva in df.columns:
    df[coluna_chuva] = df[coluna_chuva].fillna(df[coluna_chuva].mean())

colunas_mediana = [
    'Pressao_atmosferica_media_diario(AUT)(mB)',
    'Temperatura_maxima_diario(AUT)(°C)',
    'Temperatura_minima_diario(AUT)(°C)',
    'Umidade_relativa_do_ar_media_diario(AUT)(%)',
    'Vento_velocidade_media_diario(AUT)(m/s)'
]

for col in colunas_mediana:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

df['Umidade_relativa_do_ar_media_diario(AUT)(%)'] = df['Umidade_relativa_do_ar_media_diario(AUT)(%)'].round(0).astype(int)

