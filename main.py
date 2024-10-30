import random
opciones=("piedra","papel","tijeras")
def juego():
    persona=input("Elige una de estas tres opciones:piedra,papel,tijeras\n")
    
    if persona not in opciones:
        print("Escoge una de esas tres no hagas tonterías")
        return
    
    ordenador=random.choice(opciones)
    print("Elijo",ordenador)
    if ordenador==persona:
        print("Hemos epatado,la próxima vez no será así")
        return
    elif(persona=="piedra"and ordenador=="tijeras") or (persona=="papel" and ordenador=="piedra") or (persona=="tijeras"and ordenador=="papel"):
        print("Felicidades me ganaste,la próxima no será así")
        return
    else:
        print("Perdiste la próxima vez será")
        return
juego()      

