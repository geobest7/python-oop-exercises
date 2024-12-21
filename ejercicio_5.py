"""
Definir una clase Operacion que tiene dos atributos:
dos números enteros 'x' y 'y'. Esta clase nos permitirá
realizar operaciones aritméticas entre dos atributos

La clase Operacion debe contener el constructor y los siguientes métodos:
- __init__(self,x,y): un constructor que permite inicializar los atributos de la clase Operacion.
- suma(self): un método que permite realizar la suma entre los atributos x y y de la clase.
- multiplicacion(self): un método que permite realizar la multiplicación entre los atributos x y y de la clase.
-division(self): un método que permite realizar la división de x por y.
                 Si el valor de y es igual a 0, este método debe retornar la frase:
                 ¡División de x por y es imposible!

"""
class Operacion:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def suma(self):
        return self.x + self.y
    
    def multiplicacion(self):
        return self.x * self.y
    
    def division(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return '¡ERROR! NO SE PUEDE DIVIDIR POR 0'
        
oper = Operacion(3,0)
print('El resultado del la suma es:', oper.suma())
print('El resultado del la multiplicación es:',oper.multiplicacion())
print('El resultado del la división es:',oper.division())