#Reset start latch
setblock -10446 -48 -409 air

#Reset hand tick
fill -10446 -47 -401 -10446 -47 -397 air

#Reset win line
setblock -10446 -48 -376 minecraft:air

tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove targeted
schedule clear floaty:sched/boss/7/target_check
scoreboard players set boss:st_lastattack Value 5

scoreboard players set boss:st_glass bool 1
function boss:7/body_frame/0
fill -10470 -18 -376 -10469 -18 -380 air replace minecraft:player_wall_head
fill -10470 -19 -377 -10470 -21 -379 barrier replace minecraft:lime_stained_glass

fill -10471 -21 -367 -10473 -21 -369 minecraft:polished_deepslate_slab[type=bottom]
fill -10473 -21 -370 -10475 -21 -372 minecraft:polished_deepslate_slab[type=bottom]
fill -10473 -21 -384 -10475 -21 -386 minecraft:polished_deepslate_slab[type=bottom]
fill -10473 -21 -387 -10471 -21 -389 minecraft:polished_deepslate_slab[type=bottom]

execute as @n[tag=st_boss_face_ref_guide,distance=0..] at @s run tp @s ~ ~ ~ -90 0

kill @e[tag=st_hand_draw_1,distance=0..]
kill @e[tag=st_hand_draw_2,distance=0..]
kill @e[tag=st_hand_draw_3,distance=0..]
kill @e[tag=st_hand_draw_4,distance=0..]

kill @e[tag=st_hand_shadow_1,distance=0..]
kill @e[tag=st_hand_shadow_2,distance=0..]
kill @e[tag=st_hand_shadow_3,distance=0..]
kill @e[tag=st_hand_shadow_4,distance=0..]

kill @e[tag=st_hand_dest,distance=0..]
kill @e[tag=st_hand_inter,distance=0..]
kill @e[tag=st_hand_loc,distance=0..]
kill @n[tag=st_boss_statue,distance=0..]
kill @n[tag=st_boss_center_pos,distance=0..]

kill @e[tag=knucklehead,distance=0..]

bossbar set boss:st players
scoreboard players set boss:st BossHealth 6
bossbar set boss:st value 6
bossbar set boss:st color green
