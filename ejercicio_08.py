"""
Definir una clase Dado con un atributo "resultado" que corresponde al
resultado obtenido después de lanzar el dado

La clase Dado debe contener el constructor y los siguientes métodos:
- __init__(self, resultado=0). un constructor que permite inicializar el atributo
  predeterminado igual a 0.
- lanzar_dado(self): un método que permite lanzar el dado y obtener un 
  resultado aleatorio entre 1 y 6.
- mostra_puntos(self): un método que permite mostrar loa puntos obtenidos
  tras el lanzamiento del dado. (Ver visualización en consola)
  
  ej. de pruebas / casos de uso:
  >> lanzamiento_1= Dado()
  >> lanzamiento_1.lanzar_dado()
  >> lanzamiento_1.mostrar_puntos()   

"""

import random

class Dado:
    def __init__(self, resultado=0):
        self.resultado = resultado
        
    def lanzar_dado(self):
        self.resultado =  random.randint(1, 6)
        
    def mostrar_puntos(self):
        print(f'El resultado del lanzamiento del dado es: {self.resultado}')
     
lanzamiento = Dado()
lanzamiento.lanzar_dado()
lanzamiento.mostrar_puntos()

        