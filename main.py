@namespace
class SpriteKind:
    BalaEnemiga = SpriteKind.create()
    Autobus = SpriteKind.create()

def on_on_overlap(proyectil2, enemigo2):
    global kills, npcs_vivos
    sprites.destroy(proyectil2)
    sprites.destroy(enemigo2, effects.fire, 200)
    kills += 1
    npcs_vivos += 0 - 1
    info.change_score_by(1)
    if npcs_vivos == 0:
        game.splash("VICTORY ROYALE!", "Kills: " + ("" + str(kills)))
        game.over(True)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_up_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_arriba
            """),
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap2(jugador, bala_mala):
    sprites.destroy(bala_mala)
    scene.camera_shake(4, 500)
    info.change_life_by(-10)
sprites.on_overlap(SpriteKind.player, SpriteKind.BalaEnemiga, on_on_overlap2)

def on_b_pressed():
    Abrir_Cofre()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def Abrir_Cofre():
    global ubicacion, col, fila, techo, suelo, izq, der, cofre_abierto, municion_actual
    ubicacion = personaje.tilemap_location()
    col = ubicacion.column
    fila = ubicacion.row
    techo = personaje.tile_kind_at(TileDirection.TOP, assets.tile("""
        cofre_abajo
        """)) or personaje.tile_kind_at(TileDirection.TOP, assets.tile("""
        myTile23
        """))
    suelo = personaje.tile_kind_at(TileDirection.BOTTOM,
        assets.tile("""
            cofre_abajo
            """)) or personaje.tile_kind_at(TileDirection.BOTTOM, assets.tile("""
        myTile23
        """))
    izq = personaje.tile_kind_at(TileDirection.LEFT, assets.tile("""
        cofre_abajo
        """)) or personaje.tile_kind_at(TileDirection.LEFT, assets.tile("""
        myTile23
        """))
    der = personaje.tile_kind_at(TileDirection.RIGHT,
        assets.tile("""
            cofre_abajo
            """)) or personaje.tile_kind_at(TileDirection.RIGHT, assets.tile("""
        myTile23
        """))
    if ultima_direccion == "arriba" and techo:
        tiles.set_tile_at(tiles.get_tile_location(col, fila - 1),
            assets.tile("""
                cofre_arriba
                """))
        cofre_abierto = True
    elif ultima_direccion == "abajo" and suelo:
        tiles.set_tile_at(tiles.get_tile_location(col, fila + 1),
            assets.tile("""
                cofre_arriba
                """))
        cofre_abierto = True
    elif ultima_direccion == "izquierda" and izq:
        tiles.set_tile_at(tiles.get_tile_location(col - 1, fila),
            assets.tile("""
                cofre_arriba
                """))
        cofre_abierto = True
    elif ultima_direccion == "derecha" and der:
        tiles.set_tile_at(tiles.get_tile_location(col + 1, fila),
            assets.tile("""
                cofre_arriba
                """))
        cofre_abierto = True
    if cofre_abierto:
        municion_actual += 30
        game.splash("Cofre abierto!", "+30 municion")
        cofre_abierto = False
    else:
        game.splash("No hay cofre")
def disparar():
    global municion_actual
    if municion_actual > 0:
        municion_actual += -1
        proyectil = sprites.create_projectile_from_sprite(assets.image("""
            proyectil1
            """), personaje, 0, 0)
        if ultima_direccion == "arriba":
            proyectil.set_velocity(0, -150)
        elif ultima_direccion == "abajo":
            proyectil.set_velocity(0, 150)
        elif ultima_direccion == "izquierda":
            proyectil.set_velocity(-150, 0)
        elif ultima_direccion == "derecha":
            proyectil.set_velocity(150, 0)
        proyectil.set_flag(SpriteFlag.AUTO_DESTROY, True)
        proyectil.lifespan = 2000

def on_a_pressed():
    global en_bus
    if en_bus:
        personaje.set_position(autobus2.x, autobus2.y)
        controller.move_sprite(personaje, 100, 100)
        scene.camera_follow_sprite(personaje)
        sprites.destroy(autobus2, effects.trail, 500)
        en_bus = False
        spawnear_npcs()
    else:
        disparar()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_izq
            """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def spawnear_npcs():
    global i, npcs_vivos
    lista_npcs: List[Sprite] = []
    while i < 5:
        enemigo = sprites.create(img_enemigo1, SpriteKind.enemy)
        tiles.place_on_random_tile(enemigo, assets.tile("""
            myTile6
            """))
        enemigo.follow(personaje, 40)
        lista_npcs.append(enemigo)
        i += 1
    i = 0
    while i < 5:
        enemigo = sprites.create(img_enemigo2, SpriteKind.enemy)
        tiles.place_on_random_tile(enemigo, assets.tile("""
            myTile6
            """))
        lista_npcs.append(enemigo)
        i += 1
    i = 0
    while i < 5:
        enemigo = sprites.create(img_enemigo3, SpriteKind.enemy)
        tiles.place_on_random_tile(enemigo, assets.tile("""
            myTile6
            """))
        enemigo.set_velocity(50, 0)
        enemigo.set_bounce_on_wall(True)
        lista_npcs.append(enemigo)
        i += 1
    npcs_vivos = len(lista_npcs)

def on_right_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_der
            """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_abajo
            """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def crear_autobus():
    global autobus2, en_bus
    en_bus = True

    # Crear el autobús con su propio SpriteKind
    autobus2 = sprites.create(assets.image("autobus"), SpriteKind.Autobus)

    # Ignorar todos los tiles y física de jugador
    autobus2.set_flag(SpriteFlag.GHOST, True)
    autobus2.set_flag(SpriteFlag.STAY_IN_SCREEN, False)
    autobus2.set_velocity(65, 0)  # velocidad inicial

    # Posición inicial
    if randint(0, 1) == 0:
        x_inicio = -40
        velocidad_x = 65
    else:
        x_inicio = 114*16 + 40
        velocidad_x = -65

    # Altura segura en el mapa
    y_inicio = randint(20, 114*16 - 20)

    autobus2.set_position(x_inicio, y_inicio)
    autobus2.set_velocity(velocidad_x, 0)

    # La cámara sigue al autobús
    scene.camera_follow_sprite(autobus2)

def on_update_autobus():
    global en_bus
    if en_bus:
        # Mantener jugador sobre el autobús
        personaje.set_position(autobus2.x, autobus2.y)
        
        # Detectar si el autobús salió del mapa
        if autobus2.x > 114*16 + 40 or autobus2.x < -40:
            sprites.destroy(autobus2)
            en_bus = False
            spawnear_npcs()

game.on_update(on_update_autobus)            

moviendo = False
i = 0
autobus2: Sprite = None
cofre_abierto = False
der = False
izq = False
suelo = False
techo = False
fila = 0
col = 0
ubicacion: tiles.Location = None
npcs_vivos = 0
kills = 0
municion_actual = 0
ultima_direccion = ""
img_enemigo3: Image = None
img_enemigo2: Image = None
img_enemigo1: Image = None
en_bus = False
personaje: Sprite = None
MAP_SIZE = 0
en_bus = True
img_enemigo1 = assets.image("""
    enemigo1
    """)
img_enemigo2 = assets.image("""
    enemigo2
    """)
img_enemigo3 = assets.image("""
    enemigo3
    """)
ultima_direccion = "derecha"
municion_actual = 150
vida_jugador = 100
personaje = sprites.create(assets.image("""
    personaje
    """), SpriteKind.player)
controller.move_sprite(personaje, 100, 100)
tiles.set_current_tilemap(tilemap("""
    mapa
    """))
tiles.place_on_random_tile(personaje, assets.tile("""
    myTile6
    """))
info.set_score(0)
info.set_life(vida_jugador)
crear_autobus()

def on_on_update():
    global en_bus, moviendo, ultima_direccion
    if en_bus:
        MAP_SIZE2 = 114 * 16
        # tamaño real del mapa en píxeles
        # Cuando el bus sale del mapa
        if autobus2.vx > 0 and autobus2.x > MAP_SIZE2 + 40 or autobus2.vx < 0 and autobus2.x < -40:
            personaje.set_position(autobus2.x - 20, autobus2.y)
            controller.move_sprite(personaje, 100, 100)
            scene.camera_follow_sprite(personaje)
            sprites.destroy(autobus2, effects.trail, 500)
            en_bus = False
            spawnear_npcs()
    else:
        moviendo = controller.down.is_pressed() or controller.left.is_pressed() or controller.up.is_pressed() or controller.right.is_pressed()
        if controller.up.is_pressed():
            ultima_direccion = "arriba"
        elif controller.down.is_pressed():
            ultima_direccion = "abajo"
        elif controller.left.is_pressed():
            ultima_direccion = "izquierda"
        elif controller.right.is_pressed():
            ultima_direccion = "derecha"
        if not (moviendo):
            animation.stop_animation(animation.AnimationTypes.ALL, personaje)
game.on_update(on_on_update)

def on_update_interval():
    if not (en_bus):
        for enemigo_actual in sprites.all_of_kind(SpriteKind.enemy):
            # Ignorar si el enemigo no existe o no tiene imagen
            if enemigo_actual == None or enemigo_actual.image == None:
                continue
            # Probabilidad de disparar
            if randint(0, 100) < 50:
                vx = 0
                vy = 0
                if enemigo_actual.image == img_enemigo1:
                    img_bala = assets.image("""
                        proyectil2
                        """)
                    vx = 50 if personaje.x > enemigo_actual.x else -50
                    vy = 0
                elif enemigo_actual.image == img_enemigo3:
                    img_bala = assets.image("""
                        proyectil1
                        """)
                    vx = 90 if personaje.x > enemigo_actual.x else -90
                    vy = 0
                elif enemigo_actual.image == img_enemigo2:
                    img_bala = assets.image("""
                        proyectil3
                        """)
                    vx = 0
                    vy = 0
                # Crear proyectil solo si img_bala está definida
                if img_bala != None:
                    bala = sprites.create_projectile_from_sprite(img_bala, enemigo_actual, vx, vy)
                    bala.set_kind(SpriteKind.BalaEnemiga)
                    if enemigo_actual.image == img_enemigo1:
                        bala.lifespan = 2000
                    elif enemigo_actual.image == img_enemigo3:
                        bala.lifespan = 800
                    elif enemigo_actual.image == img_enemigo2:
                        bala.follow(personaje, 130)
                        bala.lifespan = 4000
game.on_update_interval(1000, on_update_interval)
