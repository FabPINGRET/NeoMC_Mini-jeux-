# Un pas de la traînée d'un tir (0,5 bloc) depuis l'arme jusqu'au point d'impact (marqueur mg.rend) ; $trp : 0 = quake, 1 = peinture rouge, 2 = peinture bleue
execute if score $trp mg.st matches 0 run particle minecraft:end_rod ~ ~ ~ 0 0 0 0 1
execute if score $trp mg.st matches 1 run particle minecraft:flame ~ ~ ~ 0 0 0 0 1
execute if score $trp mg.st matches 2 run particle minecraft:soul_fire_flame ~ ~ ~ 0 0 0 0 1
scoreboard players remove $trs mg.st 1
execute if score $trs mg.st matches 1.. unless entity @e[type=minecraft:marker,tag=mg.rend,distance=..0.5] positioned ^ ^ ^0.5 run function mg:core/shot_trail
