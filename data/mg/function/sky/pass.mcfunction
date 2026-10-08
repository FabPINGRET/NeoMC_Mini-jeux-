# Anneau franchi (@s)
scoreboard players add @s mg.skr 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.5
particle minecraft:totem_of_undying ~ ~ ~ 0.6 0.6 0.6 0.3 15 force @s
execute if score @s mg.skr matches 4 run function mg:sky/boost
execute if score @s mg.skr matches 9 run function mg:sky/boost
execute if score @s mg.skr matches 14 run function mg:sky/boost
execute if score @s mg.skr matches 18 run function mg:sky/boost
execute if score @s mg.skr matches 20.. run return run function mg:sky/finish
