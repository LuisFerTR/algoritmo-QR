import numpy as np
from Gram_Schmidt import Gram_Schmidt

def esTriangSup(matriz):
    return np.allclose(matriz, np.triu(matriz), rtol=1e-4, atol=1e-4)

def factQR(A):
    Q = Gram_Schmidt(A)
    R = Q.transpose().dot(A)

    return Q, R

def QR(originalA):
    np.set_printoptions(suppress=True,
                        formatter={'float_kind':'{:0.5f}'.format})
    A = np.copy(originalA)   
    i = 0                 
    while not esTriangSup(A):
        Q, R = factQR(A)
        print(f"Q{i} = ", Q)
        print(f"R{i} = ", R)
        A = np.dot(R,Q)
        i += 1

    return A
