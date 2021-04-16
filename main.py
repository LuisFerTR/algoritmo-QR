import numpy as np
from QR import QR

orden = int(input("Introduce el orden de la matriz: "))

A = np.zeros((orden,orden), np.float64)

for i in range(orden):
    for j in range(orden):
        A[i,j] = float(input(f"Elemento[{i+1}:{j+1}]: "))


finalA = QR(A)

print("\nEigenvalores: ")

for i in range(orden):
    for j in range(orden):
        if i == j:
            print(f"{finalA[i,j]}", end=", ")

