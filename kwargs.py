#Pasamos elementos ("string") a una funcion
def string_var (**variables): #Funcion **kwargs
    #print(variables)
    #print(type(variables))
    for key,value in variables.items():
        print(f"{key} corresponde a {value}")

string_var(nombre="Susana", estado_civil='Casada', edad=27)

