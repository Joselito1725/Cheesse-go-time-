from typing import Any
from ursina import *
import os

# Importar modulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.estructuracion.estructura_nivel1 import parte_1, parte_2
from src.interfaz.informacion_nivel1 import botones, temporizador
from src.jugador.jugador import Player, update_player
from src.jugador.interaccion_nivel1 import interaccion_nivel1

#! Inicia el juego
app = Ursina(title="Nivedl 1 - Alcantarillas")

camera.orthographic = True
camera.fov = 8

window.fullscreen = True
window.show_ursina_splash = True
window.exit_button.visible = False
window.exit_button.text = ""
window.fps_counter.enabled = False


# Fondo del nivel
fondo_nivel = Entity(model="quad", texture="../../resource/fondos/fondo_nivel1.jpg", scale=(16, 9), z=2, x=0)
fondo_nivel = Entity(model="quad", texture="../../resource/fondos/fondo_nivel1.jpg", scale=(16, 9), z=2, x=16)
fondo_nivel = Entity(model="quad", texture="../../resource/fondos/fondo_nivel1.jpg", scale=(16  , 9), z=2, x=32)
fondo_nivel = Entity(model="quad", texture="../../resource/fondos/fondo_relleno.png", scale=(16  , 9), z=-2, x=38.18)



# Audio de fondo del nivel
Audio("../../resource/sonidos/audio_fondo.wav", autoplay=True, volume=0.7, loop=True)


# Estructura y limites
estructura_nivel_1 = parte_1()
plataformas = parte_2()


def update():
    for plataforma in plataformas:
        plataforma.update()


# Interfaz del juego
direccion = botones()
temporizador_nivel1 = temporizador()


# Jugador y movimiento
player, anim = Player(2)

def input(key: Any):
    update_player(key, player, anim)

# interacción con el Jugador
coleccionar = interaccion_nivel1(player)

def update():
    coleccionar.update()

app.run()