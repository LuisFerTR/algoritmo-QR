import numpy as np

def Gram_Schmidt(A):
    """
    A: Matriz donde cada columna es un vector de la base
    del espacio vectorial.

    Devuelve una matriz donde cada columna es un vector
    de una base ortonormal del espacio vectorial.
    """
    filas, columnas = A.shape

    # Crear matriz de ceros del tamaño de A
    base_ortonormal = np.zeros((filas,columnas), np.float64)

    base_ortonormal[:,0] = np.copy(A[:,0]) / np.linalg.norm(A[:,0])

    # wi = vi - (Σ[(<vi,wj> / <wj,wj>)]wj), j = 1, 2, 3, ..., i-1
    for i in range(1, columnas):
        vi = np.copy(A[:,i] )
        wi = vi
        for j in reversed(range(i)):
            wj = np.copy(base_ortonormal[:,j])
            cociente = np.dot(vi, wj) / np.dot(wj,wj)  # <vi,wj> / <wj,wj>
            wi -= cociente * wj  
            # ui = wi / ‖wi‖, i = 1, 2, 3, ..., n
            ui = wi / np.linalg.norm(wi)

        base_ortonormal[:,i] = ui

    base_ortonormal = np.round(base_ortonormal,10)
    return base_ortonormal
