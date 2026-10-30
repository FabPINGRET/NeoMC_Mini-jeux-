execute as @n[tag=lord_morbex_stand,distance=0..] at @s run summon item_display ~ ~ ~ {interpolation_duration:40,Tags:["morbex_sunray_sword"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,1f,0.4f],translation:[0f,1f,0f],scale:[3f,3f,3f]},item:{id:"minecraft:iron_sword",count:1,components:{"minecraft:custom_model_data":{strings:["100"]}}}}
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run summon armor_stand ~ ~ ~ {Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["morbex_sunray_sword_loc"],attributes:[{id:"minecraft:gravity",base:4}],DisabledSlots:4144959}

execute as @n[tag=morbex_sunray_sword_loc,distance=0..] at @s rotated as @n[tag=lord_morbex_stand,distance=0..] run tp @s ~ ~ ~ ~ 0

execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:entity.wind_charge.throw hostile @a[tag=mg.flw] ~ ~ ~ 3 0.6

#Start tick
setblock -12358 43 333 redstone_block
