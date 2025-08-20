from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

def Player(x):
    player = PlatformerController2d(
        position=(-7, -3.50),
        gravity=1, 
        color=color.clear,
        scale=(0.8, 0.8, 0.01),
        max_jumps = 1,
        jump_height=1, 
        jump_duration=0.5, 
        walk_speed=x
    )

    # Add player animation
    anim = Animator({
        'idle': Animation('../../resource/personaje/idle/idle', parent=player, autoplay=True, fps=3, scale=(0.8, 0.8, 0.01), position=(0, 0.38), model='cube', Collider="box"),
        'walking': Animation('../../resource/personaje/walking/walking', parent=player, autoplay=True, scale=(0.8, 0.8, 0.01), position=(0, 0.38), model='cube', Collider="box"),
        'jump': Animation('../../resource/personaje/jump/jump', parent=player, autoplay=False, scale=(0.8, 0.8, 0.01), position=(0, 0.38), model='cube', Collider="box")
    })

    return player, anim

def update_player(key, player, anim):
    if held_keys['a'] or held_keys['d']:
        anim.state = 'walking'
    else:
        anim.state = 'idle'
    if key == 'space':
        anim.state = 'jump'
        
