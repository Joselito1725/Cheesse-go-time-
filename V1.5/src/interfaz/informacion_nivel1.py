import os
import sys
import subprocess
from ursina import *
from typing import Any
import time

class tiempo(Entity): # Codigo del temporizador
    def __init__(self):
        super().__init__()
         # Crear el temporizador
        self.time_left = 240 # 240 segundos de tiempo limite para ganar (4 minutos)
        self.timer_text = Text(text=f' {self.time_left} ',position=(-.775, .375),scale=1.30,color=color.white)
        # Variables del juego
        self.game_running = True
        
    def update(self):
        if not self.game_running:
            return
          
        # Actualizar temporizador
        if self.time_left > 0:
            self.time_left -= time.dt
            self.timer_text.text = f' {int(self.time_left)} '
        else:
            self.game_over()
            return
            
    def game_over(self):
        application.pause() # Pausa el juego
        Audio("../../resource/sonidos/perdiste.wav", autoplay=True, volume=1, loop=False) # Audio GameOver
        Audio("../../resource/sonidos/tuberias.wav", autoplay=True, volume=1, loop=True) # Audio de agua
        
        fondo = Entity(model = "quad",color=color.rgba(0, 255, 236, 0.5),scale=(16, 9), z=-3, x= 0)
        fondo = Entity(model= "quad" ,color=color.rgba(0, 255, 236, 0.5), scale=(16, 9), z=-3, x=16)
        fondo = Entity(model= "quad" ,color=color.rgba(0, 255, 236, 0.5), scale=(16  , 9), z=-3, x=32)
        
        Button(texture='../../resource/interfaz/fondo.png',origin=(0, 0),scale=(.5, .2),color=color.white, z=2)
        Text( text=f'GAME OVER',origin=(0, 0.2),scale=2,color=color.red,background=True, z=1)
        global contador_quesos
        print_on_screen(text=f"Quesos recogidos: {contador_quesos}/5", origin=(0, 2))
        
        # OPCION REGRESAR DE GAME OVER==============
        boton_regresar = Button(texture='../../resource/interfaz/salir.png',color=color.white,scale=(0.1, 0.1),position=(-0.1, -0.2),on_click=regresar, z=1) # Crea el botón para regresar        
        boton_reiniciar = Button(texture='../../resource/interfaz/reiniciar.png',color=color.white ,scale=(0.1, 0.1),position=(0.1, -0.2),on_click=reiniciar, z=1)# Ajusta la posición del botón
        
def botones(): # Función botones 
    # Carga de imágenes
    c = load_texture('../../resource/interfaz/cerrar.png')    
    s = load_texture('../../resource/interfaz/salir.png')    
    r = load_texture('../../resource/interfaz/regresar.png')  
    f = load_texture('../../resource/interfaz/reiniciar.png') 
    t = load_texture('../../resource/interfaz/tiempo.png') 
    b = load_texture('../../resource/interfaz/borde.png') 
    p_1 = load_texture('../../resource/interfaz/potenciador.png') 
    p_2 = load_texture('../../resource/interfaz/PowerUpJump.png') 
    q = load_texture('../../resource/interfaz/queso.png')
    v = load_texture("../../resource/interfaz/vida.png")
    
    # Mensaje en pantalla de instrucciones para el jugador
    print_on_screen("""A - D / PARA PODER MOVERTE""", position=(-0.55, -0.359), scale=1, duration=5)   
    print_on_screen("""BARRA ESPACIADORA PARA SALTAR""", position=(-0.58, -0.38), scale=1, duration=5) 
    
    def regresar(): # Función para regresar al menú
        print("Regresando...")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir, '..'))
        menu_path = os.path.join(project_dir,'index', 'inicio_juego.py')
        subprocess.Popen([sys.executable, menu_path])
        application.quit()
    
    def salir(): # Función para salir del juego
        print("Saliendo...")
        application.quit()
    
    # BLOQUES DE DISEÑO DE BOTONES============================
    # fondos:
    #Fondo - tiempo
    boton_fondo =Button(texture= t, scale=(0.2, 0.1), color=color.white, position=(-.78, .35))
    
    #Fondo - iconos
    boton_fondo =Button(texture= b, scale=(0.18, 0.07), color=color.white, position=(-.77, .27))
    boton_fondo =Button(texture= b, scale=(0.18, 0.07), color=color.white, position=(-.77, .20))
    boton_fondo =Button(texture= b, scale=(0.18, 0.07), color=color.white, position=(-.77, .13))
    boton_fondo =Button(texture= b, scale=(0.18, 0.07), color=color.white, position=(-.77, .06))
    
    #EXTRAS - DISEÑOS
    vidas = Button(texture=v,  color=color.white, scale=(0.04, 0.04), position=(-.83, .27))
    
    queso = Button(texture =q, color=color.white, scale=(0.04, 0.04), position=(-.83, .20))
    
    power_up1 = Button(texture =p_1, color=color.white, scale=(0.05, 0.05), position=(-.83, .13))

    power_up2 = Button(texture =p_2, color=color.white, scale=(0.05, 0.05), position=(-.83, .06))
    
    
    # Crear botón de salida
    boton_salir = Button(texture= c, color=color.white, scale=(0.05, 0.05), position=(-.85, .44), on_click=salir)
    
    # Crear botón de regreso
    boton_regresar = Button(texture= s, scale=(0.05, 0.05), color=color.white, position=(-.78, .44), on_click=regresar)
    
    # Crea botón de reinicio
    boton_reiniciar =Button(texture= f, scale=(0.05, 0.05), color=color.white, position=(-.71, .44), on_click=reiniciar)
    

def regresar(): # Función para el botón regresar a inicio
    print("Regresando al menú...")
    # Codigo para regresar al menu principal
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, '..'))
    menu_path = os.path.join(project_dir, 'index', 'inicio_juego.py')
    subprocess.Popen([sys.executable, menu_path])
    application.quit()

def reiniciar(): # Función para el botón reiniciar nivel
    print("Reiniciando nivel...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, '..'))
    menu_path = os.path.join(project_dir,'index', 'nivel_1.py')
    subprocess.Popen([sys.executable, menu_path])
    application.quit()

def temporizador(): # Función que retorna la clase de tiempo para llamarla como módulo
    return tiempo()