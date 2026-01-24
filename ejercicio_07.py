# este ejercicio requiere el uso de la clase Persona del ejercicio 6.

"""
Definir una clase Estudiante que herede de la clase Persona

Esta subclase Estudiante debe contener el constructor y los siguientes métodos:

 - __init__(self, nombre, edad, genero, nivel): un constructor que permite
   inicializar los atributos de la clase Estudiante.
 - inscripcion(self, estudiantes_escritos): este método toma como parámetros
   la lista de estudiantes inscritos y luego añade el nombre, la edad y el género del nuovo 
   estudiante inscrito en la lista.   
   
"""

class Persona:
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def presentarse(self):
        return ('Hola soy {},  tengo {} años y mi genero es{}'.format(self.nombre, self.edad, self.genero))

    def esAdulto(self):
        if self.edad < 18:
            return False
        else:
            return True
        
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, genero, nivel):
        super().__init__(nombre, edad, genero)
        self.nivel = nivel
        
    def inscripcion(self, estudiantes_inscritos):
        estudiantes_inscritos.append((self.nombre, self.edad, self.genero, self.nivel))

estudiantes_inscritos = [] 
       
estudiante1 = Estudiante('Alessandro', 32, 'varón', 'medioalto')
estudiante1.inscripcion(estudiantes_inscritos)

estudiante2 = Estudiante('Giulia', 16, 'chavala', 'medioalto')
estudiante2.inscripcion(estudiantes_inscritos)
print(estudiante2.presentarse())

print(estudiantes_inscritos)