import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# 1. Ler o dataset
dataset = pd.read_csv("dataset_risco.csv")

print("\nDATASET DE RISCO:")
print(dataset)


# 2. Separar frases e classificações
X = dataset["FRASE:"]
y = dataset["SITUACAO:"]


# 3. Dividir os dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


print("\nQuantidade de frases para treinamento:", len(X_treino))
print("Quantidade de frases para teste:", len(X_teste))


# 4. Transformar os textos em números usando TF-IDF
vetorizador = TfidfVectorizer()

X_treino_tfidf = vetorizador.fit_transform(X_treino)
X_teste_tfidf = vetorizador.transform(X_teste)


print(
    "\nQuantidade de características geradas pelo TF-IDF:",
    len(vetorizador.get_feature_names_out())
)


# 5. Criar o modelo
modelo = LogisticRegression(random_state=42)


# 6. Treinar o modelo
modelo.fit(X_treino_tfidf, y_treino)


# 7. Fazer previsões
previsoes = modelo.predict(X_teste_tfidf)


# 8. Avaliar o modelo
acuracia = accuracy_score(y_teste, previsoes)

print("\nACURÁCIA DO MODELO:", acuracia)
print("ACURÁCIA EM PORCENTAGEM:", f"{acuracia * 100:.2f}%")

print("\nRELATÓRIO DE CLASSIFICAÇÃO:")
print(classification_report(y_teste, previsoes))


# 9. Mostrar as previsões do conjunto de teste
print("\nCOMPARAÇÃO ENTRE VALOR REAL E PREVISÃO:")

for frase, real, previsto in zip(X_teste, y_teste, previsoes):

    if real == previsto:
        resultado = "ACERTO"
    else:
        resultado = "ERRO"

    print("\nFrase:", frase)
    print("Classificação real:", real)
    print("Classificação prevista:", previsto)
    print("Resultado:", resultado)


# 10. Testar novas frases
novas_frases = [
    "estou sentindo uma dor forte no peito e falta de ar",
    "tenho um pequeno desconforto nas costas",
    "sinto pressão no peito acompanhada de suor frio",
    "estou um pouco cansado depois de estudar"
]

novas_frases_tfidf = vetorizador.transform(novas_frases)

previsoes_novas = modelo.predict(novas_frases_tfidf)


print("\nTESTE COM NOVAS FRASES:")

for frase, previsao in zip(novas_frases, previsoes_novas):

    print("\nFrase:", frase)
    print("Classificação:", previsao)