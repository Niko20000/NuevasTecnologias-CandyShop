from dulceslimpieza.py import 
def ejecutar_proyecto():
    print("Iniciando el analisis de dulces...")
    
    # 1. Cargar datos
    datos_sucios = cargar_mi_csv('data/dulces_sucios.csv')
    nombres_dulces = cargar_mi_csv('data/info_productos.csv')
    
    # 2. Preprocesamiento
    ventas_ok = limpiar_los_datos(datos_sucios)
    
    # 3. Union de tablas (Merge)
    df_final = unir_tablas(ventas_ok, nombres_dulces)
    
    print("\RESULTADOS )
    
    # Pregunta 1: El mas vendido (frecuencia)
    mas_popular = df_final['nombre_dulce'].value_counts().idxmax()
    print(f"El dulce que mas aparece en ventas es: {mas_popular}")
    
    # Pregunta 2: Promedio de precio por categoria (agregacion)
    promedio_cat = df_final.groupby('categoria')['precio'].mean()
    print("\nPromedio de precios por categoria:")
    print(promedio_cat)
    
    # Pregunta 3: Ventas grandes (filtrado y conteo)
    # Vamos a contar cuantas ventas fueron de mas de 10 unidades
    ventas_grandes = df_final[df_final['cantidad'] > 10].shape[0]
    print(f"\nCantidad de ventas mayores a 10 unidades: {ventas_grandes}")

if __name__ == "__main__":
    ejecutar_proyecto()