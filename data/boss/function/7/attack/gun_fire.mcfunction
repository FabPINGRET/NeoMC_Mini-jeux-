execute as @n[tag=st_hand_loc_1,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_1,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 facing ^ ^ ^-1 run function boss:7/utility/gun_ray
execute as @n[tag=st_hand_loc_2,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_2,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 facing ^ ^ ^-1 run function boss:7/utility/gun_ray
execute as @n[tag=st_hand_loc_3,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_3,distance=0..] positioned ^ ^0.25 ^-3.9 facing ^ ^ ^-1 run function boss:7/utility/gun_ray
execute as @n[tag=st_hand_loc_4,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_4,distance=0..] positioned ^ ^0.25 ^-3.9 facing ^ ^ ^-1 run function boss:7/utility/gun_ray

execute as @n[tag=st_hand_loc_1,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_1,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 facing ^ ^ ^-1 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_2,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_2,distance=0..] positioned ^-0.1 ^0.25 ^-3.7 facing ^ ^ ^-1 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_3,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_3,distance=0..] positioned ^ ^0.25 ^-3.9 facing ^ ^ ^-1 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1 force
execute as @n[tag=st_hand_loc_4,tag=gun_attacking,distance=0..] at @s rotated as @n[tag=st_hand_draw_4,distance=0..] positioned ^ ^0.25 ^-3.9 facing ^ ^ ^-1 run particle minecraft:explosion ~ ~ ~ 0 0 0 0 1 force

execute as @n[tag=st_hand_loc,tag=gun_attacking,distance=0..] at @s run playsound minecraft:block.lodestone.place hostile @a[tag=mg.flw] ~ ~ ~ 2 2
execute as @n[tag=st_hand_loc,tag=gun_attacking,distance=0..] at @s run playsound minecraft:entity.evoker.cast_spell hostile @a[tag=mg.flw] ~ ~ ~ 2 2
execute as @n[tag=st_hand_loc,tag=gun_attacking,distance=0..] at @s run playsound minecraft:item.crossbow.shoot hostile @a[tag=mg.flw] ~ ~ ~ 1 2

tag @s remove gun_attacking
tag @s remove attacking
function boss:7/hand_frame/recoil
schedule function floaty:sched/boss/7/attack/gun_return 40t replace
