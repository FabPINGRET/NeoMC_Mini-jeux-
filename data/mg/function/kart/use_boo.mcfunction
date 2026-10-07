# Boo : vole l'objet d'un adversaire au hasard et rend intouchable 4 s
scoreboard players set @s mg.kboo 80
tag @s add mg.kme
execute as @a[tag=mg.play,tag=!mg.kme,scores={mg.kit=1..},sort=random,limit=1] run tag @s add mg.kvic
tag @s remove mg.kme
execute if entity @a[tag=mg.kvic] run scoreboard players operation @s mg.kit = @a[tag=mg.kvic,limit=1] mg.kit
execute if entity @a[tag=mg.kvic] run function mg:kart/item_give
execute if entity @a[tag=mg.kvic] run tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" vole l'objet de ","color":"gray"},{"selector":"@a[tag=mg.kvic]","color":"yellow"},{"text":" 👻","color":"white"}]
execute as @a[tag=mg.kvic] run function mg:kart/robbed
tag @a remove mg.kvic
title @s actionbar [{"text":"👻 Intouchable !","color":"white","bold":true}]
execute at @s run playsound minecraft:entity.vex.ambient master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 0.6
