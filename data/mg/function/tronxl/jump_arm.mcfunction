# @s arme son saut : la moto peut sauter pendant 3 s
scoreboard players set @s mg.trj 400
execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run attribute @s minecraft:jump_strength base set 0.9
title @s actionbar {"text":"⤴ SAUT ARMÉ : maintiens Espace puis relâche !","color":"gold","bold":true}
execute at @s run playsound minecraft:entity.horse.jump master @s ~ ~ ~ 1 1.2
