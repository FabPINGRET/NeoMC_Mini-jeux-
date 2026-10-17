# Admin (@s) : coupe / rétablit l'assise et les emotes du lobby ($sitoff mg.st = 1 : coupé, absent : actif)
execute store success score #sitw mg.st if score $sitoff mg.st matches 1
execute if score #sitw mg.st matches 1 run scoreboard players reset $sitoff mg.st
execute if score #sitw mg.st matches 1 run return run tellraw @s {"text":"🪑 Assis et emotes du lobby : activés.","color":"green"}
scoreboard players set $sitoff mg.st 1
execute as @a[tag=mg.sit] run function mg:lobby/sit/stand
tellraw @s {"text":"🪑 Assis et emotes du lobby : désactivés.","color":"red"}
