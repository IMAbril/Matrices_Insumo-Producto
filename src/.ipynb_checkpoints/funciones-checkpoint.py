import numpy as np
from scipy.linalg import solve_triangular

""" Toma una matriz cuadrada de nxn y devuelve tres matrices matrices L,U,P de nxn tales que P@A = L@U, 
donde L es triangular inferior y U es triangular superior"""
def calcularLU(A):
    L, U = [],[]
    P = None
    # su código
    U = A.copy()
    U = np.array(U,dtype=float)
    n = U.shape[0]
    L = np.eye(n)
    P = np.eye(n)
    for i in range(n-1):                            # Recorro las filas de U hasta la anteúltima. 
        pivot = U[i][i]                              
        fila_a_intercambiar = i                     # Acá voy a guardar el numero de fila que se debe intecambiar con la fila i 
        
        for j in range(i+1,n):                      # Recorro desde la fila i+1 hasta la n en busca de aquella con el pivot de mayor valor absoluto
            posible_nuevo_pivot = U[j][i]
            if abs(posible_nuevo_pivot) > abs(pivot):
                pivot = posible_nuevo_pivot
                fila_a_intercambiar = j 

        if(fila_a_intercambiar != i):               # Si la fila por la que hay que intercambiar la fila i es distinta de i, entonces hago los intercambios en U y P
            U[[i,fila_a_intercambiar]] = U[[fila_a_intercambiar,i]]     #Intercambio la fila i con fila_a_intercambiar
            P[[i,fila_a_intercambiar]] = P[[fila_a_intercambiar,i]]
            if i > 0:                               # Intercambio los multiplicadores que estan en L de acuerdo al intercambio de filas que se hizo en U. 
                L[[i, fila_a_intercambiar], :i] = L[[fila_a_intercambiar, i], :i]
        
        

        """ Recorro las filas a partir de la i+1 calculando los factores que deben multiplicar a la fila i para 
        restarselas a estas filas (y triangular). Luego actualizo estas filas usando eso y guardo en L los 
        multiplicadores usados. """
        for j in range(i+1,n):                        
            multiplicador = U[j][i] / U[i][i]         
            L[j][i] = multiplicador                   
            fila_i = U[i]                             
            multiplo_fila_i = multiplicador * fila_i   
            fila_j = U[j]                             
            nueva_fila_j = fila_j - multiplo_fila_i   
            U[j] = nueva_fila_j                       
                                   
    ###########
    return L, U, P

# Toma tres matrices L, U, P de nxn y devuelve la inversa de L@U o de A si PA=LU. L debe ser triangular inferior, U triangular superior y P una matriz de permutación.
# Para resolver esto se plantea la ecuacion L@U@X = I, que se separa en L@Y = I y U@X = Y 
def inversaLU(L, U, P=None):
    Inv = []
    # su código
    L = np.array(L)
    U = np.array(U)
    n = L.shape[0]
    I = np.eye(n)
    Y = resolver_ecuacion(L,I,True)    # Resuelve la ecuacion L @ Y = I
    X = resolver_ecuacion(U,Y,False)    # Resuelve la ecuacion U @ X = Y hallando X que es la inversa de LU 
    Inv = X
    if P != None: 
        Inv = X@P
    ###########
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

