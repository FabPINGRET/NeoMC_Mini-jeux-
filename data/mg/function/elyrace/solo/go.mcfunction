# @s = joueur : GO ! SEULE ENTRÉE en course (phase 2, chrono à 0). Même départ que core/begin puis elyrace/go, pour lui seul
effect clear @s minecraft:slowness
effect clear @s minecraft:resistance
function mg:core/unfreeze
effect give @s minecraft:instant_health 1 10 true
effect give @s minecraft:saturation 1 9 true
title @s title [{"text":"GO !","color":"green","bold":true}]
execute at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.7 1.4
effect give @s minecraft:resistance infinite 4 true
effect give @s minecraft:saturation infinite 0 true
# portillon de son parcours (ouvert pour tous les solos du parcours : ils sont gelés tant que le décompte dure)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/gate_off
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/gate_off
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/go_text
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/go_text
# gravité de course de son parcours (comme go pour le groupe) ; solo/stop la remet à la normale
function mg:elyrace/grav_on
scoreboard players set @s mg.xst 0
scoreboard players set @s mg.xph 2
