import random
from funciones import sacar_carta, mostrar_baraja, cargar_puntajes, guardar_puntajes
def crear_baraja():
    return {(valor, palo)
    for valor in ("1", "2", "3", "4", "5", "6", "7", "10", "11", "12")
    for palo in ("Oro", "Espada", "Copa", "Basto")}
#genera una baraja como un set de tuplas recorriendo cada una de las posibles combinaciones entre los valores y el palo
def jugar_ronda(baraja:set, puntajes:dict):
    print("\n Nueva Ronda")
    carta_jugador = sacar_carta(baraja)
    carta_maquina = sacar_carta(baraja)
    print(f"Tu carta: {carta_jugador[0]} de {carta_jugador[1]}")
    print(f"Carta de la máquina: {carta_maquina[0]} de {carta_maquina[1]}")
    if carta_jugador == ("1", "Oro"):
        print("¡Ganaste esta ronda!")
        puntajes["jugador"]+=1
        return True  
    elif carta_maquina == ("1", "Oro"):
        print("La máquina ganó esta ronda.")
        puntajes["maquina"]+=1
        return True  
    else:
        print("Nadie ganó esta ronda.")
        return False 
#funcion para jugar una ronda en este juego y agregar puntajes

def main():
    print("Saca el 1 de Oro")
    nombre_archivo="puntajes.txt"
    puntajes=cargar_puntajes(nombre_archivo)
    baraja = crear_baraja()
    print(f""" Puntajes actuales del jugador: {puntajes["jugador"]} y Máquina: {puntajes["maquina"]}
        Baraja inicial:""", mostrar_baraja(baraja))
    while True:
        if not baraja:
            print("La baraja se ha agotado. Reiniciando")
            baraja = crear_baraja()
# Si la baraja está vacía, se reinicia
        reiniciar = jugar_ronda(baraja,puntajes)
        if reiniciar:
            print("Alguien sacó el 1 de Oro. La baraja se reinicia.")
            baraja = crear_baraja()
# Si alguien saca el 1 de Oro, se reinicia el mazo
        continuar = input("¿Queres jugar otra ronda? (s/n): ").strip().lower()
        if continuar != "s":
            break

    print(f"Puntajes finales: Jugador {puntajes['jugador']} - Máquina {puntajes['maquina']}. Gracias por jugar")
    guardar_puntajes(nombre_archivo, puntajes)
#funcion principal del juego
main()


#Chequear cuando se usa cada tipo de dato
#agregar funciones que reciben funciones
#definir tipos de parametros en funciones y documentar funciones
#agregar puntaje para ver cuantas veces gano cada uno por archivo