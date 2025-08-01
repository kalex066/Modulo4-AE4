
from tamagotchi import Tamagotchi
class Gozarutchi(Tamagotchi):

    def __init__(self,nombre, color, salud=50, felicidad=30, energia=60, entrenamiento=5):
        super().__init__(nombre, color, salud, felicidad, energia)
        self.entrenamiento = entrenamiento
            
    def ir_entrenar(self):
        self.energia -= 20
        self.salud += 15
        self.felicidad += 20
        self.entrenamiento += 1
        print(f"{self.nombre} acaba de hacer su entrenamiento y su nivel de energía es {self.energia}, su salud {self.salud}, su felicidad es {self.felicidad} y su nivel de entrenamiento {self.entrenamiento}")
        if self.energia < 10:
            print(f"Tu tamagotchi {self.nombre} necesita más entrenamiento")
        return self
    
    def presentarse (self):
         print(f"¡Hola yo soy {self.nombre}, de color {self.color}, mi nivel de salud es {self.salud}, mi nivel de energia es {self.energia}, mi nivel de felicidad es {self.felicidad} y he realizado {self.entrenamiento} entrenamientos")
         return self