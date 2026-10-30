execute as @n[tag=wv_model_crown,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~
execute as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~
execute as @n[tag=wv_model_smallarm,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~
execute as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~


fill -12389 123 350 -12379 134 360 light[level=15]
clone -12389 22 350 -12379 27 360 -12389 123 350
function boss:final/arena/reset_light

function boss:final/arena/split_platform
particle minecraft:dust_pillar{block_state:"sculk"} -12369 123 355 3 0 5 1 500
particle minecraft:dust_pillar{block_state:"sculk"} -12362 123 365 2 0 1 1 200
particle minecraft:dust_pillar{block_state:"sculk"} -12362 123 345 2 0 1 1 200


playsound minecraft:item.mace.smash_ground_heavy master @a[tag=mg.flw] -12384 122 355 5 0.7

schedule function floaty:sched/boss/final/cutscene/41 10t replace

#","color":"white"},{"text":"
