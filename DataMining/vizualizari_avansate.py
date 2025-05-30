import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def vizualizari_avansate(df):
    scoruri = [
        'Scor interacțiune personal',
        'Scor claritate comisioane',
        'Scor rapiditate soluționare',
        'Scor aplicație mobilă',
        'Scor platformă online',
        'Scor general satisfacție'
    ]

    # 1. Heatmap de corelații
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[scoruri].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Corelații între dimensiunile satisfacției")
    plt.tight_layout()
    plt.savefig("corelatii_scoruri.png", dpi=300)
    plt.close()

    # 2. Boxplot - scor aplicație mobilă pe grupe de vârstă
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Vârstă', y='Scor aplicație mobilă', palette="Set3")
    plt.title("Distribuția scorului aplicației mobile pe grupe de vârstă")
    plt.xlabel("Grupa de vârstă")
    plt.ylabel("Scor aplicație mobilă")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("boxplot_aplicatie_vs_varsta.png", dpi=300)
    plt.close()

    # 3. Bar chart - scoruri medii pe gen
    medii_sex = df.groupby('Sex')[scoruri].mean()
    medii_sex.T.plot(kind='bar', figsize=(10, 6), colormap='Set2')
    plt.title("Scoruri medii ale satisfacției în funcție de gen")
    plt.xlabel("Dimensiune evaluată")
    plt.ylabel("Scor mediu")
    plt.xticks(rotation=45)
    plt.legend(title="Gen")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("medii_scoruri_pe_sex.png", dpi=300)
    plt.close()

    # 4. Bar chart - scoruri medii pe vârstă
    medii_varsta = df.groupby('Vârstă')[scoruri].mean()
    medii_varsta.T.plot(kind='bar', figsize=(10, 6), colormap='Pastel1')
    plt.title("Scoruri medii ale satisfacției în funcție de vârstă")
    plt.xlabel("Dimensiune evaluată")
    plt.ylabel("Scor mediu")
    plt.xticks(rotation=45)
    plt.legend(title="Vârstă")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("medii_scoruri_pe_varsta.png", dpi=300)
    plt.close()
