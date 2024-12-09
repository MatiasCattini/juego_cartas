import random
def sacar_carta(baraja:set):
    carta = random.choice(list(baraja)) 
    baraja.remove(carta)  
    return carta
#saca una carta aleatoria del mazo y la eliminala

def mostrar_baraja(baraja:set):
    return ", ".join([f"{valor} de {palo}" for valor, palo in baraja])
#genera un print de la baraja completa

def cargar_puntajes(nombre_archivo: str) -> dict:
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = archivo.read().strip()
            if datos:
                return eval(datos)
    except FileNotFoundError:
        pass
    return {"jugador": 0, "maquina": 0}
#Carga los puntajes desde un archivo de texto o inicializa en 0 si no existe.
def guardar_puntajes(nombre_archivo: str, puntajes: dict) -> None:
    with open(nombre_archivo, "w") as archivo: 
        archivo.write(str(puntajes)) 
#guarda los puntajes obtenidos