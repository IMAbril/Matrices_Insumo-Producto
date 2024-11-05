"""
Grupo 10
TP 1 Álgebra Lineal Computacional 2c 2024
"""

import numpy as np
from scipy.linalg import solve_triangular
import pandas as pd
import matplotlib.pyplot as plt
import scipy.linalg as lng

# Toma una matriz cuadrada de nxn y devuelve tres matrices L,U,P de nxn tales que PA = LU, 
# donde L es triangular inferior, U es triangular superior y P es una matriz de permutación de filas que surge del pivoteo parcial
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
        
        

        #Recorro las filas a partir de la i+1 calculando los factores que deben multiplicar a la fila i para 
        #restarselas a estas filas (y triangular). Luego actualizo estas filas usando eso y guardo en L los 
        #multiplicadores usados. 
        for j in range(i+1,n):                        
            multiplicador = U[j][i] / U[i][i]         
            L[j][i] = multiplicador                   
            fila_i = U[i]                             
            multiplo_fila_i = multiplicador * fila_i   
            fila_j = U[j]                             
            nueva_fila_j = fila_j - multiplo_fila_i   
            U[j] = nueva_fila_j                       
                                   
    
    return L, U, P

# Toma tres matrices L, U, P de nxn y devuelve la inversa de LU o de A si PA=LU. L debe ser triangular inferior, U triangular superior y P una matriz de permutación.
# Para resolver esto se plantea la ecuacion LUX = I, que se separa en LY = I y UX = Y 
def inversaLU(L, U, P=None):
    Inv = []
    # su código
    L = np.array(L)
    U = np.array(U)
    n = L.shape[0]
    I = np.eye(n)
    Y = resolver_ecuacion(L,I,True)    # Resuelve la ecuacion L @ Y = I
    X = resolver_ecuacion(U,Y,False)    # Resuelve la ecuacion U @ X = Y hallando X que es la inversa de LU o de A
    Inv = X
    if P is not None: 
        Inv = X@P
    return Inv

# Toma dos matrices T y S de nxn, y un parámetro booleano para indicar si T es triangular inferior o no.
# La T pasada debe ser una matriz triangular 
# Devuelve una matriz X de nxn tal que TX = S  
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

#Toma una matriz A en C^nxn, un vector columna inicial v en C^n y un natural n para las iteraciones 
#Devuelve el mayor autovalor para n  (coeficiente de Rayleigh)
def metodoPotencia(A, v, n):
    v_k = v
    for k in range(n):
        v_k = A@v_k
        v_k = (v_k )/lng.norm(v_k) 
        r_k = (v_k.T @ A @ v_k ) / (v_k.T @ v_k)
    return r_k         

#Toma una matriz A en C^nxn y un natural n para las iteraciones que por defecto es 250
#Devuelve el promedio de los autovalores de las n iteraciones de Monte Carlo de la matriz A y el desvío estándar
def monteCarlo(A, n=250):
    autovalores = []
    for _ in range(n):
        v = np.random.rand(A.shape[0])
        autovalor = metodoPotencia(A, v, n)
        autovalores.append(autovalor)
    
    promedio = np.mean(autovalores)
    desv_estandar = np.std(autovalores)
    
    return promedio, desv_estandar


#Toma una matriz A de mxm y un numero n entero mayor o igual a 0, y devuelve dos listas.
# La lista normas_inversa tiene en la posicion i la norma de la inversa de I-A,  donde I-A 
# se calcula con la serie de potencias hasta el exponente i de A, con 0<=i<=n 
# La lista potencias guarda en el lugar i la potencia correspondiente al lugar i de normas_inversa
def normas_de_series_de_potencias(A,n):
    I_menos_A_inv = np.zeros((A.shape[0],A.shape[1]))
    normas_inversa = []
    potencias = []
    for i in range(0,n+1):
        I_menos_A_inv = I_menos_A_inv + np.linalg.matrix_power(A,i)
        potencias.append(i)
        norma = np.linalg.norm(I_menos_A_inv)
        normas_inversa.append(norma)
    return potencias,normas_inversa


# Toma una matriz A de nxn y un numero e con 0 < e < 1. 
# Devuelve el autovalor de modulo máximo de A.
# La función realiza el método de la potencia utilizando como criterio de parada que entre una iteracion
# y la siguiente, la norma de la diferencia de los autovectores sea <= 1 - e. Se establece
# un limite de iteraciones máximo por si el autovector comienza a oscilar.    
def metodo_potencia_hotelling(A,e):
    x0 = np.random.rand(A.shape[0])
    x0 = x0 / np.linalg.norm(x0,2)
    xk = A @ x0 / np.linalg.norm(A @ x0,2)
    i = 0
    while True:
        xk_1 = A @ xk / np.linalg.norm(A @ xk, 2)
        if np.linalg.norm(xk_1 - xk,2) <= 1 - e or i > 100000:
            xk = xk_1
            break
        else:
            xk = xk_1
            i += 1
    rayleigh = xk.transpose() @ A @ xk / (xk.transpose() @ xk)
    return xk, rayleigh 
    



