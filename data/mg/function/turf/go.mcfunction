# Turf Wars — début de partie
scoreboard players set $tl mg.st 7200
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.play] run function mg:turf/kit
scoreboard objectives setdisplay sidebar mg.ts
scoreboard players set Rouge mg.ts 15
scoreboard players set Bleu mg.ts 15
tellraw @a[tag=mg.play] [{"text":"▮ TURF WARS ! ","color":"gold","bold":true},{"text":"Tire à l'arc : chaque flèche qui se plante dans une colonne ennemie la convertit à la couleur de ton équipe. Conquiers 28 colonnes sur 31 (90 %) ou en avoir le plus après 6 min pour gagner !","color":"gray"}]
function mg:turf/show
