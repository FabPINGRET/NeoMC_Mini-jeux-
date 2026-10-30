playsound minecraft:entity.drowned.ambient_water neutral @s -11223 -18 -109 5 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> I am free!","color":"white"},{"text":" Frogcrates","color":"#44BBFF"},{"text":", can you hear me? What happened?","color":"white"},{"text":" ⇒","color":"light_purple"}]

summon armor_stand -11223 -18 -109 {NoGravity:1b,Silent:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["npc","lord_of_water"],DisabledSlots:4144959,Rotation:[-90F,0F],equipment:{feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":3881546,"minecraft:trim":{material:"minecraft:quartz",pattern:"minecraft:tide"}}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":3881546,"minecraft:trim":{material:"minecraft:quartz",pattern:"minecraft:tide"}}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":3881546,"minecraft:trim":{material:"minecraft:quartz",pattern:"minecraft:tide"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2E4ODMyYTdiMGFlMGYwMjgxODZiNTg2YTU2ZmY3YzBiYWUzZDNmNjBkMDllNzZjZGMxNWYwN2YwZDNiMzExZiJ9fX0="}]}}}},CustomName:{"color":"blue","text":"Lord of Water"}}

#particles
setblock -11237 -34 -132 redstone_block

execute as @n[tag=lord_of_water,distance=0..] at @s run particle minecraft:splash ~ ~1 ~ 0.4 0.8 0.4 0 150
execute as @n[tag=lord_of_water,distance=0..] at @s run particle minecraft:bubble_pop ~ ~1 ~ 0.4 0.8 0.4 0 150
execute as @n[tag=lord_of_water,distance=0..] at @s run playsound minecraft:ambient.underwater.enter master @a[tag=mg.flw] -11223 -20 -109 5 0.1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_3 6.8s
