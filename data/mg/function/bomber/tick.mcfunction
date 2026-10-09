# 💣 Bombardier : tick
scoreboard players add $btt mg.st 1
execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:bomber/use
scoreboard players reset @a[scores={mg.qs=1..}] mg.qs
scoreboard players remove @a[scores={mg.bc1=1..}] mg.bc1 1
scoreboard players remove @a[scores={mg.bc2=1..}] mg.bc2 1
scoreboard players remove @a[scores={mg.bc3=1..}] mg.bc3 1
execute as @e[type=minecraft:tnt,tag=mg.bomb] at @s run function mg:bomber/bomb_tick
scoreboard players add @e[type=minecraft:marker,tag=mg.bsm] mg.bc4 1
execute as @e[type=minecraft:marker,tag=mg.bsm,scores={mg.bc4=400..}] run kill @s
scoreboard players operation $bq mg.st = $btt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $bq mg.st %= #20 mg.st
execute if score $bq mg.st matches 0 run function mg:bomber/second
execute if score $bq mg.st matches 0 run execute at @e[type=minecraft:marker,tag=mg.bsm] run particle minecraft:campfire_cosy_smoke ~ ~ ~ 0.8 0.3 0.8 0.02 3 force
execute if score $bq mg.st matches 10 run execute at @e[type=minecraft:marker,tag=mg.bsm] run particle minecraft:flame ~ ~0.5 ~ 0.8 0.3 0.8 0.01 4
execute if score $btt mg.st matches 1800 run function mg:bomber/nuke_give
execute if score $btt mg.st matches 2400 run tellraw @a[tag=mg.play] {"text":"💣 Plus que 30 secondes !","color":"gold"}
execute if score $state mg.st matches 2 if score $btt mg.st matches 3000.. run function mg:bomber/timeout
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
