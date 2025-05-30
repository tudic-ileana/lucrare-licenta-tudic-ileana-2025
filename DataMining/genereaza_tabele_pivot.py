import pandas as pd

# Încarcă fișierul CSV cu datele colectate
df = pd.read_csv("raspunsuri_participanti.csv")

# Tabel 1 – Scoruri medii pe gen
pivot_sex = df.groupby("Sex")[[
    'Scor interacțiune personal',
    'Scor claritate comisioane',
    'Scor rapiditate soluționare',
    'Scor aplicație mobilă',
    'Scor platformă online',
    'Scor general satisfacție'
]].mean().round(2)

# Tabel 2 – Scoruri medii pe vârstă
pivot_age = df.groupby("Vârstă")[[
    'Scor interacțiune personal',
    'Scor claritate comisioane',
    'Scor rapiditate soluționare',
    'Scor aplicație mobilă',
    'Scor platformă online',
    'Scor general satisfacție'
]].mean().round(2)

# Tabel 3 – Scoruri medii în funcție de utilizarea aplicației
pivot_app = df.groupby("Foloseste aplicația")[[
    'Scor interacțiune personal',
    'Scor claritate comisioane',
    'Scor rapiditate soluționare',
    'Scor aplicație mobilă',
    'Scor platformă online',
    'Scor general satisfacție'
]].mean().round(2)

# Tabel 4 – Scoruri medii pe localitate
pivot_loc = df.groupby("Localitate")[[
    'Scor interacțiune personal',
    'Scor claritate comisioane',
    'Scor rapiditate soluționare',
    'Scor aplicație mobilă',
    'Scor platformă online',
    'Scor general satisfacție'
]].mean().round(2)

# Tabel 5 – Statistici descriptive generale
summary_table = df[[
    'Scor interacțiune personal',
    'Scor claritate comisioane',
    'Scor rapiditate soluționare',
    'Scor aplicație mobilă',
    'Scor platformă online',
    'Scor general satisfacție'
]].agg(['mean', 'min', 'max']).round(2).transpose()

# Export toate tabelele intr-un singur fișier excel
with pd.ExcelWriter("tabele_feedback.xlsx") as writer:
    pivot_sex.to_excel(writer, sheet_name="Scoruri pe gen")
    pivot_age.to_excel(writer, sheet_name="Scoruri pe varsta")
    pivot_app.to_excel(writer, sheet_name="Scoruri pe aplicatie")
    pivot_loc.to_excel(writer, sheet_name="Scoruri pe localitate")
    summary_table.to_excel(writer, sheet_name="Statistici descriptive")

print("Fișierul tabele_feedback.xlsx a fost generat cu succes.")