execute if entity @s[tag=mg.kred] run return run kill @s
execute if score @s mg.kdr matches 3.. run return run kill @s
scoreboard players add @s mg.kdr 1
tp @s ~ ~ ~ ~180 0
playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 1.4
