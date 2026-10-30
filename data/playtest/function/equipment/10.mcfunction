scoreboard players set Inventory HeartContainers 19
attribute @s minecraft:max_health base set 38
effect give @a[tag=mg.flw] minecraft:saturation 3 100 true
effect give @a[tag=mg.flw] minecraft:regeneration 3 100 true
effect give @a[tag=mg.flw] minecraft:instant_health 3 100 true
execute as @a[tag=mg.flw] run attribute @s minecraft:fall_damage_multiplier base set 0

execute positioned -9761 289 429 run function playtest:chest_equip
