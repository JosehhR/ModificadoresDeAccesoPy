#Autor: Jose Luis Ramirez
# Este codigo ilustra el desarrollo de los puntos 11 a 14 del taller que involucra encapsulacion, 

#11) Completar propiedad con validación Completa para que saldo nunca sea negativo.

class Cuenta:
    def __init__(self, saldo):
        self._saldo = 0
        self.saldo = saldo
    @property
    def saldo(self):
        #devolver el valor de saldo
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
    # Validar no-negativo
        if value < 0:
            raise ValueError("El saldo no puede ser negativo")
        else:
            self._saldo=value

c=Cuenta(0)
c.saldo = 15
print (c.saldo)
        