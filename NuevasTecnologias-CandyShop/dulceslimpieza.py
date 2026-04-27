import pandas as pd

def cargar(dulces_sucios.csv):
    return pd.read_csv(dulces_sucios.csv)

def limpiar_los_datos(df):
    # Quitamos filas totalmente vacías 
    df = df.dropna(how='all')
    
    # Aquitar el $ y los espacios para que sean números
    if 'precio' in df.columns:
        df['precio'] = df['precio'].astype(str).str.replace('$', '').str.strip()
        df['precio'] = pd.to_numeri(df['precio'], errors='coerce')
    
    # Si falta la cantidad, le ponemos 0 
    if 'cantidad' in df.columns:
        df['cantidad'] = df['cantidad'].fillna(0)
    
    # Borramos registros repetidos
    df = df.drop_duplicates()
    return df

def unir_tablas(df_ventas, df_nombres):
    # Hacemos el merge usando el ID del dulce
    return pd.merge(df_ventas, df_nombres, on='id_dulce')