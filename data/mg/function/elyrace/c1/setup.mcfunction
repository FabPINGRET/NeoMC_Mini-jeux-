# Installation du départ du parcours 1 (Canyon du Couchant) : zone chargée, portillon fermé, perchoir des spectateurs, point d'apparition
function mg:elyrace/c1/fl_add
function mg:elyrace/c1/gate_on
# perchoir des spectateurs (éliminés / reconnectés)
scoreboard players set $px mg.st 24
scoreboard players set $py mg.st 270
scoreboard players set $pz mg.st 27000
execute as @a[tag=mg.play] run spawnpoint @s 24 251 27000
