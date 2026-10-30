kill @e[tag=boss_sop_flowerbomb,distance=0..]

execute at @e[tag=cherry_bomb_loc,distance=0..] run particle minecraft:cherry_leaves ~ ~ ~ 1.5 1.5 1.5 0 150
execute at @e[tag=cherry_bomb_loc,distance=0..] run particle minecraft:explosion ~ ~ ~ 1.5 1.5 1.5 0 10

execute at @e[tag=cherry_bomb_loc,distance=0..] as @a[distance=..3,tag=mg.flw] run damage @s 6 minecraft:sweet_berry_bush

execute at @e[tag=cherry_bomb_loc,distance=0..] run playsound minecraft:block.sweet_berry_bush.break hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute at @e[tag=cherry_bomb_loc,distance=0..] run playsound minecraft:entity.iron_golem.hurt hostile @a[tag=mg.flw] ~ ~ ~ 1 2

execute at @e[tag=cherry_bomb_loc,distance=0..] run summon item ~ ~ ~ {Item:{id:"minecraft:arrow",count:1}}

kill @e[tag=cherry_bomb_loc,distance=0..]
