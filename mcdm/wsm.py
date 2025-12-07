import numpy as np
import pandas as pd

def wsm(matrix, weights, types):
    """
    Weighted Sum Model (WSM)

    matrix: dataframe con criterios
    weights: vector de pesos normalizados
    types: lista con 'beneficio' o 'costo'
    """

    M = matrix.values.astype(float)

    # Normalización min-max por criterio
    norm = np.zeros_like(M)
    for j in range(M.shape[1]):
        col = M[:, j]
        minv, maxv = col.min(), col.max()

        # Evitar división por 0
        if maxv - minv == 0:
            norm[:, j] = 0
        else:
            # Normalización dependiendo del tipo
            if types[j] == "beneficio":
                norm[:, j] = (col - minv) / (maxv - minv)
            else:  # costo
                norm[:, j] = (maxv - col) / (maxv - minv)

    # WSM = sumatoria(w_i * x_ij)
    scores = np.dot(norm, weights)

    return scores, norm
