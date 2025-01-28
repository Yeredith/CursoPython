#lambda.py
"""
¿Que es una función lambda?: funciones que se utilizan
cuando se quiere realizar una operacion en un solo comando
def potencia (base,exponente):
    return base**exponente
palabra -> lambda : funcion ya predefinina y es palabra reservada

"""
#Funcion resumida usando lambda
potencia = lambda base,exponente:base**exponente 
#nombre_funcion = lambda definicion_variable:operacion
p = potencia(2,2)
print(p)