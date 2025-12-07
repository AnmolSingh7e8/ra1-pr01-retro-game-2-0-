namespace SpriteKind {
    export const BalaEnemiga = SpriteKind.create()
    export const Autobus = SpriteKind.create()
    export const Cursor = SpriteKind.create()
    export const Boton = SpriteKind.create()
    export const NPC1 = SpriteKind.create()
    export const NPC2 = SpriteKind.create()
    export const NPC3 = SpriteKind.create()
    export const NPC4 = SpriteKind.create()
    export const NPC5 = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(proyectil2: Sprite, enemigo2: Sprite) {
    
    sprites.destroy(proyectil2)
    sprites.destroy(enemigo2, effects.fire, 200)
    kills += 1
    npcs_vivos += 0 - 1
    info.changeScoreBy(1)
    if (npcs_vivos == 0) {
        game.splash("VICTORY ROYALE!", "Kills: " + ("" + ("" + kills)))
        game.over(true)
    }
    
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    if (!juego_iniciado) {
        return
    }
    
    animation.runImageAnimation(personaje, assets.animation`
            animado_arriba
            `, 200, true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.BalaEnemiga, function on_on_overlap2(jugador: Sprite, bala_mala: Sprite) {
    sprites.destroy(bala_mala)
    scene.cameraShake(4, 500)
    info.changeLifeBy(-10)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    if (!juego_iniciado) {
        return
    }
    
    Abrir_Cofre()
})
function Abrir_Cofre() {
    
    ubicacion = personaje.tilemapLocation()
    col = ubicacion.column
    fila = ubicacion.row
    techo = personaje.tileKindAt(TileDirection.Top, assets.tile`
        cofre_abajo
        `) || personaje.tileKindAt(TileDirection.Top, assets.tile`
        myTile23
        `)
    suelo = personaje.tileKindAt(TileDirection.Bottom, assets.tile`
            cofre_abajo
            `) || personaje.tileKindAt(TileDirection.Bottom, assets.tile`
        myTile23
        `)
    izq = personaje.tileKindAt(TileDirection.Left, assets.tile`
        cofre_abajo
        `) || personaje.tileKindAt(TileDirection.Left, assets.tile`
        myTile23
        `)
    der = personaje.tileKindAt(TileDirection.Right, assets.tile`
            cofre_abajo
            `) || personaje.tileKindAt(TileDirection.Right, assets.tile`
        myTile23
        `)
    if (ultima_direccion == "arriba" && techo) {
        tiles.setTileAt(tiles.getTileLocation(col, fila - 1), assets.tile`
                cofre_arriba
                `)
        cofre_abierto = true
    } else if (ultima_direccion == "abajo" && suelo) {
        tiles.setTileAt(tiles.getTileLocation(col, fila + 1), assets.tile`
                cofre_arriba
                `)
        cofre_abierto = true
    } else if (ultima_direccion == "izquierda" && izq) {
        tiles.setTileAt(tiles.getTileLocation(col - 1, fila), assets.tile`
                cofre_arriba
                `)
        cofre_abierto = true
    } else if (ultima_direccion == "derecha" && der) {
        tiles.setTileAt(tiles.getTileLocation(col + 1, fila), assets.tile`
                cofre_arriba
                `)
        cofre_abierto = true
    }
    
    if (cofre_abierto) {
        municion_actual += 30
        game.splash("Cofre abierto!", "+30 municion")
        cofre_abierto = false
    } else {
        game.splash("No hay cofre")
    }
    
}

function disparar() {
    let proyectil: Sprite;
    
    if (municion_actual > 0) {
        municion_actual += -1
        proyectil = sprites.createProjectileFromSprite(assets.image`
            proyectil1
            `, personaje, 0, 0)
        if (ultima_direccion == "arriba") {
            proyectil.setVelocity(0, -150)
        } else if (ultima_direccion == "abajo") {
            proyectil.setVelocity(0, 150)
        } else if (ultima_direccion == "izquierda") {
            proyectil.setVelocity(-150, 0)
        } else if (ultima_direccion == "derecha") {
            proyectil.setVelocity(150, 0)
        }
        
        proyectil.setFlag(SpriteFlag.AutoDestroy, true)
        proyectil.lifespan = 2000
    }
    
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    //  Logica del menu inicial
    if (!juego_iniciado) {
        if (cursor.overlapsWith(boton_jugar)) {
            iniciar_partida()
        }
        
        return
    }
    
    //  Logica normal del juego
    if (en_bus) {
        personaje.setPosition(autobus2.x, autobus2.y)
        controller.moveSprite(personaje, 100, 100)
        scene.cameraFollowSprite(personaje)
        sprites.destroy(autobus2, effects.trail, 500)
        en_bus = false
        spawnear_npcs()
    } else {
        disparar()
    }
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    if (!juego_iniciado) {
        return
    }
    
    animation.runImageAnimation(personaje, assets.animation`
            animado_izq
            `, 200, true)
})
function spawnear_npcs() {
    let enemigo: Sprite;
    
    let lista_npcs : Sprite[] = []
    while (i < 5) {
        enemigo = sprites.create(img_enemigo1, SpriteKind.Enemy)
        tiles.placeOnRandomTile(enemigo, assets.tile`
            myTile6
            `)
        enemigo.follow(personaje, 40)
        lista_npcs.push(enemigo)
        i += 1
    }
    i = 0
    while (i < 5) {
        enemigo = sprites.create(img_enemigo2, SpriteKind.Enemy)
        tiles.placeOnRandomTile(enemigo, assets.tile`
            myTile6
            `)
        lista_npcs.push(enemigo)
        i += 1
    }
    i = 0
    while (i < 5) {
        enemigo = sprites.create(img_enemigo3, SpriteKind.Enemy)
        tiles.placeOnRandomTile(enemigo, assets.tile`
            myTile6
            `)
        enemigo.setVelocity(50, 0)
        enemigo.setBounceOnWall(true)
        lista_npcs.push(enemigo)
        i += 1
    }
    npcs_vivos = lista_npcs.length
}

function iniciar_partida() {
    
    sprites.destroy(cursor)
    sprites.destroy(boton_jugar)
    municion_actual = 150
    vida_jugador = 100
    personaje = sprites.create(assets.image`
        personaje
        `, SpriteKind.Player)
    //  Importante: activar movimiento del personaje aqui
    controller.moveSprite(personaje, 100, 100)
    tiles.setCurrentTilemap(tilemap`
        mapa
        `)
    tiles.placeOnRandomTile(personaje, assets.tile`
        myTile6
        `)
    info.setScore(0)
    info.setLife(vida_jugador)
    juego_iniciado = true
    crear_autobus()
    crear_npcs_especiales()
}

controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    if (!juego_iniciado) {
        return
    }
    
    animation.runImageAnimation(personaje, assets.animation`
            animado_der
            `, 200, true)
})
//  --- FUNCIONES DE MENU ---
function mostrar_menu() {
    
    //  Asignar la imagen de fondo
    scene.setBackgroundImage(assets.image`
        pantalla_inicial
        `)
    //  Crear cursor
    cursor = sprites.create(image.create(5, 5), SpriteKind.Cursor)
    cursor.image.fill(1)
    cursor.setFlag(SpriteFlag.StayInScreen, true)
    controller.moveSprite(cursor, 150, 150)
    imagen_hitbox = image.create(60, 25)
    imagen_hitbox.fill(3)
    boton_jugar = sprites.create(imagen_hitbox, SpriteKind.Boton)
    boton_jugar.setPosition(130, 95)
    boton_jugar.setFlag(SpriteFlag.Invisible, true)
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    if (!juego_iniciado) {
        return
    }
    
    animation.runImageAnimation(personaje, assets.animation`
            animado_abajo
            `, 200, true)
})
function crear_autobus() {
    let x_inicio: number;
    let velocidad_x: number;
    
    en_bus = true
    //  Crear el autobús con su propio SpriteKind
    autobus2 = sprites.create(assets.image`
        autobus
        `, SpriteKind.Autobus)
    //  Ignorar todos los tiles y física de jugador
    autobus2.setFlag(SpriteFlag.Ghost, true)
    autobus2.setFlag(SpriteFlag.StayInScreen, false)
    autobus2.setVelocity(65, 0)
    //  velocidad inicial
    //  Posición inicial
    if (randint(0, 1) == 0) {
        x_inicio = -40
        velocidad_x = 65
    } else {
        x_inicio = 114 * 16 + 40
        velocidad_x = -65
    }
    
    //  Altura segura en el mapa
    y_inicio = randint(20, 114 * 16 - 20)
    autobus2.setPosition(x_inicio, y_inicio)
    autobus2.setVelocity(velocidad_x, 0)
    //  La cámara sigue al autobús
    scene.cameraFollowSprite(autobus2)
}

function crear_npcs_especiales() {
    //  ZONA 1 – CURANDERO
    let npc1 = sprites.create(assets.image`npc_healer`, SpriteKind.NPC1)
    tiles.placeOnTile(npc1, tiles.getTileLocation(5, 10))
    //  ZONA 2 – VELOCIDAD
    let npc2 = sprites.create(assets.image`npc_runner`, SpriteKind.NPC2)
    tiles.placeOnTile(npc2, tiles.getTileLocation(20, 8))
    //  ZONA 3 – MUNICIÓN
    let npc3 = sprites.create(assets.image`npc_ammo`, SpriteKind.NPC3)
    tiles.placeOnTile(npc3, tiles.getTileLocation(15, 20))
    //  ZONA 4 – ESCUDO
    let npc4 = sprites.create(assets.image`npc_shield`, SpriteKind.NPC4)
    tiles.placeOnTile(npc4, tiles.getTileLocation(25, 25))
    //  ZONA 5 – DOBLE DISPARO
    let npc5 = sprites.create(assets.image`npc_fire`, SpriteKind.NPC5)
    tiles.placeOnTile(npc5, tiles.getTileLocation(35, 10))
}

function habilidad_curacion() {
    info.changeLifeBy(+20)
    game.splash("NPC Curandero", "+20 vida")
}

function habilidad_velocidad() {
    personaje.vx *= 1.5
    personaje.vy *= 1.5
    game.splash("NPC Corredor", "Velocidad +50")
}

function habilidad_municion() {
    
    municion_actual += 50
    game.splash("NPC Munición", "+50 balas")
}

function habilidad_escudo() {
    
    tiene_escudo = true
    game.splash("NPC Escudo", "¡Resistes 1 golpe sin daño!")
}

function habilidad_fire_rate() {
    
    fire_rate_boost = true
    game.splash("NPC Maestro del disparo", "¡Disparo doble por 10s!")
    pause(10000)
    fire_rate_boost = false
}

function activar_npc(sprite: Sprite, npc: Sprite) {
    let tipo = npc.kind()
    if (tipo == SpriteKind.NPC1) {
        habilidad_curacion()
    } else if (tipo == SpriteKind.NPC2) {
        habilidad_velocidad()
    } else if (tipo == SpriteKind.NPC3) {
        habilidad_municion()
    } else if (tipo == SpriteKind.NPC4) {
        habilidad_escudo()
    } else if (tipo == SpriteKind.NPC5) {
        habilidad_fire_rate()
    }
    
    npc.destroy(effects.smiles, 300)
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC1, activar_npc)
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC2, activar_npc)
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC3, activar_npc)
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC4, activar_npc)
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC5, activar_npc)
sprites.onOverlap(SpriteKind.Player, SpriteKind.BalaEnemiga, function on_player_hit_with_shield(jugador: Sprite, bala: Sprite) {
    
    if (tiene_escudo) {
        tiene_escudo = false
        sprites.destroy(bala)
        game.splash("Escudo", "¡Daño bloqueado!")
    } else {
        sprites.destroy(bala)
        info.changeLifeBy(-10)
    }
    
})
let moviendo = false
let y_inicio = 0
let imagen_hitbox : Image = null
let vida_jugador = 0
let i = 0
let autobus2 : Sprite = null
let boton_jugar : Sprite = null
let cursor : Sprite = null
let municion_actual = 0
let cofre_abierto = false
let der = false
let izq = false
let suelo = false
let techo = false
let fila = 0
let col = 0
let ubicacion : tiles.Location = null
let juego_iniciado = false
let npcs_vivos = 0
let kills = 0
let ultima_direccion = ""
let img_enemigo3 : Image = null
let img_enemigo2 : Image = null
let img_enemigo1 : Image = null
let en_bus = false
let personaje : Sprite = null
let MAP_SIZE = 0
en_bus = true
let tiene_escudo = false
let fire_rate_boost = false
//  Cargar assets
img_enemigo1 = assets.image`
    enemigo1
    `
img_enemigo2 = assets.image`
    enemigo2
    `
img_enemigo3 = assets.image`
    enemigo3
    `
let npc_healer = assets.image`npc_healer`
let npc_runner = assets.image`npc_runner`
let npc_ammo = assets.image`npc_ammo`
let npc_shield = assets.image`npc_shield`
let npc_fire = assets.image`npc_fire`
ultima_direccion = "derecha"
mostrar_menu()
game.onUpdate(function on_on_update() {
    
    if (!juego_iniciado) {
        return
    }
    
    //  No actualizar bus en menu
    if (en_bus) {
        //  Mantener jugador sobre el autobús
        personaje.setPosition(autobus2.x, autobus2.y)
        //  Detectar si el autobús salió del mapa
        if (autobus2.x > 114 * 16 + 40 || autobus2.x < -40) {
            sprites.destroy(autobus2)
            en_bus = false
            spawnear_npcs()
        }
        
    }
    
})
game.onUpdate(function on_on_update2() {
    let MAP_SIZE2: number;
    
    if (!juego_iniciado) {
        return
    }
    
    if (en_bus) {
        MAP_SIZE2 = 114 * 16
        //  tamaño real del mapa en píxeles
        //  Cuando el bus sale del mapa
        if (autobus2.vx > 0 && autobus2.x > MAP_SIZE2 + 40 || autobus2.vx < 0 && autobus2.x < -40) {
            personaje.setPosition(autobus2.x - 20, autobus2.y)
            controller.moveSprite(personaje, 100, 100)
            scene.cameraFollowSprite(personaje)
            sprites.destroy(autobus2, effects.trail, 500)
            en_bus = false
            spawnear_npcs()
        }
        
    } else {
        moviendo = controller.down.isPressed() || controller.left.isPressed() || controller.up.isPressed() || controller.right.isPressed()
        if (controller.up.isPressed()) {
            ultima_direccion = "arriba"
        } else if (controller.down.isPressed()) {
            ultima_direccion = "abajo"
        } else if (controller.left.isPressed()) {
            ultima_direccion = "izquierda"
        } else if (controller.right.isPressed()) {
            ultima_direccion = "derecha"
        }
        
        if (!moviendo) {
            animation.stopAnimation(animation.AnimationTypes.All, personaje)
        }
        
    }
    
})
game.onUpdateInterval(1000, function on_update_interval() {
    let vx: number;
    let vy: number;
    let img_bala: Image;
    let bala: Sprite;
    if (!juego_iniciado) {
        return
    }
    
    if (!en_bus) {
        for (let enemigo_actual of sprites.allOfKind(SpriteKind.Enemy)) {
            //  Ignorar si el enemigo no existe o no tiene imagen
            if (enemigo_actual == null || enemigo_actual.image == null) {
                continue
            }
            
            //  Probabilidad de disparar
            if (randint(0, 100) < 50) {
                vx = 0
                vy = 0
                if (enemigo_actual.image == img_enemigo1) {
                    img_bala = assets.image`
                        proyectil2
                        `
                    vx = personaje.x > enemigo_actual.x ? 50 : -50
                    vy = 0
                } else if (enemigo_actual.image == img_enemigo3) {
                    img_bala = assets.image`
                        proyectil1
                        `
                    vx = personaje.x > enemigo_actual.x ? 90 : -90
                    vy = 0
                } else if (enemigo_actual.image == img_enemigo2) {
                    img_bala = assets.image`
                        proyectil3
                        `
                    vx = 0
                    vy = 0
                }
                
                //  Crear proyectil solo si img_bala está definida
                if (img_bala != null) {
                    bala = sprites.createProjectileFromSprite(img_bala, enemigo_actual, vx, vy)
                    bala.setKind(SpriteKind.BalaEnemiga)
                    if (enemigo_actual.image == img_enemigo1) {
                        bala.lifespan = 2000
                    } else if (enemigo_actual.image == img_enemigo3) {
                        bala.lifespan = 800
                    } else if (enemigo_actual.image == img_enemigo2) {
                        bala.follow(personaje, 130)
                        bala.lifespan = 4000
                    }
                    
                }
                
            }
            
        }
    }
    
})
