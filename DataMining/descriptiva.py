import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analiza_descriptiva(df):
    """
    Calculează medii si distribuții pentru fiecare scor de satisfacție.
    """
    scoruri = [
        'Scor interacțiune personal',
        'Scor claritate comisioane',
        'Scor rapiditate soluționare',
        'Scor aplicație mobilă',
        'Scor platformă online',
        'Scor general satisfacție'
    ]

    medii = df[scoruri].mean().round(2)
    print("\n--- Medii scoruri satisfacție ---")
    print(medii)

    df[scoruri].hist(bins=5, figsize=(12, 8), layout=(2, 3))
    plt.suptitle("Distribuția scorurilor de satisfacție")
    plt.tight_layout()
    plt.show()


def tabele_pivot(df):
    """
    Creează tabele pivot pentru analiza comparativă a scorurilor medii.
    """
    scoruri = [
        'Scor interacțiune personal',
        'Scor claritate comisioane',
        'Scor rapiditate soluționare',
        'Scor aplicație mobilă',
        'Scor platformă online',
        'Scor general satisfacție'
    ]

    print("\n--- Scoruri medii pe gen ---")
    print(df.pivot_table(values=scoruri, index='Sex', aggfunc='mean').round(2))

    print("\n--- Scoruri medii pe vârstă ---")
    print(df.pivot_table(values=scoruri, index='Vârstă', aggfunc='mean').round(2))

    print("\n--- Scoruri medii în funcție de utilizarea aplicației ---")
    print(df.pivot_table(values=scoruri, index='Foloseste aplicația', aggfunc='mean').round(2))