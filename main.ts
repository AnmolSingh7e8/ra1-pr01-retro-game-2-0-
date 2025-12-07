namespace SpriteKind {
    export const BalaEnemiga = SpriteKind.create()
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
sprites.onOverlap(SpriteKind.Player, SpriteKind.BalaEnemiga, function on_on_overlap2(jugador: Sprite, bala_mala: Sprite) {
    sprites.destroy(bala_mala)
    scene.cameraShake(4, 500)
    info.changeLifeBy(-10)
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

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    animation.runImageAnimation(personaje, assets.animation`
            animado_abajo
            `, 200, true)
})
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

controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(personaje, assets.animation`
            animado_der
            `, 200, true)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(personaje, assets.animation`
            animado_izq
            `, 200, true)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (en_bus) {
        personaje.setPosition(autobus.x, autobus.y)
        controller.moveSprite(personaje, 100, 100)
        scene.cameraFollowSprite(personaje)
        sprites.destroy(autobus, effects.trail, 500)
        en_bus = false
        spawnear_npcs()
    } else {
        disparar()
    }
    
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    Abrir_Cofre()
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

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    animation.runImageAnimation(personaje, assets.animation`
            animado_arriba
            `, 200, true)
})
function crear_autobus() {
    let x_inicio: number;
    let velocidad_x: number;
    
    en_bus = true
    autobus = sprites.create(assets.image`
        autobus
        `, SpriteKind.Player)
    if (randint(0, 1) == 0) {
        x_inicio = -40
        velocidad_x = 60
    } else {
        x_inicio = scene.screenHeight() * 16 + 40
        velocidad_x = -60
    }
    
    let y_inicio = randint(20, scene.screenWidth() * 16 - 20)
    autobus.setPosition(x_inicio, y_inicio)
    autobus.setVelocity(velocidad_x, 0)
    controller.moveSprite(personaje, 0, 0)
    scene.cameraFollowSprite(autobus)
}

let moviendo = false
let i = 0
let cofre_abierto = false
let der = false
let izq = false
let suelo = false
let techo = false
let fila = 0
let col = 0
let ubicacion : tiles.Location = null
let npcs_vivos = 0
let kills = 0
let personaje : Sprite = null
let municion_actual = 0
let ultima_direccion = ""
let img_enemigo3 : Image = null
let img_enemigo2 : Image = null
let img_enemigo1 : Image = null
let autobus : Sprite = null
let en_bus = true
img_enemigo1 = assets.image`
    enemigo1
    `
img_enemigo2 = assets.image`
    enemigo2
    `
img_enemigo3 = assets.image`
    enemigo3
    `
ultima_direccion = "derecha"
municion_actual = 150
let vida_jugador = 100
personaje = sprites.create(assets.image`
    personaje
    `, SpriteKind.Player)
controller.moveSprite(personaje, 100, 100)
tiles.setCurrentTilemap(tilemap`
    mapa
    `)
tiles.placeOnRandomTile(personaje, assets.tile`
    myTile6
    `)
info.setScore(0)
info.setLife(vida_jugador)
crear_autobus()
game.onUpdate(function on_on_update() {
    
    if (en_bus) {
        if (autobus.vx > 0 && autobus.x > scene.screenHeight() * 16 + 40 || autobus.vx < 0 && autobus.x < -40) {
            personaje.setPosition(autobus.x - 20, autobus.y)
            controller.moveSprite(personaje, 100, 100)
            scene.cameraFollowSprite(personaje)
            sprites.destroy(autobus)
            en_bus = false
            spawnear_npcs()
        }
        
    } else {
        moviendo = controller.down.isPressed() || (controller.left.isPressed() || (controller.up.isPressed() || controller.right.isPressed()))
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
    if (!en_bus) {
        for (let enemigo_actual of sprites.allOfKind(SpriteKind.Enemy)) {
            if (randint(0, 100) < 50) {
                vx = 0
                vy = 0
                if (enemigo_actual.image == img_enemigo1) {
                    img_bala = assets.image`
                        proyectil2
                        `
                    vy = 0
                    if (personaje.x > enemigo_actual.x) {
                        vx = 50
                    } else {
                        vx = -50
                    }
                    
                    bala = sprites.createProjectileFromSprite(img_bala, enemigo_actual, vx, vy)
                    bala.setKind(SpriteKind.BalaEnemiga)
                    bala.lifespan = 2000
                } else if (enemigo_actual.image == img_enemigo3) {
                    img_bala = assets.image`
                        proyectil1
                        `
                    vy = 0
                    if (personaje.x > enemigo_actual.x) {
                        vx = 90
                    } else {
                        vx = -90
                    }
                    
                    bala = sprites.createProjectileFromSprite(img_bala, enemigo_actual, vx, vy)
                    bala.setKind(SpriteKind.BalaEnemiga)
                    bala.lifespan = 800
                } else if (enemigo_actual.image == img_enemigo2) {
                    img_bala = assets.image`
                        proyectil3
                        `
                    bala = sprites.createProjectileFromSprite(img_bala, enemigo_actual, 0, 0)
                    bala.follow(personaje, 130)
                    bala.setKind(SpriteKind.BalaEnemiga)
                    bala.lifespan = 4000
                }
                
            }
            
        }
    }
    
})
