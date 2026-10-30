scoreboard players set final_morbex_target_mode Value 1
execute as @n[tag=l_morbex_2,distance=0..] at @s run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 3 1
execute as @n[tag=l_morbex_2,distance=0..] at @s run particle minecraft:trial_omen ~ ~3 ~ 1 2 1 1 75
tp @n[tag=lord_morbex_stand,distance=0..] @n[tag=l_morbex_2,distance=0..]
tp @n[tag=l_morbex_2,distance=0..] -12384 58 355
scoreboard players set morbex_hurtable bool 0
function boss:final/morbex/new_position
schedule function floaty:sched/boss/final/morbex/pick_attack 3s
