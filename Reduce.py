"""
Reduce un iterable a un solo valor.
Secuencia a un solo valor.
lambda,functools
Util para sumar y multiplicar elemntos de una lista 
"""
from functools import reduce
lista = list(range(1,10))
print(lista)
elevar = lambda a,b:a*b
print(reduce(elevar,lista))
