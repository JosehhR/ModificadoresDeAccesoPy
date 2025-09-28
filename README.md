# 📄Modificadores de Acceso Python

## 📌 Descripción

Este repositorio muestra la solución al taller pre-parcial planteado sobre modificadores de acceso en python 

---

## 🅰️ Conceptos y lectura de codigo

### 1). Selección múltiple

Dada la clase 

```python
class A:
x = 1
_y = 2
__z = 3

a = A()
```
¿Cuáles de los siguientes nombres existen como atributos accesibles directamente desde
a?  
•  A) `a.x`  
•  B) `a._y`  
•  C) `a.__z`  
•  D) `a._A__z`
  <br><br>
#### ✅ Respuesta:  
La respuesta correcta a la pregunta son las opciones **A, B, y D**, pues todas ellas son accesibles de esa forma en otras partes, sin embargo, por buenas prácticas la unica opcion a la que se deberia acceder directamente es **A**

---

### 2). Salida del Programa

```python
class A:
def __init__(self):
self.__secret = 42
a = A()
print(hasattr(a, '__secret'), hasattr(a, '_A__secret'))
````
¿Que imprime?
<br><br>
#### ✅ Respuesta:  
Como el codigo esta involucrando dos condiciones, la primera imprimirá **False** por que **__secret** no es realmente un atributo del objeto, pues este al interpretarse el codigo se transforma en **_A__Secret**, lo que realiza por ende q la segunda condicion si se cumpla, y imprima **True**, por lo que la salida en consola debe ser 

````
False True
````

---

### 3) Verdadero/Falso (explica por qué)

• a) El prefijo _ impide el acceso desde fuera de la clase.  
• b) El prefijo __ hace imposible acceder al atributo.  
• c) El name mangling depende del nombre de la clase.  
  <br><br>
#### ✅ Respuesta:  
• a) **Falso**, Por que dicho prefijo realmente no lo impide, pero si funciona como una advertencia para el programador de que no debe ser una variable accesible, y si necesito sobreescribirla o leerla debo hacerle sus getter y setter.  <br><br>
• b) **falso**, No lo hace imposible sin embargo sufre name mangling asi que toca usar otra direccion que es **_nombredelaclase__nombreoriginaldelatributo**.  <br><br>
• c) **Verdadero**, Como se dice en el punto b, el name mangling esta ligado al nombre de la clase, pues de este depende el como vamos a acceder a esta.  <br><br>

---

### 4) Lectura de código

````python
class Base:
def __init__(self):
self._token = "abc"
class Sub(Base):
def reveal(self):
return self._token
print(Sub().reveal())
````

¿Qué se imprime y por qué no hay error de acceso?
<br><br>
#### ✅ Respuesta:  
Se imprime el contenido de **_token** es decir **"abc"**, no hay error de acceso por que el usar **_** es solamente una convencion, como una advertencia para el programador más no una restriccion apra el compilador, ni en una subclase ni en una parte cualquiera del codigo.

---

### 5) Name mangling en herencia

````python
class Base:
def __init__(self):
self.__v = 1
class Sub(Base):
def __init__(self):
super().__init__()
self.__v = 2
def show(self):
return (self.__v, self._Base__v)
print(Sub().show())
````

¿Cuál es la salida?
<br><br>
#### ✅ Respuesta:  
La salida debe ser primero el contenido de la variable **__v**, es decir **2** y luego el contenido de dicha variable en **Base**, es decir 1, ello por que al heredar Sub de Base la variable antes mencionada en Base sufre name mangling para protegerla de sobreescritura, sin embargo su otra version (la de Sub) se sigue invocando igual.

---

### 6) Identifica el error

````python
class Caja:
  __slots__ = ('x',)
c = Caja()
c.x = 10
c.y = 20
````

¿Qué ocurre y por qué?
<br><br>
#### ✅ Respuesta:  
El error esta en asignar algo al atributo **"y"** de **Caja**, pues en los **__slots__** no hay nungun atributo **"y"** declarado, y si se trata de acceder a algo no declarado en **__slots__** va a generar error, ya que este limita el crear atributos nuevos fuera de este

---

### 7) Rellenar espacios
Completa para que b tenga un atributo “protegido por convención”.

````python
class B:
  def __init__(self):
    self ______ = 99
````

Escribe el nombre correcto del atributo.
<br><br>
#### ✅ Respuesta:  
Suponiendo que vamos a llamar al atributo "number" debe ser **"self._number = 99"**, es decir
````python
class B:
  def __init__(self):
    self._number = 99
````

---

### 8) Lectura de métodos “privados”

````python
class M:

  def __init__(self):
    self._state = 0

  def _step(self):
    self._state += 1
    return self._state

  def __tick(self):
    return self._step()

m = M()
print(hasattr(m, '_step'), hasattr(m, '__tick'), hasattr(m, '_M__tick'))
````

¿Qué imprime y por qué?
<br><br>
#### ✅ Respuesta:  
El resultado deberia ser **True** (pues el metodo "_step" existe en m), **False** (por que aunque "__tick" es un metodo en m, los metodos tambien sufren name mangling), **True** (pues al aplicar el name mangling el acceso al método deberia transformarse y quedar como esta descrito). 

---

### 9) Acceso a atributos privados

````python
class S:
  def __init__(self):
    self.__data = [1, 2]
  def size(self):
    return len(self.__data)

s = S()
# Accede a __data (solo para comprobar), sin modificar el código de la clase:
# Escribe una línea que obtenga la lista usando name mangling y la imprima.
````
Escribe la línea solicitada.
<br><br>
#### ✅ Respuesta:  
El desarrollo de este punto se encuentra en el archivo "Punto9.py"
#### Caso 1
````python
print(s.__data)
````
````
print(s.__data)
          ^^^^^^^^
AttributeError: 'S' object has no attribute '__data'. Did you mean: '_S__data'?
````
En el primer caso, se obtiene un error, pues debido al name mangling no se puede acceder directamente a "__data" y el interprete sugiere cambiar a "_S__data"
#### Caso 2
````python
print(s._S__data)
````
````
[1, 2]
````
Por otro lado, en el segundo caso, obtenemos el print de los elementos de __data al acoplarnos al name mangling

---

### 10) Comprensión de dir y mangling
````python
class D:
  def __init__(self):
    self.__a = 1
    self._b = 2
    self.c = 3
d = D()
names = [n for n in dir(d) if 'a' in n]
print(names)
````
¿Cuál de estos nombres es más probable que aparezca en la lista: __a, _D__a o a? Explica.
<br><br>
#### ✅ Respuesta:  
Segun la documentacion de python sobre dir, este devuelve una lista de cadenas con los nombres de atributos declarados, heredados y algunos especiales como __doc__ que heredan de la clase objeto, siguiendo esto, en el array names, se estan guardando los atributos almacenados en el "__dict__" del objeto que contienen una **"a"**, por lo que descartamos "_b" y "c" y como "__a" se transforma en "_D__a" por el mangling y cumple la condicion, de los definidos este será el unico de los que declaramos en el objeto que se muestre,  sin embargo y como se mencionó, se incluirán tambien algunos heredados de la clase objeto como "__hash__".

---

## 🅱️ Encapsulación con @property y validación
Esta parte trata temas nuevos como lo son la encapsulacion utilizando "@property", y la validación asi que antes que todo investigué un poco de estos y el como cambian la encapsulación que normalmente se ve en java, aprendiendo lo siguiente:  

#### Java  
````java
class Cuenta {
    private double saldo;

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double s) {
        if (s < 0) throw new IllegalArgumentException();
        saldo = s;
    }
}
````

#### Python  
````python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = 0
        self.saldo = saldo  # Usa el setter

    @property
    def saldo(self):            # ← getter
        return self._saldo

    @saldo.setter
    def saldo(self, value):     # ← setter
        if value < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = value
````

#### • "@property" y encapsulación en python:  
Para comenzar, la encapsulacion en python cambia bastante, pues a diferencia de java donde los metodos de getter y setter son mas explicitos, en python nos valemos de "@property" para construir el getter y de "@<prop>.setter" para crear el setter, lo cual cambia un poco la sintaxis pero se puede seguir relacionando con lenguajes que ya conozco.  
#### • Validacion:
Con el tema de la validacion, encontramos que es una especie de condicion para asegurarnos de que en el set unicamente se ingresen valores validos dependiendo nuestros requerimientos, como una forma de limitar nuestros atributos, su sintaxis es mas parecida a la de java, en esto si son similares, cambiando la forma de invocar los errores unicamente.

---

La realizacion de todos estos ejercicios se encuentran en el archivo **B. Encapsulacion.py**

- - -

### 11) Completar propiedad con validación
Completa para que saldo nunca sea negativo.

````python
class Cuenta:
  def __init__(self, saldo):
    self._saldo = 0
    self.saldo = saldo
  @property
  def saldo(self):
    ______
  @saldo.setter
  def saldo(self, value):
    # Validar no-negativo
    ______
````
<br><br>
#### ✅ Respuesta:  
````python
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
c.saldo = -15
print (c.saldo)

````
En el getter que se inicia con el "@property" unicamente retorno el valor de "_saldo" y en el setter, comprobamos si el valor recibido (value) es menor a 0, y si eso es asi hacemos que el programa suelte un error, posteriormente instanciamos el objeto y realizamos los dos casos de uso
````
15
Traceback (most recent call last):
    c.saldo = -15
    ^^^^^^^
    raise ValueError("El saldo no puede ser negativo")
ValueError: El saldo no puede ser negativo
````
y como podemos ver efectivamente, en el primer caso, escribe el valor de 15 que es un numero valido, pero si trata de escribir el valor de -15 nos lanza un error

---