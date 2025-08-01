from tamagotchi import Tamagotchi
class Persona:
    def __init__ (self, nombre, apellido, tamagotchi):
        self.nombre =  nombre
        self.apellido = apellido
        self.tamagotchi= tamagotchi 
    
    def jugar_con_tamagotchi(self): 
        print(f"{self.nombre} esta jugando con {self.tamagotchi.nombre}")
        self.tamagotchi.jugar()
        return self

    def darle_comida(self):
        print(f"{self.nombre} le está dando de comer a {self.tamagotchi.nombre}")
        self.tamagotchi.comer()
        return self

    def curarlo(self):
        print(f"{self.nombre} está curando a {self.tamagotchi.nombre}")
        self.tamagotchi.curar()
        return self
    
   