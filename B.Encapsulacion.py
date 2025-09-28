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
#c.saldo = -15
#print (c.saldo)

# 12) Convierte temperatura_f en un atributo de solo lectura que se calcula desde temperatura_c.

class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)
    # Define aquí la propiedad temperatura_f: F = C * 9/5 + 32
    @property
    def temperatura_f(self):
        return (self._c*9/5+32)
    
t=Termometro(30)
print(f"la temperatura es: {t.temperatura_f} grados fahrenheit")

# 13) Haz que nombre sea siempre str. Si asignan algo que no sea str, lanza TypeError.

class Usuario:
  def __init__(self, nombre):
    self._nombre=""
    self.nombre = nombre
  # Implementa property para nombre
  @property
  def nombre(self):
      return self._nombre
  @nombre.setter
  def nombre(self, n):
      if(type(n)==str):
        self._nombre=n
      else:
        raise TypeError("Nombre debe contener de manera obligatoria un tipo de dato str")
  
user=Usuario("Jose")
print(user.nombre)
#user2=Usuario(15)
#print(user2.nombre)

#14) Expón una vista de solo lectura de una lista interna.

class Registro:
    def __init__(self):
        self.__items = []
    def add(self, x):
        self.__items.append(x)
    # Crea una propiedad 'items' que retorne una tupla inmutable con el contenido
    @property
    def items(self):
        return tuple(self.__items)
    
r=Registro()
r.add(1)
r.add(2)
r.add(3)
print(r.items)

