item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.head from block -9959 84 369 container.0
item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.chest from block -9959 84 369 container.1
item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.legs from block -9959 84 369 container.2
item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.feet from block -9959 84 369 container.3
item replace entity @n[tag=mem_nexus_stand,distance=0..] weapon.mainhand from block -9959 84 369 container.4

data modify entity @n[tag=mem_nexus_stand,distance=0..] Invisible set value 0b

execute as @n[tag=mem_nexus_stand,distance=0..] at @s run particle minecraft:composter ~ ~1 ~ 0.2 0.6 0.2 0.5 40
