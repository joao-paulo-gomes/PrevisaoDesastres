# IMPORTAÇÃO DE NOVOS DADOS (VIA API OPEN-METEO)

import requests
import pandas as pd
from datetime import datetime, timedelta

# Coordenadas de São Paulo
latitude = -23.5505
longitude = -46.6333

# Intervalo da previsão (hoje até 6 dias à frente)
data_inicio = datetime.today().strftime('%Y-%m-%d')
data_fim = (datetime.today() + timedelta(days=6)).strftime('%Y-%m-%d')

# Variáveis diárias e horárias
variaveis_diarias = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "windspeed_10m_max",
    "relative_humidity_2m_mean"
]
variaveis_horarias = ["surface_pressure"]

# Requisição da API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}" \
      f"&daily={','.join(variaveis_diarias)}" \
      f"&hourly={','.join(variaveis_horarias)}" \
      f"&timezone=America%2FSao_Paulo&start_date={data_inicio}&end_date={data_fim}"

response = requests.get(url)
data = response.json()

# Verifica se os dados vieram corretamente
if "daily" not in data or "hourly" not in data:
    print("Erro na resposta da API:")
    print(data)
else:
    # Dados diários
    df_daily = pd.DataFrame({
        "Data_Medicao": data["daily"]["time"],
        "Temperatura_maxima_diario(AUT)(°C)": data["daily"]["temperature_2m_max"],
        "Temperatura_minima_diario(AUT)(°C)": data["daily"]["temperature_2m_min"],
        "Precipitacao_total_diario(AUT)(mm)": data["daily"]["precipitation_sum"],
        "Umidade_relativa_do_ar_media_diario(AUT)(%)": data["daily"]["relative_humidity_2m_mean"],
        "Vento_velocidade_media_diario(AUT)(m/s)": data["daily"]["windspeed_10m_max"]
    })

    # Processa pressão horária
    df_hourly = pd.DataFrame({
        "DataHora": data["hourly"]["time"],
        "Pressao_atmosferica(AUT)(mB)": data["hourly"]["surface_pressure"]
    })
    df_hourly["Data_Medicao"] = pd.to_datetime(df_hourly["DataHora"]).dt.date
    df_hourly["Pressao_atmosferica(AUT)(mB)"] = pd.to_numeric(df_hourly["Pressao_atmosferica(AUT)(mB)"], errors='coerce')

    # Média diária da pressão
    df_pressao = df_hourly.groupby("Data_Medicao")[["Pressao_atmosferica(AUT)(mB)"]].mean().reset_index()
    df_pressao["Data_Medicao"] = pd.to_datetime(df_pressao["Data_Medicao"])
    df_pressao["Pressao_atmosferica(AUT)(mB)"] = df_pressao["Pressao_atmosferica(AUT)(mB)"].round(1)

    # Junta tudo
    df_daily["Data_Medicao"] = pd.to_datetime(df_daily["Data_Medicao"])
    df_final = pd.merge(df_daily, df_pressao, on="Data_Medicao", how="left")

    # Renomear pressão
    df_final.rename(columns={
        "Pressao_atmosferica(AUT)(mB)": "Pressao_atmosferica_media_diario(AUT)(mB)"
    }, inplace=True)

    # Reorganiza as colunas na mesma ordem do dataset originaL
    colunas_ordenadas = [
        "Data_Medicao",
        "Precipitacao_total_diario(AUT)(mm)",
        "Pressao_atmosferica_media_diario(AUT)(mB)",
        "Temperatura_maxima_diario(AUT)(°C)",
        "Temperatura_minima_diario(AUT)(°C)",
        "Umidade_relativa_do_ar_media_diario(AUT)(%)",
        "Vento_velocidade_media_diario(AUT)(m/s)",
    ]
    df_final = df_final[colunas_ordenadas]
