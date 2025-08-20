from ursina import *
import os
import sys
import subprocess
from ursina.text import Text

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
cinematica = os.path.join(project_dir,'historia', 'texto_story.md')

app = Ursina(title="Cinemática")

window.fullscreen = True
window.title = "¡CHEESE GO TIME!"
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = False


font = 'TIMES NEW ROMAN.TTF'
background = Entity(model='quad', scale=(16, 10), texture='../../resource/fondos/fondo_menu_historia.jpg')

Audio("../../resource/sonidos/audio_fondo.wav", autoplay=True, volume=0.7, loop=True)

# Primero leemos el archivo
with open(cinematica, 'r', encoding='utf-8') as archivo:
    texto_story_markdown = archivo.read()

# Procesamos el texto: eliminamos los asteriscos de markdown y dividimos por líneas
intro = texto_story_markdown.replace('*', '').split('\n')

# Lista para almacenar los objetos de texto
texto = []
ancho_pantalla = 18
posicion_y = 0.4

# texto línea por línea
for intro in intro:
    if intro and not intro.startswith('!['):# Ignoramos las líneas vacías y la línea de la imagen
        texto.append(Text(
            text=intro,  # Eliminamos espacios en blanco extras
            scale=(1.5, 1.2),
            x=0,
            y=posicion_y,  # Posición vertical
            color=color.white,
            origin=(0, 30)  # Añadimos origin para mejor control del posicionamiento
        ))
        posicion_y -= 0.03
    
velocidad = 0.0009
animate = True

mensaje= Text(
    text="Presione Space para iniciar nivel...",
    scale=(1.2, 1.1),
    x=0.4,
    y=-0.4,
    color=color.green,
    origin=(0, 0)
)

#posición de reinicio de lectura
posicion_y = [t.y for t in texto]

def update():
    global animate
    if animate:
        for t in texto:
            t.y += velocidad
            if t.y < -.5:
                t.y = .5
            

def input(key):
    if key == 'space':
        # Codigo para regresar al menu principal
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir, '..'))
        menu_path = os.path.join(project_dir,'index', 'nivel_1.py')
        subprocess.Popen([sys.executable, menu_path])
        application.quit()
app.run()