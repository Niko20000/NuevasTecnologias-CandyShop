import pandas as pd

def limpiar_clientes(df_archivo):
    #Limpieza de espacio y texto en formato titulo.
    print('Limpieza de espacio y texto en formato titulo')
    df_archivo['nombre'] = df_archivo['nombre'].str.strip().str.title()
    df_archivo['apellido'] = df_archivo['apellido'].str.strip().str.title()
    df_archivo['ciudad'] = df_archivo['ciudad'].str.strip().str.title()
    df_archivo['email'] = df_archivo['email'].str.lower()
    df_archivo['edad'] = df_archivo['edad'].str.strip().str.title()
    df_archivo['telefono'] = df_archivo['telefono'].str.strip().str.title()

    #Eliminar datos duplicados
    print('Eliminar datos duplicados')
    df_archivo = df_archivo.drop_duplicates()
    
    print('Reemplazar datos con un valor')
    #Reemplazar datos con un valor
    df_archivo['edad'] = df_archivo['edad'].replace('treinta', 30)
    df_archivo['edad'] = df_archivo['edad'].replace('-26', 26)
    df_archivo['edad'] = df_archivo['edad'].replace('400', 40)
    df_archivo['telefono'] = df_archivo['telefono'].replace('notphone', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('Notphone', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('Abc123456', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('invalid', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('Invalid', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('phone123', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('Phone123', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('12345', 00000000)
    df_archivo['telefono'] = df_archivo['telefono'].replace('0', 00000000)

    df_archivo['edad'] = pd.to_numeric(df_archivo['edad'], errors='coerce').fillna(0).astype(int)

    #print(df_archivo['edad'].value_counts())

    print('Tratamiento de Nulos')
    #Tratamiento de Nulos
    df_archivo['edad'] = df_archivo['edad'].fillna(df_archivo['edad'].mean())
    df_archivo['ciudad'] = df_archivo['ciudad'].fillna('desconocida')
    df_archivo['telefono'] = df_archivo['telefono'].fillna(00000000)
    df_archivo['edad'] = df_archivo['edad'].replace(0, df_archivo['edad'].mean())


    #df_archivo.info()

# Lista oficial (solo las ciudades que usamos en tus datos)
    ciudades_oficiales = ['Bogota', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena']
    
    # Usamos ~ (NOT) para buscar a los que violan la regla de la lista
    mascara_infractores = ~df_archivo['ciudad'].isin(ciudades_oficiales)

    # Filtramos el DataFrame usando la máscara para ver los errores
    errores_detectados = df_archivo[mascara_infractores]

    #Hacemos un print de los datos que no cumplen nuestra lista
    print('errores_detectados')
    print(errores_detectados)

    #Hacemos un diccionario para aplicar una traducción
    traduccion = {
    'bogota': 'Bogota',
    'BOGOTA': 'Bogota',
    'Bogotá': 'Bogota',
    'bogotá': 'Bogota',
    'BOGOTÁ': 'Bogota',
    'Bogóta': 'Bogota',

    'medellin': 'Medellin',
    'MEDELLIN': 'Medellin',
    'Medellín': 'Medellin',
    'medellín': 'Medellin',

    'cali': 'Cali',
    'CALI': 'Cali',
    ' cali ': 'Cali',

    'barranquilla': 'Barranquilla',
    'BARRANQUILLA': 'Barranquilla',

    'cartagena': 'Cartagena',
    'CARTAGENA': 'Cartagena',

    '': 'Bogota',              
    None: 'Bogota',            
    'desconocida': 'Bogota'    
    }
    
    # Aplicamos la traducción solo a la columna afectada
    df_archivo['ciudad'] = df_archivo['ciudad'].replace(traduccion)

    print('Ahora las cuidades estan limpiesitas')
    print(df_archivo['ciudad'].value_counts())

    df_archivo.info()

    # index=False evita guardar el índice de Pandas en el archivo
    df_archivo.to_csv('data/processed/clientes_limpio.csv', index=False)
    return df_archivo


def limpieza_compras(df_compras):
    print('Limpieza de espacio y texto en formato titulo')
    df_compras['producto'] = df_compras['producto'].str.strip()
    # index=False evita guardar el índice de Pandas en el archivo
    print('Eliminar datos duplicados')
    df_compras = df_compras.drop_duplicates()
    df_compras.to_csv('data/processed/compras_limpio.csv', index=False)
    return df_compras