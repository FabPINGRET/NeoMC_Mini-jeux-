execute at @n[tag=mem_nexus,distance=0..] run playsound minecraft:block.trial_spawner.ominous_activate hostile @a[tag=mg.flw] ~ ~ ~ 1 1.4

item replace entity @n[tag=mem_nexus,distance=0..] armor.head with air
item replace entity @n[tag=mem_nexus,distance=0..] armor.chest with air
item replace entity @n[tag=mem_nexus,distance=0..] armor.legs with air
item replace entity @n[tag=mem_nexus,distance=0..] armor.feet with air
item replace entity @n[tag=mem_nexus,distance=0..] weapon.mainhand with air

attribute @n[tag=mem_nexus,distance=0..] minecraft:armor base set 17
attribute @n[tag=mem_nexus,distance=0..] minecraft:attack_damage base set 6
effect give @n[tag=mem_nexus,distance=0..] minecraft:invisibility infinite 0 true

execute as @n[tag=mem_nexus,distance=0..] at @s run particle minecraft:composter ~ ~1 ~ 0.2 0.6 0.2 0.5 40

execute as @n[tag=mem_nexus,tag=enemy,distance=0..] run tp @s -9960 69 370
