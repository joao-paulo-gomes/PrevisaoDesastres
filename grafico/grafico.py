import matplotlib.pyplot as plt

# Ordena a coluna de datas esteja ordenada
df_final = df_final.sort_values("Data_Medicao")

# Tamanho do gráfico
plt.figure(figsize=(14, 6))

# Gráfico de barras da chuva
plt.bar(df_final["Data_Medicao"], df_final["Precipitacao_total_diario(AUT)(mm)"], 
        color='skyblue', alpha=0.5, label='Chuva diária (mm)')

# Linha de probabilidade de desastre
plt.plot(df_final["Data_Medicao"], df_final["Probabilidade_Desastre(%)"], 
         color='red', marker='o', linewidth=2, label='Probabilidade de Desastre (%)')

# Linha de temperatura média dos últimos 3 dias
plt.plot(df_final["Data_Medicao"], df_final["Temp_media_3dias(°C)"], 
         color='orange', linestyle='--', linewidth=2, label='Temp. Média 3 dias (°C)')

# Títulos e legendas
plt.title("Previsão de Risco Climático - Próximos Dias", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Valores", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
