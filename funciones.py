#Random: obtener elementos aleatorios
from random import randint, randrange, seed
#lista = randint(1,10)
lista = randrange(1,10,3)
print(lista)
for i in range(3,9):
    print(i)
for i in range(1,10):
    print(i*3)
[numero*3 for numero in range(1,10)]

x = randint(9,15)
y = randrange(10,20,2)
z = seed()
