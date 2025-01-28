#Map
"""
Devuelve un objeto iterable.
Transformar elementos de una lista.
Puede convertir elementos a lista.
"""
#Iteraciones reducidas
lista = [2,5,6,7]
print([numero**2 for numero in lista])
#recorre lista y para cada numero eleva al cuadrado
#Map
elevar = lambda numero:numero**2
print(list(map(elevar,lista)))
