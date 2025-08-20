from ursina import *
import os
import sys
import subprocess
import time

# CAMARA
class HorizontalFollow(Entity):
    def __init__(self, target, offset=[0,0], speed=4):
        super().__init__(parent=camera)
        self.target = target
        self.offset = offset
        self.speed = speed
        
    def update(self):
        camera.x = lerp(camera.x, self.target.x + self.offset[0], self.speed * time.dt)
        camera.y = -0.2

# OBJETOS=========================
PowerUp_walkVelocity = '../../resource/interfaz/potenciador.png' # ruta de acceso de textura de los potenciadores
PowerUp_DobleJump = '../../resource/interfaz/PowerUpJump.png'    ##
contador_quesos = 0 # Contador de quesos
vidas = 3 # Vidas del jugador

# objeto queso
class Queso(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.model = 'quad'
        self.color = color.white
        self.scale = 0.3
        self.position = Vec2(x)
        self.collider = 'sphere'
        self.texture = '../../resource/interfaz/queso.png'
        self.y_offset = 0
        self.original_y = y
        
    def update(self): # Hace que el queso se mueva arriba y abajo (animación)
        self.y_offset = math.sin(time.time() * 2) * 0.1
        self.y = self.original_y + self.y_offset

# objeto potenciador
class PowerUp(Entity):
    def __init__(self, x, y, tex):
        super().__init__()
        self.model = 'quad'
        self.color = color.white
        self.scale = 0.4
        self.position = Vec2(x)
        self.collider = 'sphere'
        self.texture = tex
        self.y_offset = 0
        self.original_y = y
    def update(self): # Hace que el potenciador se mueva arriba y abajo (animación)
        self.y_offset = math.sin(time.time() * 2) * 0.1
        self.y = self.original_y + self.y_offset
# Temporizador del potenciador anterior
class Temporizador_up1(Entity): # PowerUp1
    def __init__(self):
        super().__init__()
        self.time_left = 20
        self.timer_text = Text(
            text=f'{self.time_left}',
            position=(-.75, .14),
            scale=0.9,
            background=True,
            color=color.white)
    def update(self):
        if self.time_left > 0:
            self.time_left -= time.dt
            self.timer_text.text = f'{int(self.time_left)}'
            
class Temporizador_up2(Entity): # PowerUp2
    def __init__(self):
        super().__init__()
        self.time_left = 20
        self.timer_text = Text(
            text=f'{self.time_left}',
            position=(-.75, .07),
            scale=0.9,
            background=True,
            color=color.white)
    def update(self):
        if self.time_left > 0:
            self.time_left -= time.dt
            self.timer_text.text = f'{int(self.time_left)}'
        else:
            destroy(self.timer_text)

class trampa(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.model='quad'
        self.color=color.green
        self.scale=(0.3, 0.07, 0.2)
        self.z = 0
        self.position=(x, y)
        self.collider = "box"
        
class vida(Entity):
    def __init__(self, x, y):
        super().__init__()
        super().__init__()
        self.model = 'quad'
        self.color = color.white
        self.scale = 0.25
        self.position = Vec2(x)
        self.collider = 'sphere'
        self.texture = '../../resource/interfaz/vida.png'
        self.y_offset = 0
        self.original_y = y
        
    def update(self): # Hace que el queso se mueva arriba y abajo (animación)
        self.y_offset = math.sin(time.time() * 2) * 0.1
        self.y = self.original_y + self.y_offset
        
class agua(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.color = color.azure
        self.scale=(20, 2, 0.2)
        self.position=(20.2, -4.62)
         
class gameover_por_agua(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.color = color.clear
        self.scale=(20, 2, 0.2)
        self.position=(20.2, -7)
        self.collider = "box"
        
# Final de parte 1 / comienzo de parte 2
class Final_part1(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'
        self.color = color.white
        self.scale = (1, 1)
        self.position = (7.20, -2.60)
        self.collider = 'sphere'
        self.texture = '../../resource/objetos/p2_abajo_izquierda.png'

# Final de parte 2 / Final del nivel 1
class Final(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'
        self.color = color.clear
        self.scale = (0.7, 0.7)
        self.position = (30.5, 3.40)
        self.collider = 'sphere'
        self.texture = '../../resource/objetos/final.png'

# Recogibles
class CollectiblesManager:
    def __init__(self, player):
        self.player = player
        self.contador_mensaje = Text(text='0/5', position=(-.77, .21), scale=1, color=color.white)
        self.contador_vidas = Text(text='3', position=(-.75, .285), scale=1, color=color.white)
        self.setup_collectibles()
    
    def setup_collectibles(self):
        global vidas
        
        # INSTANCIAS RECOGIBLES
        self.queso1 = Queso(4.5, -.5)
        self.queso2 = Queso(9, -3.35)
        self.queso3 = Queso(10.9, 1.30)
        self.queso4 = Queso(18.5, 2.50)
        self.queso5 = Queso(26.4, 0)

        self.power_up = PowerUp(-6.8, -1, PowerUp_walkVelocity)
        self.power_up2 = PowerUp(12.9, 0.15, PowerUp_DobleJump)
        
        self.trampa1 = trampa(2, 2.99)
        self.trampa2 = trampa(14, 2.77)
        self.trampa3 = trampa(26.5, 3.02)
        
        self.vida1 = vida(9.5, -1)
        self.vida2 = vida(18.5,-2.5)
        self.vida3 = vida(23.4, 0)
        
        self.agua = agua()
        self.gameover_agua = gameover_por_agua()

        self.tubo_part1 = Entity(model='quad', texture='../../resource/objetos/p1_arriba.png', color=color.white, scale=(0.60, 2, 0.2), position=(5.05, 3.70), collider='box')
        self.tubo_part2 = Entity(model='quad', texture = '../../resource/objetos/p1_arriba.png', color=color.white, scale=(0.60, 1.10, 0.2), position=(22.9, 0), collider='box')
        
        self.final_partone = Final_part1()
        self.final = Final()
        
    def update(self):
        # VERIFICACIÓN DE COLISIONES ENTRE JUGADOR / OBJETO
        # Colision queso
        if self.queso1.enabled and self.player.intersects(self.queso1): # Queso
            self.quesos_datos()
            self.queso1.disable()
            
        if self.queso2.enabled and self.player.intersects(self.queso2): # Queso
            self.quesos_datos()
            self.queso2.disable()

        if self.queso3.enabled and self.player.intersects(self.queso3): # Queso
            self.quesos_datos()
            self.queso3.disable()
        
        if self.queso4.enabled and self.player.intersects(self.queso4): # Queso
            self.quesos_datos()
            self.queso4.disable()

        if self.queso5.enabled and self.player.intersects(self.queso5): # Queso
            self.quesos_datos()
            self.queso5.disable()
        
        # Colisiones PowerUps
        if self.power_up.enabled and self.player.intersects(self.power_up): # Potenciador
            self.recoger_potenciador_walk()
            
        if self.power_up2.enabled and self.player.intersects(self.power_up2): # Potenciador
            self.recoger_potenciador_jump()
        
        # Colision Agua        
        if self.gameover_agua.enabled and self.player.intersects(self.gameover_agua):
            self.game_over()
            
        # Colision Trampa
        if self.trampa1.enabled and self.player.intersects(self.trampa1):
            self.player.position = (0, 2.90)
            self.perder_vida()
        
        if self.trampa2.enabled and self.player.intersects(self.trampa2):
            self.player.position = (15.7, 2.75)
            self.perder_vida()
            
        if self.trampa3.enabled and self.player.intersects(self.trampa3):
            self.player.position = (24.2, 3.02)
            self.perder_vida()
        
        # Colision vida
        if self.vida1.enabled and self.player.intersects(self.vida1):
            if vidas < 3:
                self.ganar_vida()
                self.vida1.disable()
                print_on_screen(text="¡Vida recogida!", position=(-.67, .28), scale=1)
            elif vidas == 3:
                self.cooldow_vidas()
                print_on_screen(text="¡Vidas completas!", position=(-.67, .28), scale=1)
        
        if self.vida2.enabled and self.player.intersects(self.vida2):
            if vidas < 3:
                self.ganar_vida()
                self.vida2.disable()
                print_on_screen(text="¡Vida recogida!", position=(-.67, .28), scale=1)
            elif vidas == 3:
                self.cooldow_vidas()
                print_on_screen(text="¡Vidas completas!", position=(-.67, .28), scale=1)
                
        if self.vida3.enabled and self.player.intersects(self.vida3):
            if vidas < 3:
                self.ganar_vida()
                self.vida3.disable()
                print_on_screen(text="¡Vida recogida!", position=(-.67, .28), scale=1)
            elif vidas == 3:
                self.cooldow_vidas()
                print_on_screen(text="¡Vidas completas!", position=(-.67, .28), scale=1)
        
        
        # Colisiones metas
        if self.final_partone.enabled and self.player.intersects(self.final_partone): # final Parte 1
            self.final_part1()

        if self.final.enabled and self.player.intersects(self.final): # Meta final
            global contador_quesos
            if contador_quesos == 5:
                self.llegar_a_meta()
            else:
                print_on_screen(text=f"Oh ¡quedan quesos por recoger! {contador_quesos}/5", origin=(0, 2))
        
    # Funciones de los objetos
    # Quesos
    def quesos_datos(self):
        global contador_quesos
        contador_quesos += 1
        self.contador_mensaje.text =f' {str(contador_quesos)}/5' # mensaje de cuantos quesos van en la clase CCollectiblesManager
        Audio('../../resource/sonidos/recoger_comida.wav', autoplay=True, loop=False, volume=10)
        notificacion = Text("¡¡Queso recogido!!", position=(-.65, .21), scale=1, color=color.yellow, background=True)
        destroy(notificacion, delay=3.5)
        if contador_quesos == 1:
            self.tubo_part1.disable()
        elif contador_quesos == 5:
            self.tubo_part2.disable()
    
    # Potenciadores
    # PowerUp +velocidad
    def recoger_potenciador_walk(self):
        self.power_up.disable()
        self.temporizador = Temporizador_up1()
        Audio('../../resource/sonidos/potenciador.wav', autoplay=True, loop=False, volume=10)
        self.potenciador_audio = Audio('../../resource/sonidos/cuenta_regresiva.wav', autoplay=True, volume=0.5, loop=True)  # Iniciar audio del potenciador
        notificacion = Text("¡PowerUp activado!", position=(-.65, .14), scale=1, background=True, color=color.white)
        destroy(notificacion, delay=3.5)
        self.player.walk_speed *= 1.85
        invoke(self.volver_a_la_normalidad_walk, delay=20)
    def volver_a_la_normalidad_walk(self):
        notificacion = Text("¡PowerUp desactivado!", position=(-.65, .14), scale=1, color=color.red, background=True,)
        destroy(notificacion, delay=3.5)
        self.player.walk_speed /= 1.5
        if self.potenciador_audio: # Detener audio de cuenta_regresiva
            self.potenciador_audio.stop()
    
    # PowerUp doble salto
    def recoger_potenciador_jump(self):
        self.power_up2.disable()
        self.temporizador = Temporizador_up2()
        Audio('../../resource/sonidos/potenciador.wav', autoplay=True, loop=False, volume=10)
        self.potenciador_audio = Audio('../../resource/sonidos/cuenta_regresiva.wav', autoplay=True, volume=0.5, loop=True)  # Iniciar audio del potenciador
        notificacion = Text("¡PowerUp activado!", position=(-.65, .07), scale=1, background=True,)
        destroy(notificacion, delay=3.5)
        self.player.max_jumps = 2
        invoke(self.volver_a_la_normalidad_jump, delay=20)
    def volver_a_la_normalidad_jump(self):
        notificacion = Text("¡PowerUp desactivado!", position=(-.65, .07), scale=1, color=color.red, background=True,)
        destroy(notificacion, delay=3.5)
        self.player.max_jumps = 1
        if self.potenciador_audio: # Detener audio de cuenta_regresiva
            self.potenciador_audio.stop() 
    
    # Trampa: perder vida
    def perder_vida(self):
        Audio('../../resource/sonidos/acido.wav', autoplay=True, loop=False)
        global vidas
        vidas -= 1
        self.contador_vidas.text =f' {str(vidas)}'
        if vidas == 0:
            self.game_over()
    
    # Trampa: ganar vida
    def ganar_vida(self):
        Audio('../../resource/sonidos/vida.wav', autoplay=True, loop=False)
        global vidas
        vidas += 1
        self.contador_vidas.text =f' {str(vidas)}'
    
    # Cooldown vidas para poder traspasarlas si tienes vidas completas
    def cooldow_vidas(self):
        self.vida1.collider = None
        self.vida2.collider = None
        self.vida3.collider = None
        invoke(self.reactivar_vidas, delay=3)
    def reactivar_vidas(self):
        self.vida1.collider = "sphere"
        self.vida2.collider = "sphere"
        self.vida3.collider = "sphere"
        
    # Final parte 1
    def final_part1(self):
        self.final_partone.disable()
        destroy(self.tubo_part1)
        # Movimiento de cámara Fov
        camera.orthographic = True
        camera.fov = 8
        horizontal_follow = HorizontalFollow(target=self.player, offset=[3,0], speed=4)
     
     # Final parte 2
    def llegar_a_meta(self):
        self.final.disable()
        global contador_quesos
        print_on_screen(text=f"Quesos recogidos: {contador_quesos}/5", origin=(0, 2))
        Audio('../../resource/sonidos/Ganastes.wav', autoplay=True, loop=False)
        application.pause() # Pausa el juego
        Button(texture='../../resource/interfaz/fondo.png',origin=(0, 0),scale=(.5, .2),color=color.white, z=2)
        Text(text=f'¡¡¡GANASTE!!!',origin=(0, 0),scale=2,color=color.red,background=True, z=1)# Texto 
 
                
        # OPCIONES DEL NIVEL==============
        boton_regresar = Button(texture='../../resource/interfaz/salir.png',color=color.white,scale=(0.1, 0.1),position=(-0.1, -0.2),on_click=regresar, z=1) # Crea el botón para regresar
        boton_reiniciar = Button(texture='../../resource/interfaz/reiniciar.png',color=color.white,scale=(0.1, 0.1),position=(0.1, -0.2),on_click=reiniciar,z=1)# Ajusta la posición del botón
        
    # GameOver
    def game_over(self):
        application.pause() # Pausa el juego
        Audio("../../resource/sonidos/perdiste.wav", autoplay=True, volume=1, loop=False) # Audio GameOver
        Audio("../../resource/sonidos/tuberias.wav", autoplay=True, volume=1, loop=False) # Audio Tuberias
        
        fondo = Entity(model = "quad",color=color.rgba(0, 255, 236, 0.5),scale=(16, 9), z=-3, x= 0) # Fondo azulado
        #fondo = Entity(model = "quad",color=color.rgba(0, 0, 0, 0.5),scale=(16, 9), z=-3, x= 0) # Fondo negro
        fondo = Entity(model= "quad" ,color=color.rgba(0, 255, 236, 0.5), scale=(16, 9), z=-3, x=16) # Fondo azulado
        #fondo = Entity(model= "quad" ,color=color.rgba(0, 0, 0, 0.5), scale=(16, 9), z=-3, x=16) # Fondo negro
        fondo = Entity(model= "quad" ,color=color.rgba(0, 255, 236, 0.5), scale=(16  , 9), z=-3, x=32) # Fondo azulado
        #fondo = Entity(model= "quad" ,color=color.rgba(0, 0, 0, 0.5), scale=(16  , 9), z=-3, x=32) # Fondo negro
        
        Button(texture='../../resource/interfaz/fondo.png',origin=(0, 0),scale=(.5, .2),color=color.white, z=2)
        Text( text=f'GAME OVER',origin=(0, 0.2),scale=2,color=color.red,background=True, z=1)
        global contador_quesos
        print_on_screen(text=f"Quesos recogidos: {contador_quesos}/5", origin=(0, 2))
        
        # OPCION REGRESAR DE GAME OVER==============
        boton_regresar = Button(texture='../../resource/interfaz/salir.png',color=color.white,scale=(0.1, 0.1),position=(-0.1, -0.2),on_click=regresar, z=1) # Crea el botón para regresar        
        boton_reiniciar = Button(texture='../../resource/interfaz/reiniciar.png',color=color.white ,scale=(0.1, 0.1),position=(0.1, -0.2),on_click=reiniciar, z=1)# Ajusta la posición del botón
        
def regresar(): # Función para el botón regresar
    print("Regresando al menú...")
    # Codigo para regresar al menu principal
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, '..'))
    menu_path = os.path.join(project_dir,'index', 'inicio_juego.py')
    subprocess.Popen([sys.executable, menu_path])
    application.quit()

def reiniciar(): # Función para el botón reiniciar
    print("Reiniciando nivel...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, '..'))
    menu_path = os.path.join(project_dir,'index', 'nivel_1.py')
    subprocess.Popen([sys.executable, menu_path])
    application.quit()

def interaccion_nivel1(player): # Función que retorna la clase de CollectiblesManager
    return CollectiblesManager(player)