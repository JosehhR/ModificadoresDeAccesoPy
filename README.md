# 📄Modificadores de Acceso Python

## 📌 Descripción

Este repositorio muestra la solución al taller pre-parcial planteado sobre modificadores de acceso en python 

---

## A. Conceptos y lectura de codigo

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
El desarrollo de este punto se encuentra en el archivo "A.ConceptosyLectura.py"
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

## B. Encapsulación con @property y validación
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

### 12) Propiedad de solo lectura
Convierte temperatura_f en un atributo de solo lectura que se calcula desde
temperatura_c.
 ````python
 class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)
    # Define aquí la propiedad temperatura_f: F = C * 9/5 + 32
````
Escribe la propiedad.
<br>
#### ✅ Respuesta:  

````python
class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)
    # Define aquí la propiedad temperatura_f: F = C * 9/5 + 32
    @property
    def temperatura_f(self):
        return (self._c*9/5+32)
    
t=Termometro(30)
print(f"la temperatura es: {t.temperatura_f} grados fahrenheit")
````

Empleamos "@property" para crear el getter de la propiedad **temperatura_f** y como no requerimos un setter, unicamente retornamos el calculo de la temperatura en grados fahrenheit, el resultado de esto en la salida del codigo es:

````
la temperatura es: 86.0 grados fahrenheit
````

---

### 13) Invariante con tipo

Haz que nombre sea siempre str. Si asignan algo que no sea str, lanza TypeError.

````python
class Usuario:
  def __init__(self, nombre):
    self.nombre = nombre
  # Implementa property para nombre
````

#### ✅ Respuesta:  
 ````python
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
user2=Usuario(15)
print(user2.nombre)
````
Primero implemente un "@property" para el getter y posteriormente cree el setter de este, donde valido que el tipo de dato recibido sea siempre del tipo **string**, si esto no se cumple lanza el **TypeError** en consola, creo dos usuarios e imprimo sus nombres.

````
Jose
Traceback (most recent call last):
  File "e:\Proyectos\2025\UNAL\POO\ModificadoresDeAccesoPy\B. Encapsulacion.py", line 61, in <module>
    user2=Usuario(15)
  File "e:\Proyectos\2025\UNAL\POO\ModificadoresDeAccesoPy\B. Encapsulacion.py", line 47, in __init__
    self.nombre = nombre
    ^^^^^^^^^^^
  File "e:\Proyectos\2025\UNAL\POO\ModificadoresDeAccesoPy\B. Encapsulacion.py", line 57, in nombre
    raise TypeError("Nombre debe contener de manera obligatoria un tipo de dato str")
TypeError: Nombre debe contener de manera obligatoria un tipo de dato str
````
Como se puede ver en la salida de consola, el primer nombre lo imprime de manera correcta, sin embargo, el segundo usuario colapsa el programa al momento de crearlo y nos lanza un **TypeError**, explicando que la propiedad nombre unicamente admite tipos de dato str.

---

### 14) Encapsulación de colección

Expón una vista de solo lectura de una lista interna.

````python
class Registro:
  def __init__(self):
    self.__items = []
  def add(self, x):
    self.__items.append(x)
  # Crea una propiedad 'items' que retorne una tupla inmutable con el contenido
````

#### ✅ Respuesta:  

````python
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
````

Como se puede ver, se agrega el getter con **property** que retorna unicamente una tupla inmutable, como ejemplo creamos un objeto **r**, añadimos los numeros del 1 al 3 y utilizamos nuestro getter para imprimir, de esa manera, la salida por consola es:

````
(1, 2, 3)
````

---

## C. Diseño y refactor
- - -
La realizacion de todos estos ejercicios se encuentran en el archivo **C.DiseñoyRefactorizacion.py**
- - -
### 15) Refactor a encapsulación
Refactoriza para evitar acceso directo al atributo y validar que velocidad sea entre 0 y 200.

````python
class Motor:
    def __init__(self, velocidad):
        self.velocidad = velocidad # refactor aquí
````
Escribe la versión con @property.

#### ✅ Respuesta:  
````python
class Motor:
    def __init__(self, velocidad):
        self._velocidad = 0
        self.velocidad = velocidad # refactor aquí
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, newVelocidad):
        if(newVelocidad>200 or newVelocidad<0):
            raise ValueError("La propiedad velocidad debe estar entre 0 y 200!")
        else:
            self._velocidad=newVelocidad

m=Motor(15)
print(f"velocidad inicial: {m.velocidad}")
m.velocidad = 30
print(f"segunda velocidad: {m.velocidad}")
m.velocidad = 300
print(f"tercera velocidad: {m.velocidad}")
````

Como se puede ver se emplea **property** para crear los getter y el setter con la validacion, y se hacen 3 comprobaciones, el constructor con una velocidad inical, una modificacion a la velocidad a un numero dentro del rango y por ultimo una comprobacion fuera de rango esperando el error en consola, con lo que la salida obtenida es:

````
velocidad inicial: 15
segunda velocidad: 30
Traceback (most recent call last):
  File "e:\Proyectos\2025\UNAL\POO\ModificadoresDeAccesoPy\C.DiseñoyRefactorizacion.py", line 25, in <module>
    m.velocidad = 300
    ^^^^^^^^^^^
  File "e:\Proyectos\2025\UNAL\POO\ModificadoresDeAccesoPy\C.DiseñoyRefactorizacion.py", line 17, in velocidad
    raise ValueError("La propiedad velocidad debe estar entre 0 y 200!")
ValueError: La propiedad velocidad debe estar entre 0 y 200!
````
---

### 16) Elección de convención 
Explica con tus palabras cuándo usarías _atributo frente a __atributo en una API pública de una librería.

#### ✅ Respuesta:  
Yo reduciria el uso de __atributo unicamente a cuando necesite usar herencia pues necesito que no se mezclen atributos en sub clases, mientras que _atributo lo usaria en la mayoria de casos donde quiera señalar que es un atributo interno y no se debe acceder directamente a el.

---

### 17) Detección de fuga de encapsulación
¿Qué problema hay aquí?
````python
class Buffer:
  def __init__(self, data):
    self._data = list(data)
  def get_data(self):
    return self._data
````
Propón una corrección.
#### ✅ Respuesta:  
El problema aca es que el getter de data esta regresando directamente _data, lo que haria que se pueda modificar sin pasar por el objeto de buffer una vez obtenido, lo ideal seria usar una tupla o un copy, pero al ser datos de solo lectura por ser un buffer, considero que lo mejor es devolver una tupla

````python
class Buffer:
  def __init__(self, data):
    self._data = list(data)
  def get_data(self):
    return tuple(self._data)
````

---
### 18) Diseño con herencia y mangling
¿Dónde fallará esto y cómo lo arreglas?

````python
class A:
  def __init__(self):
    self.__x = 1

class B(A):
  def get(self):
    return self.__x
````

#### ✅ Respuesta:  
El error esta en querer acceder al atributo **__x** de la super clase **A** en la subclase **B** pues este sufre name mangling y solo se puede acceder de la forma **_A__x**, es decir:

````python
class A:
  def __init__(self):
    self.__x = 1

class B(A):
  def get(self):
    return self._A__x
````

---

### 19) Composición y fachada

Completa para exponer solo un método seguro de un objeto interno.

````python
class _Repositorio:
  def __init__(self):
    self._datos = {}
  def guardar(self, k, v):
    self._datos[k] = v
  def _dump(self):
    return dict(self._datos)
class Servicio:
  def __init__(self):
    self.__repo = _Repositorio()
# Expón un método 'guardar' que delegue en el repositorio,
# pero NO expongas _dump ni __repo.
````

#### ✅ Respuesta:  
````python
class _Repositorio:
  def __init__(self):
    self._datos = {}
  def guardar(self, k, v):
    self._datos[k] = v
  def _dump(self):
    return dict(self._datos)
class Servicio:
  def __init__(self):
    self.__repo = _Repositorio()
# Expón un método 'guardar' que delegue en el repositorio,
# pero NO expongas _dump ni __repo.
  def guardar(self, k, v):
    self.__repo.guardar(k, v)
````
crearia un metodo publico que unicamente invoque el metodo ya existente de la clase **_Repositorio** llamado **guardar** y le paso los mismos datos que pide inicialmente


---

### 20) Mini-kata

Escribe una clase ContadorSeguro con:
  • atributo “protegido” _n
  • método inc() que suma 1
  • propiedad n de solo lectura
  • método “privado” __log() que imprima "tick" cuando se incrementa
Muestra un uso básico con dos incrementos y la lectura final.

#### ✅ Respuesta:  
````python
class ContadorSeguro:
    def __init__(self):
        self._n=0
        pass
    @property
    def n(self):
        return self._n
    def __log(self):
        print ("tick")
        return
    def inc(self):
        self._n+=1
        self.__log()

cnt = ContadorSeguro()
cnt.inc()
print(f"Actualmente el contador está en: {cnt.n}")
cnt.inc()
print(f"Actualmente el contador está en: {cnt.n}")
````
Como se puede ver, se definio todo tal cual segun los requisitos, y la salida del codigo es:
````
tick
Actualmente el contador está en: 1
tick
Actualmente el contador está en: 2
````

---

## 🎯 Conclusiones
Despues de realizar el taller, logre entender como funciona el encapsulamiento en **python**, y el como se diferencia del que ya conocia en lenguajes como **java** y **dart**, adicionalmente conoci conceptos que muy pocas veces utilizaba como la validacion, que normalmente manejaba desde antes de enviar a los objetos pero nunca a traves del setter, finalmente, aprendi cosas sobre el funcionamiento del interprete de python como el hecho de que al recibir informacion de un getter como listas asigna a la variable donde llega dicha informacion la misma ruta de acceso en el buffer que el atributo de lista inicial y por ello se usan tuplas que son inmutables o la funcion **.copy()** 