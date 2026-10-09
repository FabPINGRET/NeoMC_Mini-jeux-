# @s : mini-carte (case 30 × 30 de sa position) au-dessus des dollars
execute store result score $gmi mg.st run data get entity @s Pos[0]
execute store result score $gmj mg.st run data get entity @s Pos[2]
scoreboard players add $gmi mg.st 88
scoreboard players remove $gmj mg.st 32312
scoreboard players set #30 mg.st 30
scoreboard players set #177 mg.st 177
scoreboard players operation $gmi mg.st *= #30 mg.st
scoreboard players operation $gmi mg.st /= #177 mg.st
scoreboard players operation $gmj mg.st *= #30 mg.st
scoreboard players operation $gmj mg.st /= #177 mg.st
execute if score $gmi mg.st matches ..-1 run scoreboard players set $gmi mg.st 0
execute if score $gmi mg.st matches 30.. run scoreboard players set $gmi mg.st 29
execute if score $gmj mg.st matches ..-1 run scoreboard players set $gmj mg.st 0
execute if score $gmj mg.st matches 30.. run scoreboard players set $gmj mg.st 29
execute if score $gmj mg.st matches 0 run return run function mg:gta/mini/row_0
execute if score $gmj mg.st matches 1 run return run function mg:gta/mini/row_1
execute if score $gmj mg.st matches 2 run return run function mg:gta/mini/row_2
execute if score $gmj mg.st matches 3 run return run function mg:gta/mini/row_3
execute if score $gmj mg.st matches 4 run return run function mg:gta/mini/row_4
execute if score $gmj mg.st matches 5 run return run function mg:gta/mini/row_5
execute if score $gmj mg.st matches 6 run return run function mg:gta/mini/row_6
execute if score $gmj mg.st matches 7 run return run function mg:gta/mini/row_7
execute if score $gmj mg.st matches 8 run return run function mg:gta/mini/row_8
execute if score $gmj mg.st matches 9 run return run function mg:gta/mini/row_9
execute if score $gmj mg.st matches 10 run return run function mg:gta/mini/row_10
execute if score $gmj mg.st matches 11 run return run function mg:gta/mini/row_11
execute if score $gmj mg.st matches 12 run return run function mg:gta/mini/row_12
execute if score $gmj mg.st matches 13 run return run function mg:gta/mini/row_13
execute if score $gmj mg.st matches 14 run return run function mg:gta/mini/row_14
execute if score $gmj mg.st matches 15 run return run function mg:gta/mini/row_15
execute if score $gmj mg.st matches 16 run return run function mg:gta/mini/row_16
execute if score $gmj mg.st matches 17 run return run function mg:gta/mini/row_17
execute if score $gmj mg.st matches 18 run return run function mg:gta/mini/row_18
execute if score $gmj mg.st matches 19 run return run function mg:gta/mini/row_19
execute if score $gmj mg.st matches 20 run return run function mg:gta/mini/row_20
execute if score $gmj mg.st matches 21 run return run function mg:gta/mini/row_21
execute if score $gmj mg.st matches 22 run return run function mg:gta/mini/row_22
execute if score $gmj mg.st matches 23 run return run function mg:gta/mini/row_23
execute if score $gmj mg.st matches 24 run return run function mg:gta/mini/row_24
execute if score $gmj mg.st matches 25 run return run function mg:gta/mini/row_25
execute if score $gmj mg.st matches 26 run return run function mg:gta/mini/row_26
execute if score $gmj mg.st matches 27 run return run function mg:gta/mini/row_27
execute if score $gmj mg.st matches 28 run return run function mg:gta/mini/row_28
execute if score $gmj mg.st matches 29 run return run function mg:gta/mini/row_29
