"""
Clases y objetos?: Clase -> libreta
-> hoja ->plantilla
Plantilla donde se pueden instanciar objetos
Objeto -> Puede ser cualquier cosa ya sea animado o inanimado
Todo aquel que tenga caracteristicas puede ser un objeto
-Las caracteristicas se conocen como atributos y pueden ser
compartidos a traves de métodos 
Cuando se quiere heredar caracteristicas del objeto se ocupa
la herencia
Polimorfismo -> poli -> muchos
morfos -> forma 
-Un mismo objeto se puede comportar de una forma en una clase
pero de diferente forma en otra clase, métodos. 
"""

class Persona:
    #Inicializan los métodos
    #self referencia al propio objeto
    #__init__ inicializar el método: constructores
    def __init__(self, nombre, edad):
        self.nombre = nombre #Creamos objetos
        self.edad = edad
    #Crear método
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad}")

#instanciar a la clase Persona -> crear objetos
persona1 = Persona("Rafael",22)
persona2 = Persona("Evelyn",20)
#Llamar al método
persona1.saludar()
persona2.saludar()
