""" 
En este ejercicio vamos a definir una clase Usuario que nos permitirá gestionar eficientemente
a nuestro usuarios.
Esta clase Usuario tiene una variable de clase, que es el número de usuarios activos, y tres
variables de instancia que son el nombre, el apellido y la edad del usuario.

Además de las variables de clase y de instancia, debemos mplementar un constructor y varios métodos:

    - __init__(self,...): este método permite inicializar las varibles de instancia con valores pasados
      como parámetros.
    - def extraer_info(cls, cadena): este método de clase toma como parámetros una clase "cls" y una cadena
      en el formato "nombre,apellido,edad", y crea una instancia a partir de esta cadena.
    - mostrar_usuarios_activos(cls): este método de clase toma como parámetros una clase "cls" y devuelve
      una cadena que indica el número de usuarios activos.( Ver salida en consola)
    - desconectar(self): este método permite desconectar a un usuario activo, decrementando la variable que
      cuenta el número de usuarios activos. Además, este método devuelve una cadena con el nombre y apellido
      del usuario que se desconectó.

"""

class Usuario:

    USUARIOS_ACTIVOS = 0

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

        Usuario.USUARIOS_ACTIVOS += 1

    @classmethod
    def extraer_info(cls, cadena):
        nombre, apellido, edad = cadena.split(",")
        return cls(nombre, apellido, edad)
    
    @classmethod
    def mostrar_usuarios_activos(cls):
        return f'Actualmente,  hay {cls.USUARIOS_ACTIVOS} usuario(s) activos.'
    
    def desconectar(self):
        Usuario.USUARIOS_ACTIVOS -= 1
        return f'Se ha desconectado el usuario {self.nombre} {self.apellido}'
    

usuario_1 = Usuario("Martin", "Lebouf", 35)
usuario_2 = Usuario.extraer_info("Ginetto,Ginetti,28")
print(Usuario.mostrar_usuarios_activos())
print(usuario_2.desconectar())
print(Usuario.mostrar_usuarios_activos())


    