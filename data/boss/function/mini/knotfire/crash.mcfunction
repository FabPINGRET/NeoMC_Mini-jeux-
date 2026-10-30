tp @n[tag=knotfire_statue,tag=active,distance=0..] ~ ~ ~ ~ ~

tag @n[tag=knotfire_statue,tag=active,distance=0..] add crashed

playsound minecraft:entity.ender_dragon.flap hostile @a[tag=mg.flw] -10697 71 89 1 1
playsound minecraft:item.lodestone_compass.lock hostile @a[tag=mg.flw] -10697 71 89 2 0.1
playsound minecraft:entity.camel_husk.dash hostile @a[tag=mg.flw] -10697 71 89 1 2
playsound minecraft:item.mace.smash_ground master @a[tag=mg.flw] ~ ~ ~ 3 1

execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s positioned ^ ^ ^3 run tp @n[tag=knotfire_boss,distance=0..] ~ ~ ~ ~ ~
execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s positioned ^ ^ ^3 run particle minecraft:copper_fire_flame ~ 74 ~ 0.4 1 0.4 0.5 500


item replace entity @e[tag=knotfire_statue,tag=active,distance=0..] armor.head from block -10715 54 105 container.0
execute as @e[tag=knotfire_statue,tag=active,distance=0..] run data modify entity @s equipment.chest.components."minecraft:trim".material set value "minecraft:netherite"
execute as @e[tag=knotfire_statue,tag=active,distance=0..] run data modify entity @s equipment.legs.components."minecraft:trim".material set value "minecraft:netherite"
execute as @e[tag=knotfire_statue,tag=active,distance=0..] run data modify entity @s equipment.feet.components."minecraft:trim".material set value "minecraft:netherite"

tag @e[tag=knotfire_statue,distance=0..] remove active
