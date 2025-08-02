class Tamagotchi:
    lista_tamagotchis = []
    def __init__ (self, nombre, color, salud, felicidad, energia):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia
        Tamagotchi.lista_tamagotchis.append(self)

    def jugar(self): #incrementa la felicidad el 10, disminuye la salud en 5
        self.felicidad += 10
        self.salud -= 5
        self.energia -= 20
        print(f"El {self.nombre} está jugando, su felicidad es {self.felicidad}, su salud {self.salud} y su energía ha disminuido a {self.energia}")
        return self
    
    def comer(self): #comer(): incrementa la felicidad en 5, aumenta la salud en 10
        self.felicidad += 5
        self.salud -= 10
        self.energia += 20
        print(f"El {self.nombre} está comiendo, su felicidad es {self.felicidad}, su salud {self.salud} y su energia {self.energia}")
        return self
   
    def curar(self):#curar(): incrementa la saludo en 20, disminuye la felicidad en 5
        self.salud += 20
        self.felicidad -= 5
        print(f"El {self.nombre} está siendo curado, su felicidad es {self.felicidad}, su salud {self.salud} y su energía se mantiene en {self.energia}" )
        return self
    
    def presentarse(self):
        raise NotImplementedError
    
    @classmethod
    def muestra_tamagotchis(cls):
        for i in cls.lista_tamagotchis: 
            print(f"Nombre: {i.nombre}. Color: {i.color}. Salud: {i.salud}. Felicidad: {i.felicidad}. Energía: {i.energia}")

        




    