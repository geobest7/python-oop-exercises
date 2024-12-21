"""   Definir una clase Libro que tiene tres atributos: título del libro, nombre
   del autor y precio del libro..
   La clase Libro debe contener el constructor y el siguiente método:
       -__init__(self,titulo,autor,precio): un constructor que permite
       inicializar los atributos de la clase Libro.
       - mostrar_informaciones(self): un método que, como su nombre indica,
       permite mostrar la información relacionada con el libro.
       (Ver la visualización en consola)
"""
class Libro:
    
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor 
        self.precio = precio
        
        
    
    def mostrar_informaciones(self):
        print(f"El titulo es {self.titulo}, el autor es {self.autor} y el precio es {self.precio} euros")

libro = Libro("Divina Commedia", "Dante Alighieri", 55)
libro.mostrar_informaciones()