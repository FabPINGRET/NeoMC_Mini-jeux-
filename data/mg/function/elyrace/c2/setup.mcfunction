# Installation du départ du parcours 2 (Pic Blanc) : zone chargée, portillon fermé, perchoir des spectateurs, point d'apparition
function mg:elyrace/c2/fl_add
function mg:elyrace/c2/gate_on
# perchoir des spectateurs (éliminés / reconnectés)
scoreboard players set $px mg.st 24
scoreboard players set $py mg.st 301
scoreboard players set $pz mg.st 29600
execute as @a[tag=mg.play] run spawnpoint @s 24 282 29600
