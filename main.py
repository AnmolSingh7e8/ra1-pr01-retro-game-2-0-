@namespace
class SpriteKind:
    BalaEnemiga = SpriteKind.create()

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

def on_on_overlap2(jugador, bala_mala):
    sprites.destroy(bala_mala)
    scene.camera_shake(4, 500)
    info.change_life_by(-10)
sprites.on_overlap(SpriteKind.player, SpriteKind.BalaEnemiga, on_on_overlap2)

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

def on_down_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_abajo
            """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

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

def on_right_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_der
            """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_izq
            """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_a_pressed():
    global en_bus
    if en_bus:
        personaje.set_position(autobus.x, autobus.y)
        controller.move_sprite(personaje, 100, 100)
        scene.camera_follow_sprite(personaje)
        sprites.destroy(autobus, effects.trail, 500)
        en_bus = False
        spawnear_npcs()
    else:
        disparar()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    Abrir_Cofre()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

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

def on_up_pressed():
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_arriba
            """),
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def crear_autobus():
    global autobus, en_bus
    en_bus = True
    autobus = sprites.create(assets.image("""
        autobus
        """), SpriteKind.player)
    if randint(0, 1) == 0:
        x_inicio = -40
        velocidad_x = 60
    else:
        x_inicio = scene.screen_height() * 16 + 40
        velocidad_x = -60
    y_inicio = randint(20, scene.screen_width() * 16 - 20)
    autobus.set_position(x_inicio, y_inicio)
    autobus.set_velocity(velocidad_x, 0)
    controller.move_sprite(personaje, 0, 0)
    scene.camera_follow_sprite(autobus)

moviendo = False
i = 0
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
personaje: Sprite = None
municion_actual = 0
ultima_direccion = ""
img_enemigo3: Image = None
img_enemigo2: Image = None
img_enemigo1: Image = None
autobus: Sprite = None
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
    global moviendo, ultima_direccion, en_bus
    if en_bus:
        if (autobus.vx > 0 and autobus.x > scene.screen_height() * 16 + 40) or (autobus.vx < 0 and autobus.x < -40):
            personaje.set_position(autobus.x - 20, autobus.y)
            controller.move_sprite(personaje, 100, 100)
            scene.camera_follow_sprite(personaje)
            sprites.destroy(autobus)
            en_bus = False
            spawnear_npcs()
    else:
        moviendo = controller.down.is_pressed() or (controller.left.is_pressed() or (controller.up.is_pressed() or controller.right.is_pressed()))
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
    if not en_bus:
        for enemigo_actual in sprites.all_of_kind(SpriteKind.enemy):
            if randint(0, 100) < 50:
                vx = 0
                vy = 0
                if enemigo_actual.image == img_enemigo1:
                    img_bala = assets.image("""
                        proyectil2
                        """)
                    vy = 0
                    if personaje.x > enemigo_actual.x:
                        vx = 50
                    else:
                        vx = -50
                    bala = sprites.create_projectile_from_sprite(img_bala, enemigo_actual, vx, vy)
                    bala.set_kind(SpriteKind.BalaEnemiga)
                    bala.lifespan = 2000
                elif enemigo_actual.image == img_enemigo3:
                    img_bala = assets.image("""
                        proyectil1
                        """)
                    vy = 0
                    if personaje.x > enemigo_actual.x:
                        vx = 90
                    else:
                        vx = -90
                    bala = sprites.create_projectile_from_sprite(img_bala, enemigo_actual, vx, vy)
                    bala.set_kind(SpriteKind.BalaEnemiga)
                    bala.lifespan = 800
                elif enemigo_actual.image == img_enemigo2:
                    img_bala = assets.image("""
                        proyectil3
                        """)
                    bala = sprites.create_projectile_from_sprite(img_bala, enemigo_actual, 0, 0)
                    bala.follow(personaje, 130)
                    bala.set_kind(SpriteKind.BalaEnemiga)
                    bala.lifespan = 4000
game.on_update_interval(1000, on_update_interval)