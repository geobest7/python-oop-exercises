""" 
Definir una clase Vector4D que represente un vector de 4 dimensiones con 4 números como atributos: u, v, x, y.

La clase Vector4D debe contener el constructor y los siguientes métodos:
    - __init__(self,...): un constructor que permite inicializar todas las coordinadas del vector.
    - __add__(self,vector): este método especial nos permite sumar dos vectores de cuatro dimensiones.
    - __sub__(self, vector): este método especial nos permite restar dos vectores de cuatro dimensiones.
    - __mul__(self, vector): este método especial nos permite multiplicar dos vectores.
    - __treudiv(self, escalar): este método especial permite dividir un vector por un escalar (un número)

"""

class Vector4D:
    def __init__(self, u, v, x, y):
        self.u = u
        self.v = v
        self.x = x 
        self.y = y
        
    def __add__(self, vector):
        return  Vector4D(
            self.u + vector.u,
            self.v + vector.v,
            self.x + vector.x,
            self.y + vector.y
            )
    
    def __sub__(self, vector):
        return Vector4D(
            self.u - vector.u,
            self.v - vector.v,
            self.x - vector.x,
            self.y - vector.y
        )
    
    def __mul__(self, vector):
        return Vector4D(
            self.u * vector.u,
            self.v * vector.v,
            self.x * vector.x,
            self.y * vector.y
        )    
    
    def __truediv__(self, escalar):
        return Vector4D(
            self.u / escalar,
            self.v / escalar,
            self.x / escalar,
            self.y / escalar           
        )
    
    def __str__(self):
        return f"{self.u}, {self.v}, {self.x}, {self.y}"

# inicilaizamos dos vectores

v1 = Vector4D(1, 2, 3, 4)
v2 = Vector4D(1, 2, 3, 4)        


# suma de dos vectores

suma = v1 + v2
print(f'El resultado de la suma de estos dos vectores es: {suma}')
print('-'*30)

# resta de dos vectores

resta = v1 - v2
print(f'El resultado de la resta de estos dos vectores es: {resta}')
print('-'*30)

# multiplicación de dos vectores

multi = v1 * v2
print(f'El resultado de la multiplicación de estos dos vectores es: {multi}')
print('-'*30)

# division de un vector por un escalar

divpesc= v1 / 2
divpesc2 = v2 / 3     
print(f'El resultado de la division del vector 1 por 2 es: {divpesc}')
print(f'El resultado de la division del vector 2 por 3 es: {divpesc2}')