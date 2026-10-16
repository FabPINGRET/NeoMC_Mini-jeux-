# Rugissement : les colons proches sont ralentis et aveuglés un instant
scoreboard players set $trr2 mg.st 14
scoreboard players set @s mg.tvat 20
tag @s add mg.tvroar
execute at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 3 0.45
execute at @s run playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 2 0.6
execute at @s run particle minecraft:sonic_boom ^ ^3 ^3 0 0 0 0 1 force
execute at @s as @a[tag=mg.tvw,gamemode=adventure,distance=..24] run effect give @s minecraft:slowness 3 1
execute at @s as @a[tag=mg.tvw,gamemode=adventure,distance=..24] run effect give @s minecraft:darkness 3 0 true
