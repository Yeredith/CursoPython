"""
Filter:Crea una lista con elementos de lista original
Devuelve coleccion de elemntos ya filtrados
"""
lista = list(range(1,200))
print([numero for numero in lista if numero%20==0])
filtro = lambda numero:numero%20==0
print(list(filter(filtro,lista)))