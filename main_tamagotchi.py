from personat import Persona
from tamagotchi import Tamagotchi
from furawatchi import Furawatchi
from gozarutchi import Gozarutchi

#Crea una instancia de Persona y asígnale una instancia de Tamagotchi al atributo tamagotchi
tamagotchi1 = Tamagotchi("Milktchi", "rojo", 100, 100, 100) #creo una instancia tamagotchi
persona1 = Persona("Amy", "Suarez", tamagotchi1)# Creo una instancia persona

print (f"{persona1.nombre} {persona1.apellido} tiene un Tamagotchi llamado {persona1.tamagotchi}.")

#Haz que la persona le de comer, cure y juegue con su tamagotchi

persona1.darle_comida()
persona1.jugar_con_tamagotchi()
persona1.curarlo()

# creo 2 nuevas instancias tamagotchis utilizando las subclases
tamagotchi2 = Gozarutchi("Gotzarutchi", "azul", 50, 25, 40, 2)
tamagotchi2.presentarse()
tamagotchi2.ir_entrenar()

tamagotchi3 = Furawatchi ("Furawatchi", "rosada", 30, 40, 25, 5)
tamagotchi3.presentarse().cultivar_flores()

# Creo otra instancia persona y le asigno el tamagotchi 2, lo hago jugar y entrenar
persona2 = Persona("David", "Suarez", tamagotchi2)
persona2.jugar_con_tamagotchi()
persona2.tamagotchi.ir_entrenar()

#Creo otra persona para el tamagotchi3 para acceder a los metodos de la subclase 
persona3 = Persona("Marianela", "Perez", tamagotchi3)
persona3.darle_comida()
persona3.tamagotchi.cultivar_flores()
# Listado de Tamagotchies creados
Tamagotchi.muestra_tamagotchis()



