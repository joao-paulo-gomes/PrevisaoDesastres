# APLICAÇÃO DO MODELO AOS DADOS IMPORTADOS

modelo = joblib.load("modelo_random_forest.pkl")
features_usadas = joblib.load("lista_features.pkl")

X_novos_dados = df_final[features_usadas]

# Aplica o modelo e adiciona a probabilidade prevista
df_final["Probabilidade_Desastre(%)"] = modelo.predict(X_novos_dados) * 100
df_final["Probabilidade_Desastre(%)"] = df_final["Probabilidade_Desastre(%)"].clip(lower=0, upper=100).round().astype(int)