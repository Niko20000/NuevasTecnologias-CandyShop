from src.data_cleaning import load_data, clean_data

def main():
    df = load_data('data/orders.csv')
    print("Datos originales:")
    print(df)

    df_clean = clean_data(df)

    print("\nDatos limpios:")
    print(df_clean)

    print("\nVentas por categoría:")
    print(df_clean.groupby('category')['quantity'].sum())

if __name__ == "__main__":
    main()
