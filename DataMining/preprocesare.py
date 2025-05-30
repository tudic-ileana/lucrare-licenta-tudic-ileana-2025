import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def codificare_categorii(df):
    """
    Codifică variabilele categorice în format numeric.
    """
    codificat = df.copy()
    codificat['Sex'] = codificat['Sex'].map({'Feminin': 0, 'Masculin': 1})
    codificat['Foloseste aplicația'] = codificat['Foloseste aplicația'].map({'Nu': 0, 'Da': 1})
    codificat['Recomandă banca'] = codificat['Recomandă banca'].map({'Nu': 0, 'Da': 1})
    codificat['Vârstă'] = codificat['Vârstă'].map({
        '<25': 1, '25–34': 2, '35–44': 3, '45–54': 4, '55+': 5
    })
    return codificat


def standardizare_variabile(df, coloane):
    """
    Aplică standardizare (scalare) pe coloanele indicate.
    """
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[coloane] = scaler.fit_transform(df[coloane])
    return df_scaled


def imparte_date(df, coloane_features, coloana_tinta):
    """
    Împarte setul de date în X_train, X_test, y_train, y_test.
    """
    X = df[coloane_features]
    y = df[coloana_tinta]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

