item replace entity @e[tag=knotfire_statue,distance=0..] armor.head from block -10715 54 105 container.0
item replace entity @e[tag=knotfire_statue,distance=0..] armor.chest from block -10715 54 105 container.1
item replace entity @e[tag=knotfire_statue,distance=0..] armor.legs from block -10715 54 105 container.2
item replace entity @e[tag=knotfire_statue,distance=0..] armor.feet from block -10715 54 105 container.3

execute as @e[tag=knotfire_statue,distance=0..] run data modify entity @s equipment.chest.components."minecraft:trim".material set value "minecraft:netherite"
execute as @e[tag=knotfire_statue,distance=0..] run data modify entity @s equipment.legs.components."minecraft:trim".material set value "minecraft:netherite"
execute as @e[tag=knotfire_statue,distance=0..] run data modify entity @s equipment.feet.components."minecraft:trim".material set value "minecraft:netherite"

tp @n[tag=knotfire_statue,tag=1,distance=0..] -10711 72 89
tp @n[tag=knotfire_statue,tag=2,distance=0..] -10685 72 94
tp @n[tag=knotfire_statue,tag=3,distance=0..] -10706 72 80
tp @n[tag=knotfire_statue,tag=4,distance=0..] -10692 72 101
tp @n[tag=knotfire_statue,tag=5,distance=0..] -10697 72 75
tp @n[tag=knotfire_statue,tag=6,distance=0..] -10702 72 101
tp @n[tag=knotfire_statue,tag=7,distance=0..] -10688 72 80
tp @n[tag=knotfire_statue,tag=8,distance=0..] -10709 72 94

execute as @e[tag=knotfire_statue,distance=0..] run data modify entity @s Pose set value {}

execute as @e[tag=knotfire_statue,distance=0..] at @s facing -10697 72 89 run tp @s ~ ~ ~ ~ ~
