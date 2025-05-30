import pandas as pd

def incarca_date(cale_fisier):
    """
    Incarcă datele din fișierul CSV specificat si returnează un DataFrame.
    """
    df = pd.read_csv(cale_fisier)
    return df

def inspecteaza_date(df):
    """
    Afișeaza informații generale despre date: primele rânduri, tipuri de date, valori unice
    """
    print("\n--- Primele 5 rânduri ---")
    print(df.head())

    print("\n--- Informații generale ---")
    print(df.info())

    print("\n--- Statistici descriptive ---")
    print(df.describe(include='all'))

    print("\n--- Valori unice per coloană ---")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} valori unice")
