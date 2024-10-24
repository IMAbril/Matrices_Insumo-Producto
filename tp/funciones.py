"""
Grupo 10
TP 1 Álgebra Lineal Computacional 2c 2024
"""

import numpy as np
from scipy.linalg import solve_triangular
import pandas as pd
import matplotlib.pyplot as plt

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


#Toma 2 strings p1 y p2 códigos de países y la ruta a un archivo .xlsx con las matrices de insumo producto
#de latinoamérica generadas por la CEPAL.
#Devuelve la matriz de insumo producto de p1 y p2. 
def generar_Matriz_InsumoProducto(p1, p2, data):
    df = pd.read_excel(data, sheet_name='LAC_IOT_2011')
    df = df.loc[(df['Country_iso3'] == p1) | (df['Country_iso3']==p2)]
    df = df[[col for col in df.columns if (col.startswith(p1) or col.startswith(p2) or col == 'Country_iso3' or col == 'Output')]]
    return df

#Toma 2 strings p1 y p2 códigos de país y un dataframe con la matriz insumo producto de p1 y p2
#Devuelve las submatrices intra-regionales e inter-regionales de los coeficientes técnicos de p1 y p2, y matrices columna
#con lo producido por los sectores de p1 y p2
def generar_submatrices(p1, p2, df):
    #Genero la matriz de coeficientes técnicos intraregional del país p1
    p1_df = df.loc[df['Country_iso3'] == p1] 
    z_p1p1 = p1_df[[col for col in p1_df.columns if col.startswith(p1)]] 
    producto_p1 = p1_df['Output'].copy()
    producto_p1 = producto_p1.replace(0,1) # Reemplazamos los 0 por 1 para no dividir por 0 al calcular la inversa de P (matriz diagonal con la producción)
    producto_p1_reciprocos = []
    for elem in producto_p1:
        producto_p1_reciprocos.append(1/elem)
    inversa_producto_p1 = np.diag(producto_p1_reciprocos) # Armo la inversa de P que es igual a P pero con los recíprocos en la diagonal
    A_p1p1 = z_p1p1.dot(inversa_producto_p1)
    
    
    #Genero la matriz de coeficientes técnicos intraregional del país p2
    p2_df = df.loc[df['Country_iso3'] == p2] 
    z_p2p2 = p2_df[[col for col in p2_df.columns if col.startswith(p2)]] 
    producto_p2 = p2_df['Output'].copy()
    producto_p2 = producto_p2.replace(0,1)
    producto_p2_reciprocos = []
    for elem in producto_p2:
        producto_p2_reciprocos.append(1/elem)
    inversa_producto_p2 = np.diag(producto_p2_reciprocos)
    A_p2p2 = z_p2p2.dot(inversa_producto_p2)

    #Genero la matriz de coeficientes técnicos interregional del país p2 con p1
    z_p2p1 = p2_df[[col for col in p2_df.columns if col.startswith(p1)]] 
    A_p2p1 = z_p2p1.dot(inversa_producto_p1)
    
    #Genero la matriz de coeficientes técnicos interregional del país p1 con p2
    z_p1p2 = p1_df[[col for col in p1_df.columns if col.startswith(p2)]] 
    A_p1p2 = z_p1p2.dot(inversa_producto_p2)
        
    return A_p1p1.values, A_p1p2.values, A_p2p2.values, A_p2p1.values, p1_df['Output'].values, p2_df['Output'].values
    
#Toma 2 strings p1 y p2 códigos de país y un dataframe con la matriz insumo producto de p1 y p2
#Devuelve los vectores de demanda externa de los países p1 y p2 
def obtener_demanda(p1,p2,data):
    A_p1p1, A_p1p2, A_p2p2, A_p2p1, producto_p1, producto_p2 = generar_submatrices(p1, p2, data)
    I = np.eye(40)
    dp1 = (I-A_p1p1)@producto_p1 - A_p1p2@producto_p2
    dp2 = (-A_p2p1)@producto_p1 + (I-A_p2p2)@producto_p2
    
    return dp1, dp2

#Toma un vector con los datos de la demanda externa de un país y un diccionario con los shocks a simular en cada sector de ese país.
#Las claves del diccionario deben ser los sectores sobre los que se va a generar el shock, y los valores el porcentaje de shock. 
#Devuelve un vector con la variacion de la demanda en los sectores tras el shock.  
def variacion_demanda(demanda, porcentaje_sector):
    demanda = np.array(demanda,dtype=float)
    shock = np.zeros(demanda.shape[0])
    for sector,porcentaje in porcentaje_sector.items():
        shock[sector-1] = porcentaje/100 
    nueva_demanda = demanda + np.abs(demanda) * shock
    
    return nueva_demanda - demanda


# Toma una matriz A de coeficientes técnicos de un pais y un vector con la variación de la demanda externa sobre los sectores de ese pais.
# Devuelve un vector con la variación de la producción por sector sobre el pais donde se produce el shock.  Para calcular la variación
# se usa el modelo simple o intrarregional
def variacion_produccion_modelo_simple(A, variacion_de_la__demanda):
    I = np.eye(40)
    L,U, P = calcularLU(I-A)
    inv = inversaLU(L, U, P)
    return inv@ variacion_de_la__demanda

# Toma las matrices de coeficientes técnicos de dos paises y un vector con la variación de la 
# demanda externa sobre el país p1. 
# Devuelve un vector con la variación de la producción sobre el pais donde se produce el shock (p1). Para calcular la variación
# se usa el modelo complejo o interregional
def variacion_produccion_modelo_complejo(Ap1p1, Ap1p2, Ap2p2, Ap2p1, variacion_de_la_demanda):
    I = np.eye(40)
    L, U, P = calcularLU(I-Ap2p2)
    inv = inversaLU(L, U, P)
    x = I- Ap1p1 - ((Ap1p2@inv)@Ap2p1)
    L,U, P = calcularLU(x)
    inv = inversaLU(L, U, P)
    return inv @ variacion_de_la_demanda
    
# Genera el gráfico comparativo de la variación de la producción tras simular el shock, del modelo simple y el complejo
def generar_grafico(p1, p2, data):
    df = generar_Matriz_InsumoProducto(p1, p2, data)
    dp1, dp2 = obtener_demanda(p1, p2, df)
    porcentaje_shock_sector = {5:-10,6:3.3,7:3.3, 8:3.3}
    variacion_de_la_demanda = variacion_demanda(dp1, porcentaje_shock_sector)
    A_p1p1, A_p1p2, A_p2p2, A_p2p1, producto_p1, producto_p2 = generar_submatrices(p1, p2, df)
    variacion_compleja = variacion_produccion_modelo_complejo(A_p1p1, A_p1p2, A_p2p2, A_p2p1, variacion_de_la_demanda )
    variacion_simple = variacion_produccion_modelo_simple(A_p1p1,variacion_demanda(dp1, porcentaje_shock_sector))
    
    sectores = np.arange(1,41)
    indice = np.arange(40)
    
    plt.figure(figsize=(12, 6))
    
    plt.scatter(indice, variacion_simple, label='Modelo simple',color='blue', marker='o')
    plt.scatter(indice, variacion_compleja, label='Modelo interregional',color='red', marker='x')
    
    plt.xticks(indice, sectores)
    plt.xlabel('Sector')
    plt.ylabel('Variación de la producción (en millones de US$)')
    plt.title('Variación de la producción tras el shock')
    plt.tight_layout()
    plt.legend()
    plt.show()
    