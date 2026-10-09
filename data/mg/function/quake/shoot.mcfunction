# Tir de railgun (@s = joueur qui a fait un clic droit)
scoreboard players reset @s mg.qs
execute if score @s mg.cd matches 1.. run return 0
scoreboard players operation @s mg.cd = $qcd mg.st
tag @s add mg.qsh
scoreboard players set $rs mg.st 140
# cartes sniper : portée 120 blocs
execute if score $ar mg.st matches 0 if score $qm mg.st matches 8..9 run scoreboard players set $rs mg.st 240
execute at @s anchored eyes run summon minecraft:marker ^ ^ ^0.5 {Tags:["mg.rend"]}
execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:quake/ray
# Traînée : part de l'arme (comme le laser du lobby) et rejoint le point d'impact du rayon (qui part des yeux)
scoreboard players set $trp mg.st 0
scoreboard players set $trs mg.st 260
execute at @s anchored eyes positioned ^-0.3 ^-0.2 ^0.7 facing entity @e[type=minecraft:marker,tag=mg.rend,limit=1] feet run function mg:core/shot_trail
kill @e[type=minecraft:marker,tag=mg.rend]
tag @s remove mg.qsh
execute at @s run playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 1 1.8
