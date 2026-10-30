item replace entity @n[tag=mem_nexus,distance=0..] armor.head from block -9959 84 369 container.0
item replace entity @n[tag=mem_nexus,distance=0..] armor.chest from block -9959 84 369 container.1
item replace entity @n[tag=mem_nexus,distance=0..] armor.legs from block -9959 84 369 container.2
item replace entity @n[tag=mem_nexus,distance=0..] armor.feet from block -9959 84 369 container.3
item replace entity @n[tag=mem_nexus,distance=0..] weapon.mainhand from block -9959 84 369 container.4

attribute @n[tag=mem_nexus,distance=0..] minecraft:armor base reset
attribute @n[tag=mem_nexus,distance=0..] minecraft:attack_damage base reset
effect clear @n[tag=mem_nexus,distance=0..] minecraft:invisibility

execute as @n[tag=mem_nexus,distance=0..] at @s run particle minecraft:composter ~ ~1 ~ 0.2 0.6 0.2 0.5 40
