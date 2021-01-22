#Codigo para inteligencia artificial basica
import time
from random import choice
respuesta1 = input("Soy Diox, en que le puedo ayudar?"'\n')

tm_tiempo = time.localtime()

def tiempo():
    global respuesta1
    if respuesta1 == "Que hora es":
        print(time.asctime(tm_tiempo))
    else:
        chiste()
        

def chiste():
    global respuesta1
    if respuesta1 == "Cuentame un chiste":
        print(choice(["¿Qué sale de la cruza entre un mono y un pato? \n ¡Un monopatín!","- ¿Tienes WiFi? \n - Sí \n - ¿Y cuál es la clave? \n- Tener dinero y pagarlo."," Soy Rosa. \n - Ah, perdóname, es que soy daltónico."]))
    else:
        respuesta1 = input("Disculpe no le he entendido, ¿puede repetir?")
        tiempo()


tiempo()