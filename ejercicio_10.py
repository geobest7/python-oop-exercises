"""
Definir una clase Empleado con 4 atributos: el nombre del empleado,
su función, su salario y el número de horas trabajadas.

La clase empleado debe contener el constructor y los siguientes métodos:

- __init__(self, nombre, funcion,, salario): Este constructor permite
inicializar los atributos de la clase Empleado. El cuarto atributo, que
corresponde al número de horas trabajadas, se inicializa a 0 en el
constructor sin pasar su valor inicial como parámetro.

- def trabajar(self, numero_horas): este método permite sumar el número
de horas pasado como parámetro al número de horas trabajadas.
Además, este método devuelve una cadena que muestra el número total de 
horas trabajadas por el empleado.
(Ver visualización en pantalla)

- def info_sueldo(self): este método devuelve una cadena que muestra el
salario del empleado.(Ver visualización en pantalla)

- def dar_aumento(self, cantidad): este método permite dar un aumento al empleado,
incrementando su salario actual con la suma pasado como parámetro.

- def info_funcion(self): este método devuelve una cadena que muestra la función
actual del empleado.

"""

class Empleado:
    def __init__(self, nombre, funcion, salario, n_horas_tXd=0):
        self.nombre = nombre
        self.funcion = funcion
        self.salario = salario
        self.n_horas_tXd = n_horas_tXd
        
    def trabajar(self, numero_horas):
        self.n_horas_tXd += numero_horas
        return f'El numero de horas trabajados por dia por el empleada/o {self.nombre} es de {self.n_horas_tXd}.'
    
    def info_sueldo(self):
        return f'El salario del empleada/o {self.nombre} es de {self.salario} € brutos por año.'
    
    def dar_aumento(self, cantidad):
        self.salario += cantidad
        return f'El empleada/o {self.nombre} ha recibido un aumento de salario de {cantidad} €, ahora recibe un salario de {self.salario} brutos por año.'
            
            
    def info_funcion(self):
        return f'La función del empleada/o {self.nombre} es de {self.funcion}.'
    
    
empleado_1 = Empleado('Gino', 'jardinero', 1400)
print(empleado_1.trabajar(6))
print(empleado_1.info_sueldo())
print(empleado_1.dar_aumento(25))
print(empleado_1.info_funcion())

