# Range le kart de @s (et sa caméra, sa tête) sans le déplacer
function mg:kart/kk
ride @s dismount
execute as @e[type=minecraft:block_display,tag=mg.kk] on passengers unless entity @s[type=minecraft:player] run kill @s
kill @e[tag=mg.kk]
kill @e[tag=mg.kcamc]
execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s
tag @s remove mg.lk
tag @s remove mg.kfin
tag @s remove mg.kout
scoreboard players set @s mg.ri 0
execute if entity @s[gamemode=spectator] run gamemode adventure @s
