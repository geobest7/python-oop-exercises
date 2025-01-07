"""
Definir una clase Nota que tiene dos atributos: nombre del estudiante y su nota.
La clase Nota debe contener el constructor y el siguiente método:
- __init__(self, nota, estudiante): un constructor que permite
inicializar los atributos del clase Nota.
- ha_pasado(self): un método que permite verificar si un estudiante ha aprobado el examen.
Si la nota del estudiante supera los 75 puntos, entonces el estudiante ha aprobado, de lo 
contrario ha reprobado. Este métodoo muestra en la consola si el estudiante ha aprobado o reprobado. ( Ver visualización en la consola)

"""

class Nota:
    
    def __init__(self, nota, nombreEstudiante):
        self.nota = nota
        self.nombreEstudiante = nombreEstudiante
    
    def ha_pasado(self):
        if self.nota >= 75:
            print(f'El Alumno/a {self.nombreEstudiante} ha aprobado el examen con {self.nota} puntos')
        else:
            print(f'El Alumno/a {self.nombreEstudiante} ha reprobado el examen con {self.nota} puntos')

nota1 = Nota(77, "Aitana")
nota2 = Nota(70, "Rodrigo")
nota1.ha_pasado()

# acceder atributo istancia

print(f'La nota obtenida por {nota2.nombreEstudiante} en la primera corrección es {nota2.nota}')

# modificación del atributo "nota" en la instancia nota2

nota2.nota = 75
nota2.ha_pasado()

