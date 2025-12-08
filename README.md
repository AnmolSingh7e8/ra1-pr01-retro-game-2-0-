# Battle Royale Adventure

## Descripción
**Battle Royale Adventure** es un juego desarrollado en **MakeCode Arcade** que combina:
- Movimiento de personaje con animaciones.
- Disparos en varias direcciones.
- Cofres interactivos que dan munición.
- NPCs con habilidades especiales (curación, velocidad, escudo, doble disparo, munición extra).
- Enemigos con IA y barras de vida.
- Inicio cinemático sobre un autobús.

El objetivo del juego es derrotar a todos los enemigos y conseguir el **VICTORY ROYALE**.

---

## Controles

| Acción                  | Botón                  |
|-------------------------|-----------------------|
| Moverse                 | Flechas / Joystick    |
| Disparar                | A                     |
| Abrir cofre             | B                     |
| Seleccionar opción menu | A                     |
| Mover cursor del menú   | Flechas               |

---

## Funciones principales

### iniciar_partida()
- Configura el juego: crea al personaje, HUD, tilemap, música y enemigos especiales.
- Activa el autobús inicial y prepara el juego para empezar.

### crear_autobus()
- Genera el autobús en movimiento al inicio del juego.
- Mantiene al jugador sobre él hasta que sale del mapa.
- La cámara sigue al autobús.

### spawnear_npcs()
- Crea los enemigos del mapa y les asigna barras de vida.
- Enemigos diferentes con comportamientos distintos:
  - Enemigos que siguen al jugador.
  - Enemigos que disparan proyectiles.
  - Enemigos que rebotan por el mapa.

### disparar()
- Crea un proyectil según la última dirección del personaje.
- Resta munición y destruye el proyectil tras un tiempo.
- Base de la mecánica ofensiva del jugador.

### Abrir_Cofre()
- Detecta la dirección del jugador y si hay un cofre cerca.
- Si se abre, otorga +10 munición.

### activar_npc(sprite, npc)
- Detecta el tipo de NPC con el que colisiona el jugador.
- Activa la habilidad correspondiente:
  - Curación
  - Velocidad
  - Munición
  - Escudo
  - Disparo doble temporal
- Destruye al NPC tras activarlo.

### on_on_zero(status)
- Gestiona cuando un enemigo muere.
- Incrementa el puntaje.
- Comprueba si quedan enemigos; si no, muestra **Victory Royale**.

---

## Capturas del juego

### Pantalla principal
<img width="892" height="666" alt="Captura de pantalla 2025-12-08 185244" src="https://github.com/user-attachments/assets/7874e0d6-410c-4938-80b5-bd3477ff4d6d" />

### Personaje principal
<img width="671" height="668" alt="Captura de pantalla 2025-12-08 184635" src="https://github.com/user-attachments/assets/62414e86-bf8a-4131-bbd2-b2df1cdb8aaa" />


### Enemigos
- Enemigo 1

<img width="575" height="539" alt="Captura de pantalla 2025-12-08 184737" src="https://github.com/user-attachments/assets/1dd76e76-e395-4bb5-8f06-fecd18052d31" />

- Enemigo 2

<img width="575" height="605" alt="Captura de pantalla 2025-12-08 184827" src="https://github.com/user-attachments/assets/01968ed1-5c9c-4467-9b30-3c9a3209ac5c" />

- Enemigo 3

<img width="565" height="557" alt="Captura de pantalla 2025-12-08 185115" src="https://github.com/user-attachments/assets/9040df0e-3396-45d9-8af0-2159a6511765" />

- NPC Curandero

<img width="550" height="530" alt="Captura de pantalla 2025-12-08 184712" src="https://github.com/user-attachments/assets/b2c0c447-556b-4463-afbf-bbd22d8b3e73" />

- NPC Corredor

<img width="480" height="579" alt="Captura de pantalla 2025-12-08 184804" src="https://github.com/user-attachments/assets/c5329e3b-67a7-4357-80c1-b102bfdffaf0" />

- NPC Munición

<img width="507" height="520" alt="Captura de pantalla 2025-12-08 184702" src="https://github.com/user-attachments/assets/a8b7cb0c-5d0e-4c64-83c5-eb4d3228c6cd" />

- NPC Escudo

<img width="557" height="552" alt="Captura de pantalla 2025-12-08 184755" src="https://github.com/user-attachments/assets/ed1c369d-8234-4ef5-a4d9-127283027eac" />

- NPC Disparo Doble

<img width="539" height="544" alt="Captura de pantalla 2025-12-08 184652" src="https://github.com/user-attachments/assets/2f140dcc-5886-4200-882b-93319b437050" />

### Cofres
- Cofre Cerrado

<img width="669" height="672" alt="Captura de pantalla 2025-12-08 184905" src="https://github.com/user-attachments/assets/82bf17af-e254-4b4e-84e0-d075dcebaee3" />

- Cofre Abierto

<img width="670" height="665" alt="Captura de pantalla 2025-12-08 184916" src="https://github.com/user-attachments/assets/fd19771c-8d05-4fb8-9219-4504b4350220" />

### Autobús

<img width="657" height="600" alt="Captura de pantalla 2025-12-08 185233" src="https://github.com/user-attachments/assets/090a835e-8c44-4b9c-b024-277787ee4792" />


### Mapa del juego

<img width="733" height="729" alt="mapa" src="https://github.com/user-attachments/assets/331f1c85-85b9-4b49-827f-caa4f4d74e3b" />


---

## Objetivo del juego
Sobrevive, administra munición, abre cofres, activa habilidades de NPCs y derrota a todos los enemigos para ganar.

---

### Demo del juego

https://github.com/user-attachments/assets/0e0e9211-7d02-4599-96c7-a89bcf2dab75

 

