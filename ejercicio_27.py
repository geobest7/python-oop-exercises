"""
En este ejercicio, crearemos una clase GeneradorContrasena que nos ayudará a generar contraseñas 
eligiendo los parámetros que nuestra contraseña debe stisfacer.

La clase GeneradorContrasena contiene cinco atributos:
    - un atributo que indica la longitud de la contraseña
    - un atributo que indica si la contraseña puede incluir caracteres especiales
    - un atributo que indica si la contraseña puede incluir números
    - un atributo que indica si la contraseña puede incluir letras mayúsculas
    - un atributo que indica si la contraseña puede incluir letras minúsculas

Nuestra clase también contiene varios métodos esenciales para la generación de la
contraseña, como:
    - def __init__(self,...): un contructor para inicializar los atributos de la clase.
    - def incluir_mayusculas(self, mayuscula): este método permite modificar el estado
      de la variable de instancia que indica si una contraseña puede incluir letras mayúsculas.
    - def incluir_minusculas(self, minuscula): este método permite modificar el estado
      de la variable de instancia que indica si una contraseña puede incluir letras minusculas.
    - def incluir_numeros(self, numeros): este método permite modificar el estado
      de la variable de instancia que indica si una contraseña puede incluir números.
    - def incluir_caracteres_especiales(self, caracteres_especiales): este método permite modificar el estado
      de la variable de instancia que indica si una contraseña puede incluir caracteres especiales.
    - def modifcar_longitud(self, longitud): este método permite modificar la langitud de la contraseña.
    - def generar_contraseña(self): este método permite generar una contraseña teniendo en cuenta el estado
      de las variables de instancia. Devuelve la contraseña generada en forma de cadena de caracteres.
    - def evaluar_contraseña(self, contrasena): este método permite evaluar robustez (sobre 5 puntos) de la
      contraseña basándose en los siguientes criterios:
        - si la contraseña tiene más de 10 caracteres, la robustez aumenta de 1 punto.
        - si la contraseña tiene al menos una letra mayúscula, la robustez aumenta de 1 punto.
        - si la contraseña tiene al menos de una letra minúscula, la robustz aumenta de 1 punto.
        - si la contraseña tiene al menos un número, la robustez aumenta de 1 punto.
        - si la contraseña tien al menos un caracter especial, la robustez aumenta de 1 punto.
      Se distinguen varios niveles de robustez según los puntos acumulados:
        - Si la robustez es igual a 5 puntos, el método devuelve: "Seguridad contraseña muy fuerte"
        - Si la robustez es igual a 4 puntos, el método devuelve: "Seguridad contraseña fuerte"
        - Si la robustez es igual a 3 puntos, el método devuelve: "Seguridad contraseña media"
        - Si la robustez es igual o menor a 2 puntos, el método devuelve: "Seguridad contraseña débil"
    - def guardar_contrasena(self, contrasena, ruta_archivo): este método permite guardar una contraseña en un
      archivo cuya ruta completa se indica en los parámetros.
    - def leer_contrasena(self, ruta_archivo): este método permite leer la contraseña contenida en el archivo 
      donde está almacenada.

"""

import random
import string

class GeneradorContrasena:
    def __init__(self, long, caract_esp=True, numeros=True, mayuscula=True, minuscula=True):
        self.long = long
        self.caract_esp = caract_esp
        self.numeros = numeros
        self.mayuscula = mayuscula
        self.minuscula = minuscula

    def incluir_mayuscula(self, mayuscula):
        self.mayuscula = mayuscula

    def incluir_minuscula(self, minuscula):
        self.minuscula = minuscula
    
    def incluir_numeros(self, numero):
        self.numeros = numero

    def incluir_caracteres_especiales(self, caract_esp):
        self.caract_esp = caract_esp

    def modifcar_longitud(self, long):
        self.long = long
    
    def generar_contrasena(self):
        contrasena = ""

        if self.caract_esp:
            caract_esp_str = "!@#$%&*()"
        else:
            caract_esp_str = ""
        
        if self.numeros:
            numeros_str = string.digits
        else:
            numeros_str = ""
        
        if self.mayuscula and not self.minuscula:
            letras_str = string.ascii_uppercase
        
        elif self.minuscula and not self.mayuscula:
            letras_str = string.ascii_lowercase
        
        elif self.mayuscula and self.minuscula:
            letras_str = string.ascii_letters

        else:
            letras_str = ""

        caracteres_concat = caract_esp_str + numeros_str + letras_str

        if not caracteres_concat:
            raise ValueError("No hay caracteres disponibles para generar la contraseña")
        
        for j in range(self.long):
            contrasena += random.choice(caracteres_concat)
        
        return contrasena
    
    def evaluar_contraseña(self,contrasena):

        robustez = 0

        if len(contrasena) >= 10:
            robustez += 1
        if any(char.isupper() for char in contrasena):
            robustez += 1
        if any(char.islower() for char in contrasena):
            robustez += 1
        if any(char.isdigit() for char in contrasena):
            robustez += 1
        if any(char in "!@#$%&*()" for char in contrasena):
            robustez += 1

        if robustez == 5:
            return "Seguridad contraseña muy fuerte"
        if robustez == 4:
            return "Seguridad contraseña fuerte"
        if robustez == 3:
            return "Seguridad contraseña media"
        if robustez <= 2:
            return "Seguridad contraseña débil"
        
    def guardar_contrasena(self, contrasena, ruta_archivo):
        with open(ruta_archivo, "w") as archivo:
            archivo.write(contrasena)
    
    def leer_contrasena(self, ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            contrasena = archivo.read()
        return contrasena
    
gen_1 = GeneradorContrasena(15)

contra_1 = gen_1.generar_contrasena()
print(contra_1)
print(f'Robustez de la contraseña 1: {gen_1.evaluar_contraseña(contra_1)}')
print("-" * 30)

gen_1.incluir_caracteres_especiales(False)
contra_2 = gen_1.generar_contrasena()
print(contra_2)
print(f'Robustez de la contraseña 2: {gen_1.evaluar_contraseña(contra_2)}')
print("-" * 30)


gen_1.incluir_caracteres_especiales(True)
gen_1.incluir_mayuscula(False)
gen_1.incluir_minuscula(False)
gen_1.incluir_numeros(False)
contra_3 = gen_1.generar_contrasena()
print(contra_3)
print(f'Robustez de la contraseña 3: {gen_1.evaluar_contraseña(contra_3)}')
print("-" * 30)

print("guardando la contraseña en curso...")
gen_1.guardar_contrasena(contra_1, "contrasena.txt")
print("Guardado de contraseña -- OK")
print("Leyendo la contraseña guardada:")
print(gen_1.leer_contrasena("contrasena.txt"))



