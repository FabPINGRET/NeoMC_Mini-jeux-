item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.chest with air
item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.legs with air
item replace entity @n[tag=mem_nexus_stand,distance=0..] armor.feet with air
item replace entity @n[tag=mem_nexus_stand,distance=0..] weapon.mainhand with air

execute at @n[tag=mem_nexus_stand,distance=0..] run playsound minecraft:block.trial_spawner.ominous_activate hostile @a[tag=mg.flw] ~ ~ ~ 1 1.4

data modify entity @n[tag=mem_nexus_stand,distance=0..] Invisible set value 1b
execute as @n[tag=mem_nexus_stand,distance=0..] at @s run particle minecraft:composter ~ ~1 ~ 0.2 0.6 0.2 0.5 40
