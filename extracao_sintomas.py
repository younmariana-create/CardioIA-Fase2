import pandas as pd

mapa = pd.read_csv("mapa_conhecimento.csv")

print("\nMAPA DE CONHECIMENTO:")
print(mapa)

with open("frases_sintomas.txt", "r", encoding="utf-8") as arquivo:
    frases = arquivo.readlines()

sintomas = [
    "dor forte no peito",
    "cansaço constante",
    "fadiga",
    "falta de ar",
    "dificuldade para respirar",
    "coração bater muito rápido",
    "palpitações",
    "tontura",
    "parece que vou desmaiar",
    "inchaço nas pernas",
    "inchaço nos tornozelos",
    "pressão forte no peito",
    "suor frio",
    "fadiga persistente",
    "aperto no tórax",
    "esforço físico"
]

for frase in frases:
    frase_limpa = frase.strip().lower()

    print("\nFrase:", frase.strip())

    sintomas_encontrados = []

    for sintoma in sintomas:
        if sintoma in frase_limpa:
            sintomas_encontrados.append(sintoma)

    print("Sintomas encontrados:", sintomas_encontrados)

    diagnosticos = []

    for _, linha in mapa.iterrows():
        sintoma1 = linha["Sintoma 1"].lower()
        sintoma2 = linha["Sintoma 2"].lower()

        if sintoma1 in sintomas_encontrados and sintoma2 in sintomas_encontrados:
            diagnosticos.append(linha["Doenca Associada"])

    if diagnosticos:
        diagnosticos_unicos = list(dict.fromkeys(diagnosticos))
        print("Possível condição associada:", ", ".join(diagnosticos_unicos))
    else:
        print("Nenhuma associação encontrada no mapa.")