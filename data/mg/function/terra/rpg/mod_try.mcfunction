# Tous les 5 ticks, @s (accroupi, étape 32 ou 64) : ramassage d'un module / de la cellule (2 s)
scoreboard players set $k mg.st 0
execute if score @s mg.trch matches 32 as @e[type=minecraft:marker,tag=mg.trmod,distance=..2.2] run scoreboard players operation $k mg.st = @s mg.trnid
execute if score @s mg.trch matches 64 if entity @e[type=minecraft:marker,tag=mg.trcell,distance=..2.5] run scoreboard players set $k mg.st 9
execute if score $k mg.st matches 0 run return run scoreboard players set @s mg.trpk 0
execute if score $k mg.st matches 1 run scoreboard players set $kb mg.st 1
execute if score $k mg.st matches 2 run scoreboard players set $kb mg.st 2
execute if score $k mg.st matches 3 run scoreboard players set $kb mg.st 4
scoreboard players operation $b mg.st = @s mg.trqp
execute if score $k mg.st matches 1..3 run scoreboard players operation $b mg.st /= $kb mg.st
execute if score $k mg.st matches 1..3 run scoreboard players operation $b mg.st %= #2 mg.st
execute if score $k mg.st matches 1..3 if score $b mg.st matches 1 run return run title @s actionbar {"text":"💾 Module déjà récupéré","color":"gray"}
scoreboard players add @s mg.trpk 1
scoreboard players set @s mg.tval 10
execute if score @s mg.trpk matches 1 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮","color":"green"},{"text":"▮▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 2 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮","color":"green"},{"text":"▮▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 3 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮▮","color":"green"},{"text":"▮▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 4 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮▮▮","color":"green"},{"text":"▮▮▮▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 5 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮▮▮▮","color":"green"},{"text":"▮▮▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 6 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮▮▮▮▮","color":"green"},{"text":"▮▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 7 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮▮▮▮▮▮","color":"green"},{"text":"▮","color":"dark_gray"}]
execute if score @s mg.trpk matches 8 run title @s actionbar [{"text":"💾 Récupération ","color":"aqua"},{"text":"▮▮▮▮▮▮▮▮","color":"green"},{"text":"","color":"dark_gray"}]
execute if score @s mg.trpk matches 8.. if score $k mg.st matches 1..3 run function mg:terra/rpg/mod_got
execute if score @s mg.trpk matches 8.. if score $k mg.st matches 9 run function mg:terra/rpg/cell_got
