import numpy as np
from scipy.linalg import solve_triangular
import pandas as pd

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
    if P is not None: 
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

#Toma 2 strings p1 y p2 códigos de países y la ruta a un archivo .xlsx con las matrices de insumo producto
#de latinoamérica generadas por la CEPAL.
#Devuelve la matriz de insumo producto de p1 y p2. 
def generar_Matriz_InsumoProducto(p1, p2, data):
    df = pd.read_excel(data, sheet_name='LAC_IOT_2011')
    df = df.loc[(df['Country_iso3'] == p1) | (df['Country_iso3']==p2)]
    df = df[[col for col in df.columns if (col.startswith(p1) or col.startswith(p2) or col == 'Country_iso3' or col == 'Output')]]
    return df

#Toma 2 strings p1 y p2 códigos de país y un dataframe con la matriz insumo producto de p1 y p2
#Devuelve las submatrices intra-regionales e inter-regionales de los coeficientes técnicos de p1 y p2
def generar_submatrices(p1, p2, data):
    #Genero la matriz de insumo producto intraregional del país p1
    p1_df = data.loc[df['Country_iso3'] == p1] 
    z_p1p1 = p1_df[[col for col in p1_df.columns if col.startswith(p1)]] 
    producto_p1 = p1_df['Output']
    producto_p1 = producto_p1.replace(0,1)
    A_p1p1 = z_p1p1.div(producto_p1, axis=0)
    
    #Genero la matriz de insumo producto intraregional del país p2
    p2_df = data.loc[df['Country_iso3'] == p2] 
    z_p2p2 = p2_df[[col for col in p2_df.columns if col.startswith(p2)]] 
    producto_p2 = p2_df['Output']
    producto_p2 = producto_p2.replace(0,1)
    A_p2p2 = z_p2p2.div(producto_p2, axis=0)

    #Genero la matriz de insumo producto interregional del país p2 con p1
    z_p2p1 = p2_df[[col for col in p2_df.columns if col.startswith(p1)]] 
    A_p2p1 = z_p2p1.div(producto_p2, axis=0)
    
    #Genero la matriz de insumo producto interregional del país p1 con p2
    z_p1p2 = p1_df[[col for col in p1_df.columns if col.startswith(p2)]] 
    A_p1p2 = z_p1p2.div(producto_p1, axis=0)
        
    return A_p1p1.values, A_p1p2.values, A_p2p2.values, A_p2p1.values, producto_p1.values, producto_p2.values
    
#Toma 2 strings p1 y p2 códigos de país y un dataframe con la matriz insumo producto de p1 y p2
#Devuelve los vectores demanda externa de los países p1 y p2 
def obtener_demanda(p1,p2,data):
    A_p1p1, A_p1p2, A_p2p2, A_p2p1, producto_p1, producto_p2 = generar_submatrices(p1, p2, data)
    I = np.eye(40)
    dp1 = (I-A_p1p1)@producto_p1 - A_p1p2@producto_p2
    dp2 = (-A_p2p1)@producto_p1 + (I-A_p2p2)@producto_p2
    
    return dp1, dp2

#Toma un vector con los datos de la demanda externa de un país y un vector con los shocks a simular en cada sector de esa región
#Devuelve un vector demanda modificado con los shocks proporcionados.
def simular_shock(demanda, porcentaje_sector):
    shock = np.zeros(40)
    for i,j in porcentaje_sector:
        shock[i-1] = j 
    demanda += abs(demanda)*shock
    return demanda

def variacion_produccion_modelo_simple(A, demanda):
    I = np.eye(40)
    L,U, P = calcularLU(I-A)
    inv = inversaLU(L, U, P)
    return inv@demanda


def variacion_produccion_modelo_complejo(Ap1p1, Ap1p2, Ap2p2, Ap2p1, demanda):
    I = np.eye(40)
    L, U, P = calcularLU(I-Ap2p2)
    inv = inversaLU(L, U, P)
    x = I- Ap1p1 - ((Ap1p2@inv)@Ap2p1)
    L,U, P = calcularLU(x)
    inv = inversaLU(L, U, P)
    return inv @ demanda
    
data = '../data/matrizlatina2011_compressed_0.xlsx'
p1 ='SLV'
p2= 'NIC'
df = generar_Matriz_InsumoProducto(p1, p2, data)
dp1, dp2 = obtener_demanda(p1, p2, df)
print(dp1)
porcentaje_sector = [(5,-0.1), (6, 0.033), (7,0.033), (8,0.033)]
print(simular_shock(dp1, porcentaje_sector))

A_p1p1, A_p1p2, A_p2p2, A_p2p1, producto_p1, producto_p2 = generar_submatrices(p1, p2, df)

variacion_produccion_modelo_complejo(A_p1p1, A_p1p2, A_p2p2, A_p2p1, dp1)