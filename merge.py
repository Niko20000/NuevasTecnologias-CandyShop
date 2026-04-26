import pandas as pd

def merge():
    df_cliente = pd.read_csv('data/processed/clientes_limpio.csv')
    df_compras = pd.read_csv('data/processed/compras_limpio.csv')
    df_clientes_compras = df_compras.merge(df_cliente, on="id", how="left")
    df_clientes_compras.to_csv('data/processed/clientes_compras.csv', index=False)
    return df_clientes_compras