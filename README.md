# lucrare-licenta-tudic-ileana-2025

# Analiza satisfactiei clientilor bancari folosind tehnici de Data Mining



## Descriere generala

Aceasta aplicatie realizeaza analiza unui set de date colectate printr-un chestionar online despre perceptia si satisfactia clientilor in relatia cu serviciile bancare. Scopul este de a identifica tipare relevante si factori care influenteaza satisfactia generala, utilizand Python si librarii de analiza statistica si machine learning.

Analiza include:
- preprocesarea datelor brute
- statistici descriptive si vizualizari
- clasificare cu arbori de decizie, regresie logistica si SVM
- clustering cu algoritmul KMeans
- generarea automata a tabelelor pivot

---

## Structura fisierelor

- `main.py` – punctul de pornire, executa analiza completa
- `data_loader.py` – incarca si curata datele
- `descriptiva.py` – calculeaza medii, frecvente si statistici
- `genereaza_tabele_pivot.py` – genereaza tabele pivot segmentate
- `interpretare.py` – ruleaza modele de clasificare si clustering

---

## Cerinte de rulare

Ai nevoie de Python 3.8+ si urmatoarele librarii:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
