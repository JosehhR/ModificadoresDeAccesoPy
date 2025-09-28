#Autor: Jose Luis Ramirez
# Este codigo ilustra el desarrollo de los puntos 15 a 20 del taller que involucra la refactorizacion de algunos ejercicios 


#15) Refactoriza para evitar acceso directo al atributo y validar que velocidad sea entre 0 y 200.

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