# Région Forêt de Sylvanor : 10 monstres + 4 par joueur présent (22 au plus)
execute store result score $n mg.st if entity @e[tag=mg.olm,tag=mg.olr_nw]
execute store result score $cap mg.st if entity @a[tag=mg.olw,scores={mg.olrg=2}]
scoreboard players operation $cap mg.st *= #4 mg.st
scoreboard players add $cap mg.st 10
execute if score $cap mg.st matches 23.. run scoreboard players set $cap mg.st 22
execute if score $n mg.st >= $cap mg.st run return 0
tag @e[tag=mg.olok] remove mg.olok
execute as @e[type=minecraft:marker,tag=mg.olsp_nw] at @s if entity @a[tag=mg.olw,distance=22..70] unless entity @a[tag=mg.olw,distance=..18] run tag @s add mg.olok
execute as @e[tag=mg.olok,sort=random,limit=1] at @s run function mg:ombre/m/grp_nw
tag @e[tag=mg.olok] remove mg.olok
