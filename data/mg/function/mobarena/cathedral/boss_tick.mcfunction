# Le Comte de Sang
function mg:mobarena/hp_check
scoreboard players add $bc mg.st 1
execute at @e[tag=mg.boss] run particle minecraft:soul ~ ~1.5 ~ 0.5 1 0.5 0.02 3
# Phase 1 : toutes les 5 s, il se téléporte dans le dos d'un joueur (on réessaie jusqu'à trouver une place libre)
scoreboard players operation $m1 mg.st = $bc mg.st
scoreboard players operation $m1 mg.st %= $k100 mg.st
execute if score $m1 mg.st matches 0 run scoreboard players set $tpd mg.st 1
execute if score $tpd mg.st matches 1 as @r[tag=mg.play] at @s if block ^ ^ ^-2 #minecraft:air if block ^ ^1 ^-2 #minecraft:air run function mg:mobarena/cathedral/blink
# Phase 2 à 50 % des PV
execute if entity @e[tag=mg.boss,tag=!mg.ph2] if score $bh2 mg.st <= $bmax mg.st run function mg:mobarena/cathedral/phase2
execute if entity @e[tag=mg.boss,tag=mg.ph2] run function mg:mobarena/cathedral/ph2_tick
