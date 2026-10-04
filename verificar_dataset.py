import pandas as pd

dataset = pd.read_csv("dataset_risco.csv")

print("\nDATASET DE RISCO:")
print(dataset)

print("\nQuantidade de exemplos por situação:")
print(dataset["SITUACAO:"].value_counts())