import random
opciones=("piedra","papel","tijeras")
def bienvenida():
    print("Vamos a jugar un piedra papel y tijeras, preparate!!")
    print("Es una partida a tres puntos el primero que llegue gana ")

def puntuación(puntos_persona,puntos_ordenador):
    print("Jugador",puntos_persona,"-",puntos_ordenador,"Ordenador")
    
def juego():
    bienvenida()
    puntos_persona=0
    puntos_ordenador=0
    while puntos_persona<3 and puntos_ordenador<3:
        puntuación(puntos_persona,puntos_ordenador)
        persona=input("Elige una de estas tres opciones:piedra,papel,tijeras\n")

        if persona not in opciones:
            print("Escoge una de esas tres no hagas tonterías")
            continue 

        ordenador=random.choice(opciones)
        print("Elijo",ordenador)
        if ordenador==persona:
            print("Hemos empatado,la próxima vez no será así") 
        elif(persona=="piedra"and ordenador=="tijeras") or (persona=="papel" and ordenador=="piedra") or (persona=="tijeras"and ordenador=="papel"):
            puntos_persona+=1
            print("Felicidades me ganaste,la siguiente ya te ganaré")
        else:
            puntos_ordenador+=1
            print("Perdiste,la próxima vez será")

    if puntos_persona==3:
        print("Pero bueno, dicen que lo importante es participar")
    else:
        print("Mientras experimenta el sabor de la derrota JA JA JA")
juego() 



