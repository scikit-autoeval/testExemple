import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.impute import KNNImputer
from sklearn.pipeline import make_pipeline
from xgboost import XGBClassifier

# Carregar datasets
fraude_2024 = pd.read_csv("./datasets/fraude-2024-controle.csv")
fraude_2025 = pd.read_csv("./datasets/fraude-2025-controle.csv")

# Separar atributos e rótulos
atributos_treino, rotulos_treino = fraude_2024.drop(columns=["Fraude"]), fraude_2024["Fraude"]
atributos_teste = fraude_2025.drop(columns=["Fraude"])

# Definir modelos
modelo = make_pipeline(
    KNNImputer(n_neighbors=5),
    XGBClassifier()
)

# Definir métricas de avaliação
metricas = {
    "accuracy": accuracy_score,
    "f1_macro": lambda y, p: f1_score(y, p, average="macro")
}