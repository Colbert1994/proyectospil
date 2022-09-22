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
         
        
        
        
# Cosas que fui testeando       
"""elementos = ['Agua', 'Tierra', 'Fuego']
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
print('-------------------------------------------------------------------------------------------------------')"""
def help():
    print('*' * 50)
    print('Ayuda\nLas opciones disponibles son: \n1. Empezar el juego. \n2. Ayuda.\n3. Salir')
    print('*' * 50)
    print('Tambien te recordamos que: \nEl elemento Agua es fuerte contra el elemento Fuego, pero es debil contra el elemento Tierra.')
    print('El elemento Fuego Fuego es fuerte contra el elemento Tierra\nEl elemento Tierra es fuerte contra el Elemento Agua')
    print('*' * 50)
    print('En esta version los elementos seran elegidos aleatoriamente')
    print('*' * 50)
    print('Resumen de efectividad.')
    print('*' * 50)
    print('Agua > Fuego\tAgua < Tierra\nFuego > Tierra\tFuego < Agua\nTierra > Agua\tTierra < Fuego')
    print('*' * 50)
opc = 0
while opc != 3:
    print('-' * 50)
    print('Bienvenidos!!')
    print('-' * 50)
    help()
    opc = int(input('Ingrese su opccion opcion: '))
    if opc == 1:
        nomb_j1 = input('Ingrese el nombre del jugador 1: ')
        print('_' * 50)
        nomb_j2 = input('Ingrese el nombre del jugador 2: ')
        print('_' * 50)
        elementos = ['Agua', 'Tierra', 'Fuego']
        elemento1 = random.choice(elementos)
        vida = 100
        daño = 40
        energia = 100
        print('/' * 50)
        print('Estadisticas del jugador : ',nomb_j1)
        j1 = Jugador(elemento1, vida, daño, energia)
        
        print('Elemento: ',j1.elemento,'\nVida Base: ',j1.vida,'\nDaño Base: ',j1.daño,'\nEnergia Base: ',j1.energia)
        atk1 = j1.ataque1()
        nrg1 = j1.energia1()
        vida_jugador1 = j1.vida
        #vida_restantej2 = vida - atk1
        #print('vida jugador2: ', vida_restantej2)
        #print('El jugador 1 tiene: ',nrg1, 'de energia.')
        print('-' * 50)
        print('Estadisticas del jugador 2: ')
        elemento2 = random.choice(elementos)
        j2 = Jugador('Agua', 100, 40, 100)
        print('Elemento: ',j2.elemento,'\nVida Base: ',j2.vida,'\nDaño Base: ',j2.daño,'\nEnergia Base: ',j2.energia)
        print(j2.elemento, j2.vida, j2.daño, j2.energia)
        atk2 = j2.ataque1()
        nrg2 = j2.energia1()
        vida_jugador2 = j2.vida
        #vida_restantej1 = vida - atk2
        #print('vida jugador1: ', vida_restantej1)
        #print('El jugador 2 tiene: ',nrg2, 'de energia.')
        print('-' * 50)
        
        while vida_jugador1 != 0 or vida_jugador2 != 0:
            print('='*50)
            print('Empezamos!')
            
            if elemento1 == elemento2:
                print('Son del mismo elemento')
                vida_jugador1 = vida_jugador1 - atk2
                j2.energia1()
                vida_jugador2 = vida_jugador2 - atk1
                j1.energia1()      
            elif elemento1 != elemento2:
                if elemento1 == 'Agua' and elemento2 == 'Fuego':
                    print('Ataque Efectivo')
                    vida_jugador2 = vida_jugador2 - (atk1 + j1.efectividad())
                    j1.energia1()
                    print('La vida restante de ', nomb_j2, 'es: ', vida_jugador2)
                    print('+++',j1.efectividad())
                elif elemento1 == 'Agua' and elemento2 == 'Tierra':
                    print('Ataque Efectivo')
                    vida_jugador1 = vida_jugador1 - (atk2 + j2.efectividad())
                    j2.energia1()
                    print('La vida restante de ', nomb_j1,'es: ', vida_jugador1)
                    print('---',j2.efectividad())
                    
                elif elemento1 == 'Fuego' and elemento2 == 'Tierra':
                    print('Ataque efectivo')
                    j1.energia1()
                    vida_jugador2 = vida_jugador2 - (atk1 + j1.efectividad())
                    print('La vida restante de ', nomb_j2,'es: ', vida_jugador2)
                    print('+++', j1.efectividad)
                elif elemento1 == 'Fuego' and elemento2 == 'Agua':
                    print('Ataque Efectivo')
                    j2.energia1()
                    vida_jugador1 = vida_jugador1 - (atk2 + j2.efectividad())
                    print('La vida restante de ', nomb_j1,'es: ', vida_jugador1)
                    print('---', j2.efectividad())
                    
                elif elemento1 == 'Tierra' and elemento2 == 'Fuego':
                    print('Ataque efectivo')
                    j2.energia1()
                    vida_jugador1 = vida_jugador1 - (atk2 + j1.efectividad())
                    print('La vida restante de ', nomb_j1,'es: ', vida_jugador1)
                    print('---', j2.efectividad())
                elif elemento1 == 'Tierra' and elemento2 == 'Agua':
                    print('Ataque efectivo')
                    j1.energia1()
                    vida_jugador2 = vida_jugador2 - (atk1 + j1.efectividad())
                    print('La vida restante de ', nomb_j2,'es: ', vida_jugador2)
                    print('+++',j1.efectividad())
                
    elif opc == 2:
        help()
    else: 
        print('Salir')