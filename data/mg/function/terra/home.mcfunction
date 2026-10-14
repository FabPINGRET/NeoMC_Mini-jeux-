# @s : rappel à la colonie (5 s, annulé par un coup)
execute if entity @s[tag=mg.tvcar] run return run function mg:terra/home_no_crate
execute unless entity @s[tag=mg.tvout] run return run function mg:terra/home_here
execute if score @s mg.tvhm matches 1.. run return 0
scoreboard players set @s mg.tvhm 100
scoreboard players set @s mg.tvdt 0
tellraw @s {"text":"📡 Rappel à la colonie dans 5 s… ne prends pas de coup !","color":"green"}
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.6 1.6
