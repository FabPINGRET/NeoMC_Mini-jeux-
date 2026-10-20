# Tir du sniper (@s = joueur qui a fait un clic droit) : rayon de 150 blocs, recharge 2 s
scoreboard players reset @s mg.qs
execute unless items entity @s weapon.* *[custom_data~{mg_tm:1b}] run return 0
execute if entity @s[tag=mg.tmp] run return 0
execute if score @s mg.tmcd matches 1.. run return 0
scoreboard players set @s mg.tmcd 40
tag @s add mg.tmsh
# le rayon ne vise que l'équipe adverse : il traverse les coéquipiers (pas de tir ami)
execute if entity @s[team=mg_red] run tag @a[tag=mg.play,gamemode=adventure,team=mg_blue] add mg.tmen
execute if entity @s[team=mg_blue] run tag @a[tag=mg.play,gamemode=adventure,team=mg_red] add mg.tmen
scoreboard players set $rs mg.st 300
execute at @s run playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 1 1.8
# marqueur de fin de rayon : mg.tmend (propre au TDM) + mg.rend (le repère de core/shot_trail)
execute at @s anchored eyes run summon minecraft:marker ^ ^ ^0.5 {Tags:["mg.tmend","mg.rend"]}
execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:tdm/ray
# traînée : part de l'arme et rejoint le point d'impact
scoreboard players set $trp mg.st 0
scoreboard players set $trs mg.st 320
execute at @s anchored eyes positioned ^-0.3 ^-0.2 ^0.7 facing entity @e[type=minecraft:marker,tag=mg.tmend,limit=1] feet run function mg:core/shot_trail
kill @e[type=minecraft:marker,tag=mg.tmend]
# frag APRÈS la traînée (la réapparition déplacerait la victime)
execute as @a[tag=mg.tmvc,scores={mg.tmhp=..0}] run function mg:tdm/frag
tag @a remove mg.tmvc
tag @a remove mg.tmen
tag @s remove mg.tmsh
