execute as @e[tag=boss_skt_hole_1,distance=0..] at @s run clone -10233 73 410 -10225 83 418 ~-4 ~1 ~-5
execute as @e[tag=boss_skt_hole_1,distance=0..] at @s run clone -10230 72 414 -10228 72 416 ~-1 ~ ~-1
particle block{block_state:"minecraft:moss_block"} -10222 98 433 2 5 1 0 300 force
particle block{block_state:"minecraft:bamboo_planks"} -10222 98 433 2 5 1 0 100 force
playsound minecraft:entity.bogged.death master @a[tag=mg.flw] -10222 94 433 4 0.5
playsound minecraft:entity.evoker.death master @a[tag=mg.flw] -10222 94 433 4 0.5
playsound minecraft:entity.phantom.death master @a[tag=mg.flw] -10222 94 433 3 0.7
setblock -10201 55 405 minecraft:redstone_block
