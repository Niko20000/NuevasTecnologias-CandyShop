import pandas as pd

def analisis(df_compras):

    print("Traer las personas por ciudad")
    print("Bogota")
    marcara_bogota = df_compras["ciudad"] == "Bogota"
    df_ciudad_bogota = df_compras[marcara_bogota]
    print(df_ciudad_bogota)



    df_compras["compras"] = df_compras["compras"].str.replace("$","").astype(float)
    print("Traer las compras mayores a 10000")
    mascara_compras = df_compras["compras"] > 10000
    df_compras_altas = df_compras[mascara_compras]
    print(df_compras_altas)

    print(" \n Promedio de compras")
    print(df_compras["compras"].mean())
    print(" \n Total de compras ")
    print(df_compras["compras"].sum())

    print(" \n Total de compras, por ciudad")
    ventas_por_ciudad = df_compras.groupby('ciudad')["compras"].agg(['sum', 'mean'])
    df_compras_ordenado = ventas_por_ciudad.sort_values(by='sum', ascending=False)
    print(df_compras_ordenado)
