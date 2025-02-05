import camelot
import pandas as pd
from utils.env import PATH_PDF


def excel_reader():
    tabelas = camelot.read_pdf(PATH_PDF, pages='1', flavor='stream')

    if not tabelas.n:
        print("Nenhuma tabela encontrada no PDF.")
        return

    df = tabelas[0].df
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    # print(df)

    try:
        c1 = df.iloc[4, 1]
        c2 = df.iloc[4, 2]
        c3 = df.iloc[4, 3]
        c4 = df.iloc[1, 1]

        print(f"MERCADO INTERNO - {c1}")
        print(f"MERCADO EXTERNO - {c2}")
        print(f"MERCADO TOTAL - {c3}")
        print(c4)
    except IndexError:
        print("Erro ao acessar índices do DataFrame. Verifique a estrutura da tabela extraída.")
