@namespace
class SpriteKind:
    BalaEnemiga = SpriteKind.create()
    Autobus = SpriteKind.create()
    Cursor = SpriteKind.create()
    Boton = SpriteKind.create()
    NPC1 = SpriteKind.create()
    NPC2 = SpriteKind.create()
    NPC3 = SpriteKind.create()
    NPC4 = SpriteKind.create()
    NPC5 = SpriteKind.create()

def on_on_overlap(proyectil2, enemigo2):
    global barra_enemigo
    sprites.destroy(proyectil2)
    barra_enemigo = statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, enemigo2)
    if barra_enemigo:
        barra_enemigo.value += -20
        enemigo2.start_effect(effects.ashes, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def habilidad_escudo():
    global tiene_escudo
    tiene_escudo = True
    game.splash("NPC Escudo", "¡Resistes 1 golpe sin daño!")

def on_on_overlap2(jugador, bala_mala):
    global daño_recibido, tiene_escudo
    # Comparar imagenes para saber el daño
    if bala_mala.image == assets.image("""
        disparo1
        """):
        daño_recibido = 30
    elif bala_mala.image == assets.image("""
        disparo2
        """):
        daño_recibido = 40
    elif bala_mala.image == assets.image("""
        disparo3
        """):
        daño_recibido = 20
    else:
        daño_recibido = 10
    sprites.destroy(bala_mala)
    scene.camera_shake(4, 500)
    if tiene_escudo:
        personaje.start_effect(effects.fountain, 500)
        tiene_escudo = False
        game.splash("¡Escudo roto!", "No recibes daño")
    else:
        info.change_life_by(daño_recibido * -1)
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
def crear_npcs_especiales():
    global npc1, npc2, npc3, npc4, npc5
    # ZONA 1 – CURANDERO
    npc1 = sprites.create(assets.image("""
        npc_healer
        """), SpriteKind.NPC1)
    tiles.place_on_tile(npc1, tiles.get_tile_location(29, 35))
    # ZONA 2 – VELOCIDAD
    npc2 = sprites.create(assets.image("""
        npc_runner
        """), SpriteKind.NPC2)
    tiles.place_on_tile(npc2, tiles.get_tile_location(84, 92))
    # ZONA 3 – MUNICIÓN
    npc3 = sprites.create(assets.image("""
        npc_ammo
        """), SpriteKind.NPC3)
    tiles.place_on_tile(npc3, tiles.get_tile_location(65, 21))
    # ZONA 4 – ESCUDO
    npc4 = sprites.create(assets.image("""
        npc_shield
        """), SpriteKind.NPC4)
    tiles.place_on_tile(npc4, tiles.get_tile_location(99, 10))
    # ZONA 5 – DOBLE DISPARO
    npc5 = sprites.create(assets.image("""
        npc_fire
        """), SpriteKind.NPC5)
    tiles.place_on_tile(npc5, tiles.get_tile_location(46, 102))

def on_down_pressed():
    if not (juego_iniciado):
        return
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_abajo
            """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def habilidad_velocidad():
    controller.move_sprite(personaje, 150, 150)
    game.splash("NPC Corredor", "Velocidad aumentada!")
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
    if not (juego_iniciado):
        return
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_der
            """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def habilidad_curacion():
    info.change_life_by(20)
    game.splash("NPC Curandero", "+20 vida")

def on_left_pressed():
    if not (juego_iniciado):
        return
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_izq
            """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_a_pressed():
    global en_bus
    # Logica del menu inicial
    if not (juego_iniciado):
        if cursor.overlaps_with(boton_jugar):
            iniciar_partida()
        return
    # Logica normal del juego
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

def on_b_pressed():
    if not (juego_iniciado):
        return
    Abrir_Cofre()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def habilidad_fire_rate():
    global fire_rate_boost
    fire_rate_boost = True
    game.splash("NPC Maestro del disparo", "¡Disparo doble por 10s!")
    pause(10000)
    fire_rate_boost = False
def activar_npc(sprite: Sprite, npc: Sprite):
    global tipo
    tipo = npc.kind()
    if tipo == SpriteKind.NPC1:
        habilidad_curacion()
    elif tipo == SpriteKind.NPC2:
        habilidad_velocidad()
    elif tipo == SpriteKind.NPC3:
        habilidad_municion()
    elif tipo == SpriteKind.NPC4:
        habilidad_escudo()
    elif tipo == SpriteKind.NPC5:
        habilidad_fire_rate()
    npc.destroy(effects.smiles, 300)

def on_on_zero(status):
    global enemigo_muerto, kills, npcs_vivos
    enemigo_muerto = status.sprite_attached_to()
    sprites.destroy(enemigo_muerto, effects.fire, 500)
    kills += 1
    npcs_vivos += 0 - 1
    info.change_score_by(1)
    if npcs_vivos == 0:
        game.splash("VICTORY ROYALE!", "Kills: " + ("" + str(kills)))
        game.over(True)
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def spawnear_npcs():
    global i, npcs_vivos
    lista_npcs: List[Sprite] = []
    # Creación de enemigos con diferente vida según que haga cada uno
    while i < 5:
        enemigo = sprites.create(img_enemigo1, SpriteKind.enemy)
        tiles.place_on_random_tile(enemigo, assets.tile("""
            myTile6
            """))
        enemigo.follow(personaje, 40)
        barra = statusbars.create(20, 4, StatusBarKind.enemy_health)
        barra.attach_to_sprite(enemigo)
        barra.max = 100
        barra.value = 100
        barra.set_color(7, 2)
        lista_npcs.append(enemigo)
        i += 1
    i = 0
    while i < 5:
        enemigo = sprites.create(img_enemigo2, SpriteKind.enemy)
        tiles.place_on_random_tile(enemigo, assets.tile("""
            myTile6
            """))
        barra = statusbars.create(20, 4, StatusBarKind.enemy_health)
        barra.attach_to_sprite(enemigo)
        barra.max = 40
        barra.value = 40
        barra.set_color(7, 2)
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
        barra = statusbars.create(20, 4, StatusBarKind.enemy_health)
        barra.attach_to_sprite(enemigo)
        barra.max = 60
        barra.value = 60
        barra.set_color(7, 2)
        lista_npcs.append(enemigo)
        i += 1
    npcs_vivos = len(lista_npcs)
def iniciar_partida():
    global municion_actual, vida_jugador, personaje, juego_iniciado
    music.stop_all_sounds()
    music.play(music.string_playable("C5 A B G A F G E ", 160),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    sprites.destroy(cursor)
    sprites.destroy(boton_jugar)
    municion_actual = 150
    vida_jugador = 100
    personaje = sprites.create(assets.image("""
        personaje
        """), SpriteKind.player)
    # Importante: activar movimiento del personaje aqui
    controller.move_sprite(personaje, 100, 100)
    tiles.set_current_tilemap(tilemap("""
        mapa
        """))
    tiles.place_on_random_tile(personaje, assets.tile("""
        myTile6
        """))
    info.set_score(0)
    info.set_life(vida_jugador)
    juego_iniciado = True
    crear_autobus()
    crear_npcs_especiales()
# --- FUNCIONES DE MENU ---
def mostrar_menu():
    global cursor, imagen_hitbox, boton_jugar
    music.stop_all_sounds()
    music.set_volume(100)
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    scene.set_background_image(assets.image("""
        pantalla_inicial
        """))
    cursor = sprites.create(image.create(5, 5), SpriteKind.Cursor)
    cursor.image.fill(1)
    cursor.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    controller.move_sprite(cursor, 150, 150)
    imagen_hitbox = image.create(60, 25)
    imagen_hitbox.fill(3)
    boton_jugar = sprites.create(imagen_hitbox, SpriteKind.Boton)
    boton_jugar.set_position(130, 95)
    boton_jugar.set_flag(SpriteFlag.INVISIBLE, True)

def on_up_pressed():
    if not (juego_iniciado):
        return
    animation.run_image_animation(personaje,
        assets.animation("""
            animado_arriba
            """),
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def crear_autobus():
    global en_bus, autobus2, y_inicio
    en_bus = True
    # Crear el autobús con su propio SpriteKind
    autobus2 = sprites.create(assets.image("""
        autobus
        """), SpriteKind.Autobus)
    # Ignorar todos los tiles y física de jugador
    autobus2.set_flag(SpriteFlag.GHOST, True)
    autobus2.set_flag(SpriteFlag.STAY_IN_SCREEN, False)
    autobus2.set_velocity(65, 0)
    # velocidad inicial
    # Posición inicial
    if randint(0, 1) == 0:
        x_inicio = -40
        velocidad_x = 65
    else:
        x_inicio = 114 * 16 + 40
        velocidad_x = -65
    # Altura segura en el mapa
    y_inicio = randint(20, 114 * 16 - 20)
    autobus2.set_position(x_inicio, y_inicio)
    autobus2.set_velocity(velocidad_x, 0)
    # La cámara sigue al autobús
    scene.camera_follow_sprite(autobus2)
def habilidad_municion():
    global municion_actual
    municion_actual += 50
    game.splash("NPC Munición", "+50 balas")
moviendo = False
y_inicio = 0
imagen_hitbox: Image = None
vida_jugador = 0
i = 0
npcs_vivos = 0
kills = 0
enemigo_muerto: Sprite = None
tipo = 0
fire_rate_boost = False
autobus2: Sprite = None
boton_jugar: Sprite = None
cursor: Sprite = None
juego_iniciado = False
npc5: Sprite = None
npc4: Sprite = None
npc3: Sprite = None
npc2: Sprite = None
npc1: Sprite = None
municion_actual = 0
cofre_abierto = False
der = False
izq = False
suelo = False
techo = False
fila = 0
col = 0
ubicacion: tiles.Location = None
personaje: Sprite = None
daño_recibido = 0
tiene_escudo = False
barra_enemigo: StatusBarSprite = None
ultima_direccion = ""
img_enemigo3: Image = None
img_enemigo2: Image = None
img_enemigo1: Image = None
en_bus = False
MAP_SIZE = 0
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC1, activar_npc)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC2, activar_npc)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC3, activar_npc)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC4, activar_npc)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC5, activar_npc)
en_bus = True
# Cargar assets
img_enemigo1 = assets.image("""
    enemigo1
    """)
img_enemigo2 = assets.image("""
    enemigo2
    """)
img_enemigo3 = assets.image("""
    enemigo3
    """)
npc_healer = assets.image("""
    npc_healer
    """)
npc_runner = assets.image("""
    npc_runner
    """)
npc_ammo = assets.image("""
    npc_ammo
    """)
npc_shield = assets.image("""
    npc_shield
    """)
npc_fire = assets.image("""
    npc_fire
    """)
ultima_direccion = "derecha"
mostrar_menu()

def on_on_update():
    global en_bus
    if not (juego_iniciado):
        return
    # No actualizar bus en menu
    if en_bus:
        # Mantener jugador sobre el autobús
        personaje.set_position(autobus2.x, autobus2.y)
        # Detectar si el autobús salió del mapa
        if autobus2.x > 114 * 16 + 40 or autobus2.x < -40:
            sprites.destroy(autobus2)
            en_bus = False
            spawnear_npcs()
game.on_update(on_on_update)

def on_on_update2():
    global en_bus, moviendo, ultima_direccion
    if not (juego_iniciado):
        return
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
game.on_update(on_on_update2)

def on_update_interval():
    if not (juego_iniciado) or en_bus:
        return
    for enemigo_actual in sprites.all_of_kind(SpriteKind.enemy):
        if enemigo_actual == None or enemigo_actual.image == None:
            continue
        # Probabilidad de disparo
        if randint(0, 100) < 50:
            img_bala = None
            velocidad_bala = 0
            vida_bala = 0
            # Enemigos con escopeta, fusil y francotirador
            if enemigo_actual.image == img_enemigo1:
                img_bala = assets.image("""
                    disparo1
                    """)
                velocidad_bala = 60
                vida_bala = 600
            elif enemigo_actual.image == img_enemigo2:
                img_bala = assets.image("""
                    disparo2
                    """)
                velocidad_bala = 180
                vida_bala = 3000
            elif enemigo_actual.image == img_enemigo3:
                img_bala = assets.image("""
                    disparo3
                    """)
                velocidad_bala = 100
                vida_bala = 1500
            # Disparo con punteria calculando la posición del Jugador
            if img_bala != None:
                bala = sprites.create_projectile_from_sprite(img_bala, enemigo_actual, 0, 0)
                bala.set_kind(SpriteKind.BalaEnemiga)
                dx = personaje.x - enemigo_actual.x
                dy = personaje.y - enemigo_actual.y
                angulo = Math.atan2(dy, dx)
                vx = Math.cos(angulo) * velocidad_bala
                vy = Math.sin(angulo) * velocidad_bala
                bala.set_velocity(vx, vy)
                bala.lifespan = vida_bala
game.on_update_interval(1000, on_update_interval)
