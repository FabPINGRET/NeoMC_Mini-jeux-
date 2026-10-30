summon armor_stand -10072 116 -355 {NoGravity:1b,Invulnerable:1b,ShowArms:1b,Invisible:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["boss_ed_cutscene"],DisabledSlots:4144959,Rotation:[-90F,0F],equipment:{feet:{id:"minecraft:chainmail_boots",count:1,components:{"minecraft:trim":{material:"minecraft:redstone",pattern:"minecraft:tide"}}},legs:{id:"minecraft:chainmail_leggings",count:1,components:{"minecraft:trim":{material:"minecraft:redstone",pattern:"minecraft:tide"}}},chest:{id:"minecraft:chainmail_chestplate",count:1,components:{"minecraft:trim":{material:"minecraft:redstone",pattern:"minecraft:tide"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;1646574283,-1653911923,-1227161329,-839415811],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTkwY2JkNzJlNDFhOWJkNDExYmU5MjliNzNmZDI2OTIwNjM2OGIyODEwZDZjNjgxOTkxOGNiOGViNjYyMjRmNCJ9fX0="}]}}},mainhand:{id:"minecraft:blaze_powder",count:1},offhand:{id:"minecraft:blaze_powder",count:1}}}
execute as @e[tag=boss_ed_cutscene,distance=0..] at @s run particle minecraft:lava ~ ~1 ~ 1 1 1 0 100
execute as @e[tag=boss_ed_cutscene,distance=0..] at @s run particle minecraft:smoke ~ ~ ~ 0.5 0.5 0.5 0.2 30
execute as @e[tag=boss_ed_cutscene,distance=0..] at @s run playsound minecraft:entity.strider.happy master @a[tag=mg.flw] ~ ~ ~ 4 0.1
execute as @e[tag=boss_ed_cutscene,distance=0..] at @s run playsound minecraft:entity.strider.death master @a[tag=mg.flw] ~ ~ ~ 4 2
execute as @e[tag=boss_ed_cutscene,distance=0..] at @s run playsound minecraft:entity.firework_rocket.twinkle_far master @a[tag=mg.flw] ~ ~ ~ 4 0.7
execute as @e[tag=boss_ed_cutscene,distance=0..] at @s run playsound minecraft:entity.ravager.hurt master @a[tag=mg.flw] ~ ~ ~ 4 0.1

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/5 3s
