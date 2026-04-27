import pandas as pd

def limpiar_y_unir():

    # Cargar archivos
    ventas    = pd.read_csv('data/dulces_sucios.csv')
    productos = pd.read_csv('data/info_productos.csv')

    # Limpiar precio: quitar $ y espacios
    ventas['precio'] = ventas['precio'].astype(str).str.replace('$', '', regex=False).str.strip()
    ventas['precio'] = pd.to_numeric(ventas['precio'], errors='coerce')

    # Eliminar filas con precio o cantidad inválidos
    ventas = ventas.dropna(subset=['precio', 'cantidad'])
    ventas = ventas[ventas['precio'] > 0]

    # Eliminar duplicados
    ventas = ventas.drop_duplicates()

    # Convertir cantidad a entero
    ventas['cantidad'] = ventas['cantidad'].astype(int)

    # Unir con info de productos
    df_final = pd.merge(ventas, productos, on='id_dulce', how='inner')

    print(f' Registros limpios y unidos: {len(df_final)}')
    return df_final
