def analizar(df):

    # Análisis 1: Dulce más vendido
    mas_vendido = df.groupby('Nombre')['cantidad'].sum().idxmax()
    total       = df.groupby('Nombre')['cantidad'].sum().max()
    print(f' Dulce más vendido: {mas_vendido} con {total} unidades')

    # Análisis 2: Ingresos por vendedor
    df['ingreso'] = df['precio'] * df['cantidad']
    ingresos = df.groupby('vendedor')['ingreso'].sum()
    print(' Ingresos por vendedor:')
    print(ingresos)

    # Análisis 3: Ventas mayores a 10 unidades
    grandes = df[df['cantidad'] > 10].shape[0]
    print(f' Ventas mayores a 10 unidades: {grandes}')
