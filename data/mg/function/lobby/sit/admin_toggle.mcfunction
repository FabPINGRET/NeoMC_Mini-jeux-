# Admin (@s) : coupe / rétablit l'assise, les emotes, l'objet 🎉 et les zones des bancs du lobby ($sitoff mg.st = 1 : coupé, absent : actif)
execute store success score #sitw mg.st if score $sitoff mg.st matches 1
execute if score #sitw mg.st matches 1 run scoreboard players reset $sitoff mg.st
# $lbx absent : sit/bench_check repose les zones des bancs au prochain passage (toutes les 2 s)
execute if score #sitw mg.st matches 1 run scoreboard players reset $lbx mg.st
execute if score #sitw mg.st matches 1 run return run tellraw @s {"text":"🪑 Assis et emotes du lobby : activés.","color":"green"}
scoreboard players set $sitoff mg.st 1
execute as @a[tag=mg.sit] run function mg:lobby/sit/stand
kill @e[type=minecraft:interaction,tag=mg.bench]
clear @a *[minecraft:custom_data~{mg_emote:1b}]
tellraw @s {"text":"🪑 Assis et emotes du lobby : désactivés.","color":"red"}
