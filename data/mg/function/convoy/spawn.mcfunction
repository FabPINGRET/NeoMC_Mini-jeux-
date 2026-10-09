# @s : point d'apparition (près du convoi : escorte derrière, défense devant)
scoreboard players set $cva mg.st 0
execute if score $cvm mg.st matches 1 run scoreboard players set $cva mg.st 1
execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 0 if entity @s[team=mg_red] run scoreboard players set $cva mg.st 1
execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 1 if entity @s[team=mg_blue] run scoreboard players set $cva mg.st 1
execute if score $cva mg.st matches 1 if score $cvp mg.st matches 17.. at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] run tp @s ~-25 81 21200.5 facing ~ 81 21200.5
execute if score $cva mg.st matches 1 if score $cvp mg.st matches ..16 run tp @s -68 81 21200.5 facing 0 81 21200.5
execute if score $cva mg.st matches 0 if score $cvp mg.st matches ..87 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] run tp @s ~40 81 21200.5 facing ~ 81 21200.5
execute if score $cva mg.st matches 0 if score $cvp mg.st matches 88.. run tp @s 68 81 21200.5 facing -70 81 21200.5
execute at @s run spawnpoint @s ~ ~ ~
