# Roulette d'objet de @s (mg.krl : ticks restants)
scoreboard players remove @s mg.krl 1
scoreboard players operation $krm mg.st = @s mg.krl
scoreboard players operation $krm mg.st %= #k2 mg.st
execute if score $krm mg.st matches 0 if score @s mg.krl matches 8.. at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.8 2
execute if score $krm mg.st matches 0 if score @s mg.krl matches 1..7 at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.8 1.6
execute if score @s mg.krl matches 0 if score @s mg.kit matches 0 run function mg:kart/item_roll
execute if score @s mg.krl matches 0 at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5
