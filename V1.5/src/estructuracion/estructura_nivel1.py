from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
import math, time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.jugador.jugador import Player, update_player

def parte_1 ():    
    # texturas para el laberinto
    p0_s = load_texture('../../resource/objetos/comienzo.png')
    p0_f = load_texture('../../resource/objetos/final.png')
    p1 = load_texture('../../resource/objetos/p1_arriba.png')
    p2_a_d = load_texture('../../resource/objetos/p2_abajo_derecha.png')
    p2_a_i= load_texture('../../resource/objetos/p2_abajo_izquierda.png')
    p2_b_d = load_texture('../../resource/objetos/p2_arriba_derecha.png')
    p2_b_i = load_texture('../../resource/objetos/p2_arriba_izquierda.png')
    p3_b = load_texture('../../resource/objetos/p3_abajo.png')
    p3_a = load_texture('../../resource/objetos/p3_arriba.png')
    p4 = load_texture('../../resource/objetos/p4_izquierda.png')
    p5 = load_texture('../../resource/objetos/p5_derecha.png')
    p6 = load_texture('../../resource/objetos/p6_centro.png')
    
    #linea de limitación visual
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.17, 0.90, 0.3), position=(29.6, 3.41, -1))
    #square = Entity(model='quad', texture = p6, color=color.white, scale=(2, 15, 0.2), position=(31.2, 0), collider='box') 
    
    # limites de la pantalla
    platform_abajo = Entity(model='quad', color=color.clear, position=(-2.1,-4), scale=(15, .5, 1), collider='box')
    platform_abajo = Entity(model='quad', color=color.clear, position=(7.5,-4), scale=(5, .5, 1), collider='box')
    border_left = Entity( model='quad', color=color.clear, position=(-7.5,-5.1), scale=(.5, 100, 1), y=-4, collider='box')
    border_right = Entity(model='quad',  color=color.clear, position=(30.5,-5.1), scale=(.5, 100, 1), y=-4, collider='box')
    
    # Estructura del laberinto
    # COMIENZO
    square = Entity(model='quad', texture = p0_s, color=color.white, scale=(1, 1), position=(-5.50, -3.40))

    
    # BLOQUE 1.
    #MEDIO
    square = Entity(model='quad', texture = p3_b, color=color.white, scale=(1.50, 0.90, 0.2), position=(0, -3.40), collider='box')
    
    #DERECHA
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(5.05, -3.20), collider='box')
    
    
    #BLOQUE 2.
    #IZQUIERDA
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.50, 0.60, 0.2), position=(-4, -2.40), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.50, 0.60, 0.2), position=(-2.50, -2.40), collider='box')
    qsuare = Entity(model='quad', texture = p6, color=color.white, scale=(1.50, 0.60, 0.2), position=(-5.50, -2.40), collider='box')
    qsuare = Entity(model='quad', texture = p3_b, color=color.white, scale=(1.70, 0.80, 0.2), position=(-5.50, -1.70), collider='box')
    square = Entity(model='quad', texture = p2_a_i, color=color.white, scale=(1, 1), position=(-6.70, -2.20), collider='box')
    
    #DERECHA
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.50, 0.60, 0.2), position=(2.50, -2.40), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.50, 0.60, 0.2), position=(4, -2.40), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(0.6, 0.6), position=(5.05, -2.40), collider='box')
    
    
    #BLOQUE 3.
    #IZQUIERDA
    square = Entity(model='quad', texture = p2_b_i, color=color.white, scale=(1, 1), position=(-2, -0.10), collider='box')
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.60, 0.60, 0.2), position=(-2.69, -0.80), collider='box')
    
    #MEDIO
    square = Entity(model='quad', texture = p6, color=color.white, scale=(0.80, 0.60, 0.2), position=(-1.11, 0.10), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(0.80, 0.60, 0.2), position=(1.11, 0.10), collider='box')
    square = Entity(model='quad', texture = p3_a, color=color.white, scale=(1.50, 1, 0.2), position=(0, 0.3), collider='box')
    
    #DERECHA
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.60, 0.60, 0.2), position=(2.69, -0.80), collider='box')
    square = Entity(model='quad', texture = p2_b_d, color=color.white, scale=(1, 1), position=(2, -0.10), collider='box')
    
    
    # BLOQUE 4.
    #SUB-BLOQUE IZQUIERDO
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(-6.05, 0.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(-6.05, 1.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(-6.05, 2), collider='box')
    square = Entity(model='quad', texture = p2_a_i, color=color.white, scale=(1, 1), position=(-5.37, 1.32), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(1.50, 0.59, 0.2), position=(-4.12, 1.14), collider='box')

    #SUB-BLOQUE MEDIO
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.80, 0.59, 0.2), position=(-1.08, 2), collider='box')    
    square = Entity(model='quad', texture = p3_b, color=color.white, scale=(1.50, 0.90, 0.2), position=(0, 2.50), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(1.40, 0.40, 0.2), position=(1.40, 2.70), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.25, 0.58, 0.2), position=(2.70, 2.70), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.30, 0.2), position=(0, 1.44), collider='box')
    
    #SUB-BLOQUE DERECHO
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(5.05, -1.70), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(5.05, -0.70), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(5.05, 0.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(5.05, 1.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(5.05, 2.30), collider='box')
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1, 0.60, 0.2), position=(4.33 , 0.80), collider='box')
    
    #SUB-BLOQUE FINAL
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(7, -1.60), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(7, -0.60), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(7, 0.40), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(7, 1.40), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(7, 2.40), collider='box')
    #square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(7, 2.60), collider='box')
    square = Entity(model='quad', texture = p2_b_i, color=color.white, scale=(1, 1), position=(7.20, 3.40), collider='box')

def parte_2():
    # texturas para el laberinto
    p0_s = load_texture('../../resource/objetos/comienzo.png')
    p0_f = load_texture('../../resource/objetos/final.png')
    p1 = load_texture('../../resource/objetos/p1_arriba.png')
    p2_a_d = load_texture('../../resource/objetos/p2_abajo_derecha.png')
    p2_a_i= load_texture('../../resource/objetos/p2_abajo_izquierda.png')    
    p2_b_d = load_texture('../../resource/objetos/p2_arriba_derecha.png')
    p2_b_i = load_texture('../../resource/objetos/p2_arriba_izquierda.png')
    p3_b = load_texture('../../resource/objetos/p3_abajo.png')
    p3_a = load_texture('../../resource/objetos/p3_arriba.png')
    p4 = load_texture('../../resource/objetos/p4_izquierda.png')
    p5 = load_texture('../../resource/objetos/p5_derecha.png')
    p6 = load_texture('../../resource/objetos/p6_centro.png')
    p7 = load_texture('../../resource/objetos/p8_plataforma.png')
    
    class PlataformaMovil(Entity):
        def __init__(self, inicio_pos, fin_pos, velocidad=2):
            super().__init__()
            self.model = 'quad'
            self.texture = p7
            self.color = color.white
            self.scale = (1, 0.3)
            self.position = inicio_pos
            self.inicio_pos = inicio_pos
            self.fin_pos = fin_pos
            self.velocidad = velocidad
            self.collider = 'box'

        def update(self):
            pos_anterior = self.position
            factor = (math.sin(time.time() * self.velocidad) + 1) / 2
            self.position = lerp(self.inicio_pos, self.fin_pos, factor)
            delta = self.position - pos_anterior

            for entity in scene.entities:
                if isinstance(entity, PlatformerController2d):
                    if entity.intersects(self).hit and entity.y > self.y + (self.scale_y / 2) - 0.1:
                        entity.y += delta.y
                        entity.x += delta.x
    
    #Plataformas movibles
    crear_plataformas = [
        #BLOQUE IZQUIERDO
        PlataformaMovil(inicio_pos=Vec3( 8.5, 2.80, 0), fin_pos=Vec3( 8.5, -2, 0), velocidad=0.7),
        
        
        #BLOQUE MEDIO BAJO
        PlataformaMovil(inicio_pos=Vec3(16, -3.15, 0), fin_pos=Vec3(11, -3.15, 0), velocidad=0.5),
        PlataformaMovil(inicio_pos=Vec3(18.5, -3, 0), fin_pos=Vec3( 18.5, 2.5, 0), velocidad=0.5),
        PlataformaMovil(inicio_pos=Vec3(21, -3.15, 0), fin_pos=Vec3(28, -3.15, 0), velocidad=0.5),
        
        #BLOQUE DERECHO
        PlataformaMovil(inicio_pos=Vec3(29.4, 0.2, 0), fin_pos=Vec3(29.4, -3.15, 0), velocidad=0.5),
        PlataformaMovil(inicio_pos=Vec3(24.1, 2.90, 0), fin_pos=Vec3(24.1, 0.80, 0), velocidad=1),
        ]
    
    #BLOQUE IZQUIERDO
    #izquierda
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.50, 0.2), position=(9.85, 1.99), collider='box')
    square = Entity(model='quad', texture = p2_a_i, color=color.white, scale=(0.80, 0.80), position=(9.99, 0.90), collider='box')
    
    #medio
    square = Entity(model='quad', texture = p2_b_i, color=color.white, scale=(0.80, 0.80), position=(16.1, 0), collider='box')
    square = Entity(model='quad', texture = p2_a_d, color=color.white, scale=(0.80, 0.80), position=(15.8, -0.67), collider='box')
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.05, 0.50, 0.2), position=(14.9, -0.80), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(3.05, 0.50, 0.2), position=(12.9, -0.80), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.05, 0.50, 0.2), position=(10.9, -0.79), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(1.05, 0.50, 0.2), position=(9.6, -1.60), collider='box')
    
    square = Entity(model='quad', texture = p6, color=color.white, scale=(3.05, 0.50, 0.2), position=(12.9, 0.80), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.05, 0.50, 0.2), position=(10.9, 0.79), collider='box')
    
    square = Entity(model='quad', texture = p6, color=color.white, scale=(3.05, 0.50, 0.2), position=(14.5, 2.54), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.05, 0.50, 0.2), position=(12.5, 2.55), collider='box')
    
    #derecha
    square = Entity(model='quad', texture = p2_b_d, color=color.white, scale=(1,1), position=(16.5, 2.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(16.7, 0.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(16.7, 1.30), collider='box')
    
    
    # BLOQUE MEDIO BAJO
    #derecha
    
    #medio
    square = Entity(model='quad', texture = p3_b, color=color.white, scale=(1.58, 0.90, 0.2), position=(17.8, -3.44), collider='box')
    square = Entity(model='quad', texture = p3_b, color=color.white, scale=(1.58, 0.90, 0.2), position=(19.3, -3.44), collider='box')
    
    #izquierda
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 2, 0.2), position=(10, -4), collider='box')
    
    #BLOQUE DERECHO:
    #izquierda
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(20.3, 0.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.05, 0.2), position=(20.3, 1.30), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.25, 0.2), position=(20.3, 2.45), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.25, 0.2), position=(20.3, 3.65), collider='box')
    square = Entity(model='quad', texture = p1, color=color.white, scale=(0.60, 1.25, 0.2), position=(20.3, 4.85), collider='box')
    
    #medio
    square = Entity(model='quad', texture = p2_b_d, color=color.white, scale=(0.80, 0.80), position=(20.9, 0), collider='box')
    square = Entity(model='quad', texture = p2_a_i, color=color.white, scale=(0.80, 0.80), position=(21.2, -0.67), collider='box')
    square = Entity(model='quad', texture = p5, color=color.white, scale=(1.05, 0.50, 0.2), position=(22.1, -0.80), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(2.55, 0.50, 0.2), position=(23.9, -0.80), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(2.55, 0.50, 0.2), position=(26.4, -0.80), collider='box')
    square = Entity(model='quad', texture = p4, color=color.white, scale=(1.05, 0.50, 0.2), position=(28.1, -0.79), collider='box')
    
    square = Entity(model='quad', texture = p6, color=color.white, scale=(2.55, 0.50, 0.2), position=(23.9, 0.80), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(2.55, 0.50, 0.2), position=(26.4, 0.80), collider='box')
    
    square = Entity(model='quad', texture = p6, color=color.white, scale=(2.65, 0.50, 0.2), position=(26.3, 2.80), collider='box')
    square = Entity(model='quad', texture = p6, color=color.white, scale=(2.65, 0.50, 0.2), position=(28.9, 2.80), collider='box')

    

   
