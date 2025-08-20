from ursina import *
import subprocess
import os

app = Ursina(title="Cheese Go Time", icon='textures/ursina.ico') # Librería UrsinaEngine
window.fullscreen = True
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = False

fondo_menu = Entity(model='quad', texture='../../resource/fondos/fondo_menu.png', scale=(16, 9), z=1)

Audio("../../resource/sonidos/audio_fondo.wav", autoplay=True, volume=10, loop=True)

def start_game():
    print("Mostrando la introducción...")
    # Codigo para regresar al menu principal
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, '..'))
    menu_path = os.path.join(project_dir,'historia', 'escenario_story.py')
    subprocess.Popen([sys.executable, menu_path])
    application.quit()

def quit_game():
    print("Saliendo del juego...")
    application.quit()

title = Entity(
    model= 'quad',
    text="¡CHEESE GO TIME!",
    scale=(4,2),
    color=color.white,
    texture= '../../resource/interfaz/titulo.png',
    position=(-3, 1),
    z=0
)

start_button = Button( 
    scale=(0.2, 0.1),
    position=(-0.45, -0.1),
    on_click=start_game,
    texture="../../resource/interfaz/inicio.png",
    color=color.white,
)

quit_button = Button(
    scale=(0.1, 0.1),
    position=(-0.25, -0.1),
    on_click=quit_game,
    color=color.white,
    texture="../../resource/interfaz/cerrar.png",
)
app.run() # Iniciar juego
