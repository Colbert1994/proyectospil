# Hacer personajes, que hereden atributos, tenga funciones. y si se puede jugar mejor. 
# Ejercicio programacion orientada a objetos
# Tipo MOBA (LOL DOTA CSGO DIABLO)
# Programa que permita al usuario crear un persona. va a tener que tener 2 clases. una clase padre 
# y una hija. en donde el personaje pueda tener diferentes roles. (terroristas o counters)
# tipo lol(top mid adc jg supp)
# una clase personaje, para definir sus atributos y metodos
# crear varias clases hijas de acuerdo al tipo de personaje que quieran usar.
# Crear una clase padre y una clase hijo. de un personaje con todos sus atributos.
# recordar las funciones que tienen los personajes.  acciones
# crear 2 personajes, que tengan vida, que esos personajes se peleen que haya una batalla 
# uno de esos metodos que sea atacar. (movimientos super efectivo, efectivo, etc)
# que tenga una funcion o metodo que tenga atacar, que tenga un valor de daño
# podemos usar una funcion random o randint. 
# una clase padre, una clase hijo que hereden que tenga propiedades algunas y tengan funciones.

# Lo que yo entendi por este ejercicio: crear personajes, que tengan clase padre y clase hija, que la hija herede atributos.
# que estos personajes puedan interactuar. 
# 1ero con elementos. cada jugador tendra 3 personajes de 3 elementos. tierra fuego  agua
# interacciones:
# agua > fuego pero tierra > agua
# fuego > tierra pero agua > fuego
# tierra > agua pero fuego > tierra


# vamos a usar esto para los ataques, criticos, etc
import random

# Clase Padre
class Personajes:
    def __init__(self, elemento, vida, daño):
        self.elemento = elemento
        self.vida = vida
        self.daño = daño

# Clase Hijo
class Jugador(Personajes):
    def __init__(self, elemento, vida, daño, energia):
        super().__init__(elemento, vida, daño)
        self.energia = energia
        
        
    # Metodos
    
    def ataque1(self):
        self.total_atk = self.daño + random.randrange(0, 10)
        print('El ataque fue de: ',self.total_atk)
        return self.total_atk
    def energia1(self):
        self.total_energy = self.energia - 20
        return self.total_energy
    
    def efectividad(self):
        efectivo = self.total_atk + 5
        return efectivo
         
        
        
        
       
elementos = ['Agua', 'Tierra', 'Fuego']
elemento1 = random.choice(elementos)
vida = 100
daño = 40
energia = 100

j1 = Jugador(elemento1, vida, daño, energia)
print(j1.elemento, j1.vida, j1.daño, j1.energia)
atk1 = j1.ataque1()
nrg1 = j1.energia1()
vida_restantej2 = vida - atk1

print('vida jugador2: ', vida_restantej2)
print('El jugador 1 tiene: ',nrg1, 'de energia.')
print('-------------------------------------------------------------------------------------------------------')
elemento2 = random.choice(elementos)
j2 = Jugador(elemento2, vida, daño, energia)
print(j2.elemento, j2.vida, j2.daño, j2.energia)
atk2 = j2.ataque1()
nrg2 = j2.energia1()
vida_restantej1 = vida - atk2
print('vida jugador1: ', vida_restantej1)
print('El jugador 2 tiene: ',nrg2, 'de energia.')
print('-------------------------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------')

if elemento1 == elemento2:
    print('Son del mismo elemento')
    
elif elemento1 != elemento2:
    if elemento1 == 'Agua' and elemento2 == 'Fuego':
        print('Ataque Efectivo')
        j1.energia1()
        j1.efectividad()
        print('+++',j1.efectividad())
    elif elemento1 == 'Agua' and elemento2 == 'Tierra':
        print('Ataque Efectivo')
        j2.energia1()
        j2.efectividad()
        print('---',j2.efectividad())
        
    elif elemento1 == 'Fuego' and elemento2 == 'Tierra':
        print('Ataque efectivo')
        j1.energia1()
        j1.efectividad()
        print('+++', j1.efectividad)
    elif elemento1 == 'Fuego' and elemento2 == 'Agua':
        print('Ataque Efectivo')
        j2.energia1()
        j2.efectividad()
        print('---', j2.efectividad())
        
    elif elemento1 == 'Tierra' and elemento2 == 'Fuego':
        print('Ataque efectivo')
        j2.energia1()
        j2.efectividad()
        print('---', j2.efectividad())
    elif elemento1 == 'Tierra' and elemento2 == 'Agua':
        print('Ataque efectivo')
        j1.energia1()
        j1.efectividad()
        print('+++',j1.efectividad())