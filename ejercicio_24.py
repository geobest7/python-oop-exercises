"""" 
Definir una clase llamada CuentaBancaria que nos permitirá gestionar nuestra cuenta bancaria.
Esta clase posee dos variables de clase que son el tipo de cuenta (ahorros,cuenta corriente, etc.)
y la tasa de intéres aplicada. Además, la clase contiene cuatro atributos: el nombre y apellido del
titular de la cuenta, el número de cuenta y el saldo de la cuenta.

Los métodos a implementar para esta clase son:

    - __init__(self,...): un constructur para inicializar los atributos de la clase.
    - def establecer_tasa_interes(clas, nueva_tasa): este método de clase permite
      cambiar la tasa de intéres aplicabile. Este método debe simplemente modificar la variable de 
      clase correspondiente.
    - def cambiar_tipo_cuenta(cls, tipo_cantidad): este método de clase permite cambiar el tipo de
      cuenta simplemente modificando la variable de clase correspondiente.
    - def deposito(self, cantidad): este método permite depositar una cantidad en nuestra cuenta bancaria.
    - def retiro(self,cantidad): este método permite realizar un retiro si la cnatidad solicitada está 
      disponible en nuestra cuenta bancaria.
    - aplicar_tasa_interes(self): este método permite aplicar la tasa de interés establecida por el banco, 
      restándole al saldo actual el monto correspondiente a dicha tasa.
    - __str__(self): este método especial nos permite personalizar la visualización del objeto de esta clase.
      ( Ver la visualización en la consola para crear este método).

"""

class CuentaBancaria:

    TIPO_CUENTA = ""
    TASA_INTERES = 0

    def __init__(self, nombre, apellido, n_cuenta, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.saldo = saldo

    @classmethod
    def establecer_tasa_interes(cls, nueva_tasa):
        cls.TASA_INTERES = nueva_tasa
        return f'Tasa de interes aplicada de {CuentaBancaria.TASA_INTERES} %'
    
    @classmethod
    def cambiar_tipo_cuenta(cls, tipo_cuenta):
        cls.TIPO_CUENTA = tipo_cuenta
        return f'Esta cuenta es de tipo: {tipo_cuenta}'
    
    def deposito(self, cantidad):
        self.saldo += cantidad
        return f'Has depositado {cantidad} € en tu cuenta y el saldo es de {self.saldo}.'
    
    def retiro(self, cantidad):
        if cantidad < self.saldo:
            self.saldo -= cantidad
            return f'Has retirado {cantidad} € de tu cuenta y el saldo es de {self.saldo} €.'
        else:
            return "Su saldo es insufficiente"
            
    def aplicar_tasa_interes(self):
        interes = round(self.saldo * (CuentaBancaria.TASA_INTERES / 100), 2)
        self.saldo -= interes
        return f'Hemos aplicado una tasa de interés de {interes} €. Nuevo saldo: {self.saldo} €.'
    
    def __str__(self):
        return f'Numero de cuenta: {self.n_cuenta}\nTipo de cuenta: {CuentaBancaria.TIPO_CUENTA}\n' + \
               f'Titular de la cuenta: {self.nombre} {self.apellido}\n' + \
               f'saldo de cuenta: {self.saldo} €'
    

CuentaBancaria.cambiar_tipo_cuenta("Corriente")
CuentaBancaria.establecer_tasa_interes(0.05)
cuenta_1 = CuentaBancaria("Laurent", "Dubois", "983750XZ", 3000)
print(cuenta_1)
print("-" * 20)
print(cuenta_1.retiro(4000))
print(cuenta_1)
print("-" * 20)
print(cuenta_1.retiro(1500))
print(cuenta_1.deposito(500))
print("-" * 20)
print(cuenta_1.aplicar_tasa_interes())


