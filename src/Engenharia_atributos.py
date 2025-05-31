# ENGENHARIA DE ATRIBUTOS

# Chuva acumulada últimos 3 dias
df['Chuva_3dias(mm)'] = df['Precipitacao_total_diario(AUT)(mm)'].rolling(window=3).sum()

# Temperatura média últimos 3 dias
df['Temp_media_3dias(°C)'] = df[['Temperatura_maxima_diario(AUT)(°C)', 'Temperatura_minima_diario(AUT)(°C)']].mean(axis=1).rolling(window=3).mean()

# Variação diária de temperatura
df['Variacao_Temp(°C)'] = df['Temperatura_maxima_diario(AUT)(°C)'] - df['Temperatura_minima_diario(AUT)(°C)']

# Variações absolutas de pressão e umidade em relação ao dia anterior
df['Variacao_Pressao(mB)'] = df['Pressao_atmosferica_media_diario(AUT)(mB)'].diff().abs()
df['Variacao_Umidade(%)'] = df['Umidade_relativa_do_ar_media_diario(AUT)(%)'].diff().abs()

# Preencher valor ausente com média
colunas_auxiliares = [
    'Chuva_3dias(mm)',
    'Temp_media_3dias(°C)',
    'Variacao_Pressao(mB)',
    'Variacao_Umidade(%)'
]
df[colunas_auxiliares] = df[colunas_auxiliares].apply(lambda x: x.fillna(x.mean()))

# Arredonda todas as novas colunas para 1 casa decimal
colunas_para_arredondar = colunas_auxiliares + ['Variacao_Temp(°C)']
df[colunas_para_arredondar] = df[colunas_para_arredondar].round(1)
