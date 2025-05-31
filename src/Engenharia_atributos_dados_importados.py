# ENGENHARIA DE ATRIBUTOS COMPLETA APLICADA A df_final

# Chuva acumulada dos últimos 3 dias
df_final['Chuva_3dias(mm)'] = df_final['Precipitacao_total_diario(AUT)(mm)'].rolling(window=3).sum()

# Temperatura média dos últimos 3 dias
df_final['Temp_media_3dias(°C)'] = df_final[['Temperatura_maxima_diario(AUT)(°C)', 'Temperatura_minima_diario(AUT)(°C)']].mean(axis=1).rolling(window=3).mean()

# Variação diária de temperatura
df_final['Variacao_Temp(°C)'] = df_final['Temperatura_maxima_diario(AUT)(°C)'] - df_final['Temperatura_minima_diario(AUT)(°C)']

# Variações absolutas de pressão e umidade em relação ao dia anterior
df_final['Variacao_Pressao(mB)'] = df_final['Pressao_atmosferica_media_diario(AUT)(mB)'].diff().abs()
df_final['Variacao_Umidade(%)'] = df_final['Umidade_relativa_do_ar_media_diario(AUT)(%)'].diff().abs()

# Preencher valores ausentes nas colunas auxiliares com a média
colunas_auxiliares = [
    'Chuva_3dias(mm)',
    'Temp_media_3dias(°C)',
    'Variacao_Pressao(mB)',
    'Variacao_Umidade(%)'
]
df_final[colunas_auxiliares] = df_final[colunas_auxiliares].apply(lambda x: x.fillna(x.mean()))

# Arredondar para 1 casa decimal
colunas_para_arredondar = colunas_auxiliares + ['Variacao_Temp(°C)']
df_final[colunas_para_arredondar] = df_final[colunas_para_arredondar].round(1)
