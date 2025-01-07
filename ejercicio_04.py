"""
Definir una clase Circulo que tiene tres atributos: su radio,
la posicion de su centro O(x,y).
La clase Circulo debe contener el constructor y los siguientes métodos:

- __init__(self, x, y, R): un contructor que permite inicializar los atributos
del a clase Circulo-
- area(self): un método que permite calcular el área de un círculo.
- perímetro(self): un método que permite calcular el perímetro de un círculo.
-mostrar_propriedades(self): un método que permite mostrar las propriedades de 
un círculo, es decir, las coordenadas de su centro O, y su radio en cm. (visualización en la consola)

"""

class Circulo:
    
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R 
        
    def area(self):
        pi = 3.14159
        return (self.R**2) * pi
    
    def perimetro(self):
        pi = 3.14159
        return self.R * 2 * pi
    
    def mostrar_propriedades(self):
        return f"El circulo tiene radio de {self.R} cm, las cordenadas de su centro O son ({self.x}, {self.y})"
    
circulo1= Circulo(3, 4, 5)
print(circulo1.mostrar_propriedades())
print("El perímetro del círculo es ", round(circulo1.perimetro(), 2))
print("El área del circulo es: ", round(circulo1.area(), 2))

