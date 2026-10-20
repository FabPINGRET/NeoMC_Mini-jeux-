# Tir du sniper (@s = duelliste qui a fait un clic gauche, gun/cl_left) : rayon de 150 blocs, recharge 2 s
scoreboard players reset @s mg.qs
# le sniper en main droite seulement (le couteau porte aussi mg_dl ; un clic droit vanilla avec lui ne doit pas tirer)
execute unless items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run return 0
execute if entity @s[tag=mg.dlp] run return 0
execute if score @s mg.dlcd matches 1.. run return 0
scoreboard players set @s mg.dlcd 40
tag @s add mg.dlsh
# le rayon ne touche que l'adversaire de la même arène (mg.dli)
scoreboard players operation $dli mg.st = @s mg.dli
scoreboard players set $rs mg.st 300
execute at @s run playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 1 1.8
# marqueur de fin de rayon : mg.dlend (propre au duel) + mg.rend (le repère de core/shot_trail)
execute at @s anchored eyes run summon minecraft:marker ^ ^ ^0.5 {Tags:["mg.dlend","mg.rend"]}
execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:duel/ray
# traînée : part de l'arme et rejoint le point d'impact
scoreboard players set $trp mg.st 0
scoreboard players set $trs mg.st 320
execute at @s anchored eyes positioned ^-0.3 ^-0.2 ^0.7 facing entity @e[type=minecraft:marker,tag=mg.dlend,limit=1] feet run function mg:core/shot_trail
kill @e[type=minecraft:marker,tag=mg.dlend]
# fin de manche APRÈS la traînée (le retour au départ déplacerait le tireur)
execute as @a[tag=mg.dlvc,scores={mg.dlhp=..0}] run function mg:duel/round
tag @a remove mg.dlvc
tag @s remove mg.dlsh
