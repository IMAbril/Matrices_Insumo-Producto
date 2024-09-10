import numpy as np
from scipy.linalg import solve_triangular
# Toma una matriz cuadrada de nxn y devuelve dos matrices L y U de nxn tales que A = L@U, donde L es triangular inferior y U es triangular superior
def calcularLU(A):
    L, U = [],[]
    # su código
    U = np.array(A,dtype=float)           
    n = U.shape[0]                                    # Obtengo las dimensiones de A  
    L = np.eye(n)
    for i in range(0,n-1):                            # Recorro las filas que tienen el pivot
        for j in range(i+1,n):                        # Recorro las filas a las que se les va a restar un múltiplo de la fila que tiene el pivot 
            multiplicador = U[j][i] / U[i][i]         # Calculo el factor por el que hay que multiplicar la fila i (la del pivot) para restarsela a la j 
            L[j][i] = multiplicador                   # Guardo el multiplicador en la matriz L donde corresponde
            fila_i = U[i]                             # Obtengo la fila i
            multiplo_fila_i = multiplicador * fila_i  # Calculo el multiplo de la fila i 
            fila_j = U[j]                             # Guardo la fila j
            nueva_fila_j = fila_j - multiplo_fila_i   # Calculo la nueva fila j que resulta de restarle el multiplo de la fila i  
            U[j] = nueva_fila_j                       # Actualizo la fila j  

    ###########
    return L, U

# Toma dos matrices L y U de nxn y devuelve la inversa de L@U.
# Para esto se plantea la ecuacion L@U@X = id, que se separa en L@Y = id y U@X = Y 
def inversaLU(L, U):
    Inv = []
    # su código
    L = np.array(L)
    U = np.array(U)
    n = L.shape[0]
    id = np.eye(n)
    Y = resolver_ecuacion(L,id,True)    # Resuelve la ecuacion L @ Y = id
    X = resolver_ecuacion(U,Y,False)    # Resuelve la ecuacion L @ X = Y hallando X que es la inversa de LU 
    Inv = X
    
    return Inv

# Toma dos matrices T y S de nxn, y un parámetro booleano para indicar si T es triangular inferior o no.
# La T pasada debe ser una matriz triangular 
# Devuelve una matriz X de nxn tal que T@X = S  

def resolver_ecuacion(T,S,es_inferior):
    T = np.array(T,dtype=float)
    S = np.array(S,dtype=float).transpose()                                 # Traspongo S para obtener sus columnas
    n = T.shape[0]                                                          # Obtengo las dimensiones de T
    X = []
    for i in range(n):                                                      # Resuelvo los sistemas T X(i) = S(i) donde X(i) va a ser la columna i de X
        columna_i_S = S[i]                                                  # Obtengo S(i)  (columna i de S)                                               
        columna_i_X = solve_triangular(T,columna_i_S,lower=es_inferior)     # Obtengo X(i)
        X.append(columna_i_X)                                               # Agrego X(i) como fila a X
    return np.array(X).transpose()                                          # Traspongo X que tenia las columnas como filas 




L,U = calcularLU([[1,2,0],[2,0,2],[3,1,0]])
print(L)
print(U)
print(L@U)
print(inversaLU(L,U) @ (L@U))