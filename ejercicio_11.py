"""
Define una clase Calculo_Numerico que nos permita llevar a cabo varias operaciones numéricas.
Este clase tiene un solo atributo: un número entero.

La clase Calculo_Numerico debe contener un constructor y varios métodos de operaciones numéricas, a saber:

 - __init__(self, numero): un constructor que permite inicializar el atributo de la clase.
 - calculo_factorial(self): un método que permite calcular el factorial del atributo número. Este método
   devuelve el resultado obtenido.
 - lista_divisores(self): un método que permite encontrar la lista de divisores del atributo número.
   Este método devuelve una lista de Python con todos los divisores de ese número.
 - esPrimo(self): n método que permite verificar si un número es primo.
   Este método muestra si el número es primo o no.
   (Ver la salida en la consola)
 - esPar(self): un método que permite verificar si un número es par.
   Este método muestra si le número es par o impar.
   (Ver la salida en la consola)
   
   ### ejemplos de pruebas / casos de uso:
   
       primer_calculo = Calculo_Numerico(5)
       factorial_5 = primer_calculo.calculo_factorial()
       divisores_5 = primer_calculo.lista_divisores()
       print("...") ## completar
       print("...") ## completar
       primer_calculo.esPar()
       primer_calculo.esPrimo()
    
    """
    
class Calculo_Numerico:
    def __init__(self, numero):
        self.numero = numero
        
    
    def calculo_factorial(self):
        if self.numero < 0:
            return "El factorial no està definido para números negativos"
        elif self.numero == 0:
            return 1
        
        result = 1
        for i in range(1, self.numero + 1):
            result *= i
            
        return result 


    def lista_divisores(self):
        divisores = []
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                divisores.append(i)
        return divisores
        
        
    def esPrimo(self):
        if self.numero <= 1:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return "El número no es Primo"
        return "El número es Primo"
    
    def esPar(self):
        if self.numero % 2 == 0:
            print("El número es Par")
        else:
            print("El número es Impar")
        
        
           
primer_calculo = Calculo_Numerico(5) 
divisor = primer_calculo.lista_divisores()
factorial= primer_calculo.calculo_factorial()
print(f"Los divisores de {primer_calculo.numero} son: ", divisor)
print(f"El número factorial de {primer_calculo.numero} es: ", factorial)
print(primer_calculo.esPrimo())
primer_calculo.esPar()     
        
    
    