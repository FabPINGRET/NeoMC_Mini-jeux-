# @s = ancien porteur
item replace entity @s armor.head with minecraft:air
item replace entity @s armor.chest with minecraft:air
effect clear @s minecraft:speed
effect clear @s minecraft:jump_boost
effect clear @s minecraft:glowing
team leave @s
tag @s remove mg.bomb
