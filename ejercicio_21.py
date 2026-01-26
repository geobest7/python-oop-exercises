"""
Definir una clase llamada Calculadora que contiene un constructor y los siguientes métodos estáticos:

    - __init__(self,variable): un constructor que permite inicializar el atributo variable.
    - def suma(x,y). este método permite sumar los valores x y y pasados como parámetros.
    - def multiplicacion(x,y): este método permite multiplicar el valor de x por y.
    - def division(x,y): este método estático permite dividir x por y.

"""


class Calculadora:
    def __init__(self, variable):
        self.variable = variable

    @staticmethod
    def suma(x, y):
        return x + y
    
    @staticmethod
    def multiplicacion(x, y):
        return x * y
    
    @staticmethod
    def division(x, y):
        if y == 0:
            return "Error: división por cero"
        return x / y
        

c1 = Calculadora(10)

print(f'Suma de dos números: {Calculadora.suma(1, 1)}')
print(f'Multiplicación de dos números: {Calculadora.multiplicacion(1, 1)}')
print(f'División de dos números: {Calculadora.division(1, 1)}')
    