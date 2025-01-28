"""
Pandas: Sirve para manipulacion de datos estructurados

"""
import pandas as pd
#leer archivos csv 
df = pd.read_csv("hola.csv")
print(df) #Mostrar toda la tabla
print(df.head()) #Los primeros y los ultimos
print(df.info()) #Informacion de la tabla
print(df.shape)
print(df.shape[0])
print(df.shape[1])
print(list(df.columns))
titulos = list(df.columns)
print(titulos[0])
#loc, iloc, isnull
