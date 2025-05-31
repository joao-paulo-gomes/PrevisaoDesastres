
# 🌧️ Previsão de Desastres Climáticos com Machine Learning

Este projeto foi desenvolvido como trabalho final da disciplina **Atividade Extensionista II** do curso de Análise e Desenvolvimento de Sistemas da UNINTER.

A ideia é usar dados reais da estação meteorológica do Mirante de Santana (São Paulo), junto com previsões climáticas da API Open-Meteo, para estimar a **probabilidade de ocorrência de desastres naturais** com base em variações climáticas — como chuvas fortes, ventos, calor intenso, umidade elevada e variações de pressão.

---

## 📁 Organização dos Arquivos

O projeto foi dividido por etapas para facilitar o entendimento e a reutilização:

```
PrevisaoDesastres/
├── src/
│   ├── pre_processamento.py
│   ├── engenharia_atributos.py
│   ├── calculo_probabilidade.py
│   ├── treinamento_avaliacao.py
│   ├── aplicacao_modelo.py
│   ├── engenharia_atributos_dados_importados.py
├── api/
│   └── importacao_novos_dados.py
├── models/
│   ├── modelo_random_forest.pkl
│   └── lista_features.pkl
├── notebooks/
│   └── TrabalhoUninter.ipynb
├── data/
│   └── dados_exemplo.csv
└── requirements.txt
```

---

## 🧪 O que o projeto faz

- Limpa e prepara os dados meteorológicos históricos.
- Cria novas colunas com informações mais úteis (como variações e médias dos últimos dias).
- Usa regras manuais (limiares climáticos) para criar uma variável chamada `Probabilidade_Desastre(%)`.
- Treina um modelo de Machine Learning (Random Forest) com base nesses dados.
- Importa novos dados climáticos da Open-Meteo.
- Aplica o modelo para prever o risco de desastre nos próximos dias.

---

## 🚀 Como rodar

### 1. Clone o repositório
```bash
git clone https://github.com/seuusuario/previsao-desastres.git
```

### 2. Instale os pacotes necessários
```bash
pip install -r requirements.txt
```

### 3. Execute os arquivos `.py` na ordem correta

Você pode rodar cada etapa diretamente com Python (ou pelo notebook):

```bash
python src/pre_processamento.py
python src/engenharia_atributos.py
python src/calculo_probabilidade.py
python src/treinamento_avaliacao.py
python api/importacao_novos_dados.py
python src/engenharia_atributos_dados_importados.py
python src/aplicacao_modelo.py
```



## 👤 Autor

**João Paulo Gomes**  
Estudante de Análise e Desenvolvimento de Sistemas  
📧 joaopaulogomestoth@gmail.com