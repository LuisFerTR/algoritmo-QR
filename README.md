# Algoritmo QR

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sea *A* una matriz real de la que queremos calcular sus eigenvalores. Luego, sea
1. *A*<sub>0</sub> := *A*
2. Para *i* = 0, 1, 2, ..., n iteraciones hacer: <br>
    a) Hallar la factorización *A*<sub>i</sub> = *Q*<sub>i</sub>*R*<sub>i</sub> <br>
    b) *A*<sub>i+1</sub> = *R*<sub>i</sub>*Q*<sub>i</sub> <br> 
    c) Repetir a) hasta que *A*<sub>i+1</sub> sea una matriz triangular superior.

Donde la matriz *Q*<sub>i</sub> es una matriz ortogonal y *R*<sub>i</sub> es una matriz triangular superior.