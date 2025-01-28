"""
conda install numpy
Realizar operaciones con Matrices
"""
import numpy as np
print(np.absolute(-9))

#Listas
lista = [55,68,97,52,45]
print(type(lista))
#Arrays
np_array = np.array(lista)
print(type(np_array))
#Trabajat datos como flotantes
np_array_float = np.array(lista,dtype="float32")
print(type(np_array_float))
""""
Operaciones con listas
suma, resta, producto, min, max, ordenamiento
Operaciones con arrays
Operaciones con vectores, matrices 2D y 3D, n_dimensionales

"""
print(sum(lista))
print(np.sum(np_array))
vector = [[1,2,3],[4,5,6],[7,8,9]]
array_2D = np.array(vector)
print(array_2D)
suma_2D = np.sum(array_2D)
prod_2D = np.prod(array_2D)
min_2D = np.min(array_2D)
max_2D = np.max(array_2D)

vector2D_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector2D_2 = np.array([[4,9,8],[1,5,9],[5,4,6]])
"""
     [1][2][3]        [4][9][8]               [5][11][11]
M1 = [4][5][6]   M2 = [1][5][9]  M3 = M1+M2 = [5][10][15]
     [7][8][9]        [5][4][6]               [12][12][15]
"""
vector2D_3 = vector2D_1+vector2D_2
print(vector2D_3)

#¿Operaciones de multiplicacion en las matrices?
#Producto punto y producto cruz
#producto punto
vector2D_4 = np.dot(vector2D_1,vector2D_2)
print(vector2D_4)
vector2D_5 = vector2D_1 @ vector2D_2
print(vector2D_5)
#producto cruz
vector2D_6 = np.cross(vector2D_1,vector2D_2)
print(vector2D_6)
#Numpy operaciones extras
print(np.ones(10,dtype=int))
print(np.zeros(10))
print(np.arange(0,11,0.1))
print(np.random.normal(0,1,10))
#vectores transpuestos
"""
x= [4,5,6,7]-->T x = [4]
                     [5]
                     [6]
                     [7]
"""
x = np.array([4,5,6])
#Transpuesto
print(np.transpose(x))

#Ocupamos seaborn para mostrar la grafica
import seaborn as sab
vector_list = np.random.normal(0,1,1000)
ax = sab.displot(vector_list)
