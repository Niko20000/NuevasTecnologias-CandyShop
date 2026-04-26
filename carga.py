import pandas as pd

def carga_clientes():
    df_archivo = pd.read_csv('data/raw/clientes.csv')
    df_archivo.info()
    return df_archivo

def carga_compras():
    df_compras = pd.read_csv('data/raw/compras.csv')
    df_compras.info()
    return df_compras