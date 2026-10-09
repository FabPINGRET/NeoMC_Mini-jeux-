# Un œuf en vol (@s = l'œuf, à sa position) : traînée, durée de vie, puis rayon de 1,75 bloc dans le sens de son déplacement
particle minecraft:snowflake ~ ~ ~ 0 0 0 0 1
scoreboard players add @s mg.ag 1
execute if score @s mg.ag > $sgl mg.st run return run kill @s
data modify storage mg:c mx set from entity @s Motion[0]
data modify storage mg:c my set from entity @s Motion[1]
data modify storage mg:c mz set from entity @s Motion[2]
scoreboard players set $sgs mg.st 7
function mg:splegg/egg_aim with storage mg:c
