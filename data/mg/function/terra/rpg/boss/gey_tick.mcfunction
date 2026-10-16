# @s (geyser) : 2 s d'avertissement puis jaillissement
scoreboard players remove @s mg.tvst 1
execute if score @s mg.tvst matches 1.. run particle minecraft:lava ~ ~0.2 ~ 0.6 0.1 0.6 0 8
execute if score @s mg.tvst matches 1.. run particle minecraft:large_smoke ~ ~0.2 ~ 0.6 0.1 0.6 0.02 10
execute if score @s mg.tvst matches 1.. run return 0
particle minecraft:flame ~ ~1 ~ 0.6 2 0.6 0.1 120 force
particle minecraft:lava ~ ~1 ~ 0.6 1.5 0.6 0 30 force
playsound minecraft:block.lava.extinguish hostile @a ~ ~ ~ 1.5 0.6
execute as @a[tag=mg.tvw,gamemode=adventure,distance=..2] run damage @s 8 minecraft:in_fire
execute as @a[tag=mg.tvw,gamemode=adventure,distance=..2] run effect give @s minecraft:levitation 1 4 true
kill @s
