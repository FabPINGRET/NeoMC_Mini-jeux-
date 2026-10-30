tag @e[tag=knotfire_statue,distance=0..] remove next_active

item replace entity @e[tag=knotfire_statue,tag=active,distance=0..] armor.head from block -10715 54 105 container.0
item replace entity @e[tag=knotfire_statue,tag=active,distance=0..] armor.chest from block -10715 54 105 container.1
item replace entity @e[tag=knotfire_statue,tag=active,distance=0..] armor.legs from block -10715 54 105 container.2
item replace entity @e[tag=knotfire_statue,tag=active,distance=0..] armor.feet from block -10715 54 105 container.3

execute as @e[tag=knotfire_statue,tag=active,distance=0..] run data modify entity @s equipment.chest.components."minecraft:trim".material set value "minecraft:netherite"
execute as @e[tag=knotfire_statue,tag=active,distance=0..] run data modify entity @s equipment.legs.components."minecraft:trim".material set value "minecraft:netherite"
execute as @e[tag=knotfire_statue,tag=active,distance=0..] run data modify entity @s equipment.feet.components."minecraft:trim".material set value "minecraft:netherite"


tag @e[tag=knotfire_statue,distance=0..] remove active
tag @s add active

item replace entity @s armor.head from block -10715 54 105 container.9
item replace entity @s armor.chest from block -10715 54 105 container.10
item replace entity @s armor.legs from block -10715 54 105 container.11
item replace entity @s armor.feet from block -10715 54 105 container.12

data modify entity @s equipment.chest.components."minecraft:trim".material set value "minecraft:emerald"
data modify entity @s equipment.legs.components."minecraft:trim".material set value "minecraft:emerald"
data modify entity @s equipment.feet.components."minecraft:trim".material set value "minecraft:emerald"

execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s run particle minecraft:copper_fire_flame ~ ~3 ~ 0.8 2 0.8 0.05 100
execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s run particle minecraft:egg_crack ~ ~3 ~ 0.8 2 0.8 0.05 100
execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s run playsound minecraft:block.enchantment_table.use hostile @a[tag=mg.flw] ~ ~ ~ 1 1.8
