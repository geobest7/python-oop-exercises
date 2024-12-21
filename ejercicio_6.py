"""
Definir una clase Persona que tiene tres atributos: el nombre del persona,
su edad y su género.
La clase Persona debe contener el constructor y los siguientes métodos.
- __init__(self,nombre,edad,genero): un contructor que permite inicializar
                                     los atributos de la clase persona.
- presentarse(self): un método que retorna una cadena de caracteres con la
                     informacion de la persona.(Ver visualización en la consola).
- esAdulto(self): un método que verifica si una persona es adulta (es decir, si su
                  edad es igual o superior a las 18 años). El método retorna True si
                  la persona es adulta y False de lo contrario.
    
    """
    
class Persona:
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def presentarse(self):
        return ('Hola soy {}, mi genero es {} y tengo {}'.format(self.nombre, self.edad, self.genero))

    def esAdulto(self):
        if self.edad < 18:
            return False
        else:
            return True
            
persona = Persona('Alessandro', 12, 'Masculino')
print(persona.presentarse())
print(persona.esAdulto())