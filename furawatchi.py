from tamagotchi import Tamagotchi
class Furawatchi(Tamagotchi):

    def __init__(self,nombre, color, salud=45, felicidad=50, energia=60, flores=10):
        super().__init__(nombre, color, salud, felicidad, energia)
        self.flores = flores
            
    def cultivar_flores(self):
        self.energia -= 5
        self.felicidad += 15
        self.flores += 1
        print(f"{self.nombre} ha cultivado {self.flores} flores, su energia es {self.energia} y su felicidad es {self.felicidad}")
        if self.felicidad < 5:
            print(f"Tu tamagotchi {self.nombre} necesita cultivar más flores")
        return self
    
    def presentarse (self):
         print(f"¡Hola yo soy {self.nombre}, he cultivado {self.flores} y por eso mi nivel de felicidad es {self.felicidad}")
         return self