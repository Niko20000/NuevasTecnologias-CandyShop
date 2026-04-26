import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
 
    df = df.dropna()

    
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

   
    df = df.dropna()
    df = df[df['quantity'] > 0]

    
    df['product'] = df['product'].str.lower().str.strip()
    df['category'] = df['category'].str.lower().str.strip()

    return df
