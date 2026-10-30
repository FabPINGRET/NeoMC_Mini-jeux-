tp @n[tag=lord_morbex_stand,distance=0..] -12384 123 355
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run particle minecraft:trial_omen ~ ~3 ~ 1 2 1 1 75
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item_begin master @a[tag=mg.flw] ~ ~ ~ 3 1
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob master @a[tag=mg.flw] ~ ~ ~ 3 1

#start face player
setblock -12346 43 336 minecraft:redstone_block

execute positioned -12384 58 355 run function summon:lord_morbex_2

schedule function floaty:sched/boss/final/cutscene/2 3s replace

#","color":"white"},{"text":"
