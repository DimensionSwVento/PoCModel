import pandas as pd

from mcdm.ahp import compute_weights, consistency_ratio
from mcdm.topsis import topsis
from mcdm.wsm import wsm
from visualization.folium_map import create_map

# 1. Cargar alternativas
alts = pd.read_csv("data/alternatives.csv")

# Extraemos los criterios
matrix = alts.drop(columns=["id", "nombre", "lat", "lon"])

# 2. Cargar criterios y sus tipos
df_criterios = pd.read_csv("data/criteria.csv")

criterios = df_criterios["criterio"].tolist()
tipos = df_criterios["tipo"].tolist()

assert all(c in matrix.columns for c in criterios), "ERROR: Faltan criterios en alternatives.csv"

matrix = matrix[criterios]

# 3. Cargar matriz AHP
pairwise = pd.read_csv("data/pairwise_matrix.csv", header=None).values

weights = compute_weights(pairwise)
CR = consistency_ratio(pairwise)

print("Índice de Consistencia (CR):", CR)
print("Pesos AHP:", weights)

# 4. Ejecutar TOPSIS
topsis_scores, V, ideal_pos, ideal_neg = topsis(matrix, weights, tipos)
alts["score_topsis"] = topsis_scores

# 5. Ejecutar WSM
wsm_scores, norm_matrix = wsm(matrix, weights, tipos)
alts["score_wsm"] = wsm_scores

print("\nRESULTADOS:")
print(alts[["nombre", "score_topsis", "score_wsm"]])

# 6. Crear mapas (TOPSIS y WSM)
m = create_map(alts, score_col="score_topsis")
m.save("map_topsis.html")

m2 = create_map(alts, score_col="score_wsm")
m2.save("map_wsm.html")

print("Mapas generados: map_topsis.html | map_wsm.html")
