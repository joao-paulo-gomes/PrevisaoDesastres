# TREINAMENTO E AVALIAÇÃO E DO MODELO

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

# Lista de variáveis independentes (features)
features = [
    'Precipitacao_total_diario(AUT)(mm)',
    'Pressao_atmosferica_media_diario(AUT)(mB)',
    'Temperatura_maxima_diario(AUT)(°C)',
    'Temperatura_minima_diario(AUT)(°C)',
    'Umidade_relativa_do_ar_media_diario(AUT)(%)',
    'Vento_velocidade_media_diario(AUT)(m/s)',
    'Chuva_3dias(mm)',
    'Temp_media_3dias(°C)',
    'Variacao_Temp(°C)',
    'Variacao_Pressao(mB)',
    'Variacao_Umidade(%)'
]

# Variável alvo
target = 'Probabilidade_Desastre(%)'

# Separação entre variáveis independentes (X) e variável alvo (y)
X = df[features]
y = df[target]

# Divisão em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do modelo de regressão
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Previsão no conjunto de teste
y_pred = model.predict(X_test)

# Avaliação do modelo
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Resultados
print("\U0001F4BB Treinamento e Avaliação do Modelo (Random Forest Regressor)")
print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
print(f"Erro Absoluto Médio (MAE): {mae:.2f}")
print(f"Coeficiente de Determinação (R²): {r2:.2f}")


# Salvar o modelo treinado
joblib.dump(model, 'modelo_random_forest.pkl')

# Salvar a lista de features usadas
joblib.dump(features, 'lista_features.pkl')
