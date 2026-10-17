# Chaque seconde (lobby/theme/npc_second ; @s = joueur lapin) : invisibilité rafraîchie, son lapin est gardé (tag mg.thbo retiré), recréé s'il a disparu
effect give @s minecraft:invisibility 3 0 true
scoreboard players operation $thbi mg.st = @s mg.thbn
execute as @e[type=minecraft:rabbit,tag=mg.thbun] if score @s mg.thbn = $thbi mg.st run tag @s remove mg.thbo
scoreboard players set $thbf mg.st 0
execute as @e[type=minecraft:rabbit,tag=mg.thbun] if score @s mg.thbn = $thbi mg.st run scoreboard players set $thbf mg.st 1
execute if score $thbf mg.st matches 0 run function mg:lobby/theme/stew_rabbit_body
