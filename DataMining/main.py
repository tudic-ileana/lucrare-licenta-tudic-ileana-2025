from data_loader import incarca_date, inspecteaza_date
from descriptiva import analiza_descriptiva, tabele_pivot
from preprocesare import codificare_categorii, standardizare_variabile, imparte_date
from modele import antreneaza_si_evalueaza_model, clustering_kmeans
from interpretare import concluzii_clasificare, concluzii_clustering, sugestii_strategice
from vizualizari_avansate import vizualizari_avansate

# 1. Încarca date
cale_fisier = "raspunsuri_participanti.csv"
df = incarca_date(cale_fisier)

# 2. Inspecteaza datele
inspecteaza_date(df)

# 3. Analiza descriptivă
analiza_descriptiva(df)

# 3.1 Vizualizari suplimentar pentru interpretare
vizualizari_avansate(df)

# 4. Tabele pivot
tabele_pivot(df)

# 5. Preprocesare date
df_codificat = codificare_categorii(df)

# Separam coloanele pentru clasificare vs. clustering
features_model = [
    'Scor interacțiune personal',
    'Scor claritate comisioane',
    'Scor rapiditate soluționare',
    'Scor aplicație mobilă',
    'Scor platformă online',
    'Sex', 'Vârstă', 'Foloseste aplicația'
]

features_clustering = features_model + ['Scor general satisfacție']

# 6. Clasificare: standardizare + imparțire + modele
df_std = standardizare_variabile(df_codificat, features_model)
X_train, X_test, y_train, y_test = imparte_date(df_std, features_model, 'Recomandă banca')
antreneaza_si_evalueaza_model(X_train, X_test, y_train, y_test, feature_names=features_model)

# 7. Clustering (K-means)
df_clusters = clustering_kmeans(df_codificat, features=features_clustering, nr_grupuri=3)

# 8. Interpretari finale
concluzii_clasificare()
concluzii_clustering()
sugestii_strategice()