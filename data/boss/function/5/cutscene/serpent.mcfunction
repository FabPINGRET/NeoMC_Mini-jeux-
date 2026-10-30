execute as @e[tag=boss_skt_hole_1,distance=0..] at @s run clone -10243 73 410 -10235 83 418 ~-4 ~1 ~-5
execute as @e[tag=boss_skt_hole_1,distance=0..] at @s run clone -10240 72 414 -10238 72 416 ~-1 ~ ~-1

playsound minecraft:entity.phantom.hurt master @a[tag=mg.flw] -10222 94 433 3 0.5
particle block{block_state:"minecraft:coarse_dirt"} -10222 98 433 2 5 1 0 100 force
execute as @e[tag=boss_skt_hole_1,distance=0..] at @s run particle dust_pillar{block_state:"minecraft:coarse_dirt"} ~ ~ ~ 1 0 1 1 300 force
