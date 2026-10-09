# @s tient la carte : plan de la ville au centre de l'écran, sa position en rouge
execute unless score $rp mg.st matches 1 run return run title @s actionbar [{"text":"🗺 Carte : active le resource pack (/function mg:rp_on)","color":"gray"}]
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
title @s times 0 6 2
scoreboard players set @s mg.gal 6
title @s actionbar [{"text":"■ ","color":"#9646C8"},{"text":"Concession  ","color":"gray"},{"text":"■ ","color":"#C82828"},{"text":"Armurerie  ","color":"gray"},{"text":"■ ","color":"#E8BA24"},{"text":"Banque  ","color":"gray"},{"text":"■ ","color":"#F58C1E"},{"text":"Commerces  ","color":"gray"},{"text":"■ ","color":"#28C8DC"},{"text":"Villa","color":"gray"}]
execute if score $gmj mg.st matches 0 run return run function mg:gta/map/row_0
execute if score $gmj mg.st matches 1 run return run function mg:gta/map/row_1
execute if score $gmj mg.st matches 2 run return run function mg:gta/map/row_2
execute if score $gmj mg.st matches 3 run return run function mg:gta/map/row_3
execute if score $gmj mg.st matches 4 run return run function mg:gta/map/row_4
execute if score $gmj mg.st matches 5 run return run function mg:gta/map/row_5
execute if score $gmj mg.st matches 6 run return run function mg:gta/map/row_6
execute if score $gmj mg.st matches 7 run return run function mg:gta/map/row_7
execute if score $gmj mg.st matches 8 run return run function mg:gta/map/row_8
execute if score $gmj mg.st matches 9 run return run function mg:gta/map/row_9
execute if score $gmj mg.st matches 10 run return run function mg:gta/map/row_10
execute if score $gmj mg.st matches 11 run return run function mg:gta/map/row_11
execute if score $gmj mg.st matches 12 run return run function mg:gta/map/row_12
execute if score $gmj mg.st matches 13 run return run function mg:gta/map/row_13
execute if score $gmj mg.st matches 14 run return run function mg:gta/map/row_14
execute if score $gmj mg.st matches 15 run return run function mg:gta/map/row_15
execute if score $gmj mg.st matches 16 run return run function mg:gta/map/row_16
execute if score $gmj mg.st matches 17 run return run function mg:gta/map/row_17
execute if score $gmj mg.st matches 18 run return run function mg:gta/map/row_18
execute if score $gmj mg.st matches 19 run return run function mg:gta/map/row_19
execute if score $gmj mg.st matches 20 run return run function mg:gta/map/row_20
execute if score $gmj mg.st matches 21 run return run function mg:gta/map/row_21
execute if score $gmj mg.st matches 22 run return run function mg:gta/map/row_22
execute if score $gmj mg.st matches 23 run return run function mg:gta/map/row_23
execute if score $gmj mg.st matches 24 run return run function mg:gta/map/row_24
execute if score $gmj mg.st matches 25 run return run function mg:gta/map/row_25
execute if score $gmj mg.st matches 26 run return run function mg:gta/map/row_26
execute if score $gmj mg.st matches 27 run return run function mg:gta/map/row_27
execute if score $gmj mg.st matches 28 run return run function mg:gta/map/row_28
execute if score $gmj mg.st matches 29 run return run function mg:gta/map/row_29
