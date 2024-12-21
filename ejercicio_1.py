"""
    Definir una clase Galleta que tiene dos atributos: nombre de la galleta y su forma.
    La clase Galleta debe contener el constructor y el siguente metodo:
    -__init__(self,nombre,forma):un constructor que permite inicializar los atributos
    de la clase Galleta.
    -hornar(self): un metodo que simplemente permite mostrar dos frases en la consola.

"""

class Galleta:

    def __init__(self,nombre,forma):
        self.nombre = nombre
        self.forma = forma
    
    def hornear(self):
        print(f'Esta {self.nombre} ha sido horneada en forma de {self.forma}')

galleta1 = Galleta('galleta de chocolate','corazon')
galleta1.hornear()


