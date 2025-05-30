from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def antreneaza_si_evalueaza_model(X_train, X_test, y_train, y_test, feature_names):
    modele = {
        "Regresie Logistică": LogisticRegression(max_iter=1000),
        "SVM": SVC(kernel='linear'),
        "Arbore Decizional": DecisionTreeClassifier()
    }

    for nume, model in modele.items():
        print(f"\n--- {nume} ---")
        model.fit(X_train, y_train)
        predictii = model.predict(X_test)
        print(confusion_matrix(y_test, predictii))
        print(classification_report(y_test, predictii))

        if nume == "Arbore Decizional":
            importances = model.feature_importances_
            plt.figure(figsize=(10, 6))
            sns.barplot(x=importances, y=feature_names, palette="viridis")
            plt.title("Importanța variabilelor în arborele decizional")
            plt.xlabel("Importanță")
            plt.ylabel("Variabilă predictivă")
            plt.grid(True)
            plt.tight_layout()
            plt.savefig("grafic_importanta_variabile.jpg", format="jpg", dpi=300)
            plt.show()
            plt.close()


def clustering_kmeans(df, features, nr_grupuri=3):
    kmeans = KMeans(n_clusters=nr_grupuri, random_state=42)
    df_cluster = df.copy()
    df_cluster['Cluster'] = kmeans.fit_predict(df[features])

    print("\n--- Distribuția respondenților pe clustere ---")
    print(df_cluster['Cluster'].value_counts())

    x_var = 'Scor general satisfacție'
    y_var = 'Scor aplicație mobilă'

    if x_var in features and y_var in features:
        plt.figure(figsize=(10, 7))
        sns.scatterplot(
            data=df_cluster,
            x=x_var,
            y=y_var,
            hue='Cluster',
            palette='Set2',
            s=70,
            edgecolor='black')

        centroids = kmeans.cluster_centers_
        plt.scatter(
            centroids[:, features.index(x_var)],
            centroids[:, features.index(y_var)],
            s=200,
            marker='X',
            c='black',
            label='Centroid',
            alpha=0.6
        )

        plt.title("Clustering K-means al clienților în funcție de satisfacție și aplicație")
        plt.xlabel("Scor general satisfacție (1 – foarte mic, 5 – foarte mare)")
        plt.ylabel("Scor aplicație mobilă (1 – foarte slab, 5 – foarte bun)")
        plt.legend(title="Cluster")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("clustering_kmeans.jpg", format="jpg", dpi=300)
        plt.show()
        plt.close()

    else:
        print(f"Variabilele '{x_var}' și '{y_var}' nu se află în lista de features pentru grafic.")

    return df_cluster