import pandas as pd
import matplotlib.pyplot as plt



def gerar_tabela(resultados):

    df = pd.DataFrame(resultados)

    df.to_csv(
        "output/resultados.csv",
        index=False,
        encoding="utf-8"
    )
    print(df)
def gerar_graficos(resultados):
    df = pd.DataFrame(resultados)
    media = df.groupby("tecnica")["acuracia"].mean()
    media.plot(kind="bar")
    plt.title("Acurácia por Técnica")
    plt.savefig("output/graficos/acuracia.png")
    plt.close()
    custo = df.groupby("tecnica")["tokens_prompt"].mean()
    custo.plot(kind="bar")
    plt.title("Tokens Médios")
    plt.savefig("output/graficos/custo.png")
    plt.close()

