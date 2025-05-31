# CÁLCULO DE PROBABILIDADE DE DESASTRE

def detectar_probabilidade_desastre(row):
    LIMIARES = {
        "chuva_dia": 80,
        "chuva_3dias": 120,
        "vento": 20,
        "umidade": 90,
        "onda_calor": 33
    }

    PESOS = {
        "chuva_dia": 0.5,
        "chuva_3dias": 0.3,
        "vento": 0.1,
        "umidade": 0.05,
        "onda_calor": 0.05
    }

    score = sum([
        PESOS["chuva_dia"]   if row['Precipitacao_total_diario(AUT)(mm)'] >= LIMIARES["chuva_dia"] else 0,
        PESOS["chuva_3dias"] if row['Chuva_3dias(mm)'] >= LIMIARES["chuva_3dias"] else 0,
        PESOS["vento"]        if row['Vento_velocidade_media_diario(AUT)(m/s)'] >= LIMIARES["vento"] else 0,
        PESOS["umidade"]      if row['Umidade_relativa_do_ar_media_diario(AUT)(%)'] >= LIMIARES["umidade"] else 0,
        PESOS["onda_calor"]   if row['Temp_media_3dias(°C)'] >= LIMIARES["onda_calor"] else 0
    ])

    score = min(score, 1)
    return round(score, 2)

# Aplicando a função ao df
df['Probabilidade_Desastre(%)'] = df.apply(detectar_probabilidade_desastre, axis=1)

# Convertendo para porcentagem
df['Probabilidade_Desastre(%)'] = (df['Probabilidade_Desastre(%)'] * 100).round().astype(int)
