import random
opciones=("piedra","papel","tijeras")
def juego():
    persona=input("Elige una de estas tres opciones:piedra,papel,tijeras")
    if persona!=opciones:
        print("Escoge una de esas tres no hagas tonterías")
        return
   
juego()      

