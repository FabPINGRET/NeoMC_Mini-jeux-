setblock -10462 43 -74 air
particle minecraft:dust_pillar{block_state:"honey_block"} ~ ~0.1 ~ 0.5 0 0.5 2 200 force @a[tag=mg.flw]
particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0 10 force @a[tag=mg.flw]

playsound minecraft:entity.shulker_bullet.hurt hostile @a[tag=mg.flw] ~ ~ ~ 2 1
playsound minecraft:block.honey_block.break hostile @a[tag=mg.flw] ~ ~ ~ 2 0.5
playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ ~ ~ 2 2

fill ~-1 79 ~-1 ~1 79 ~1 honey_block replace iron_bars

execute as @a[distance=..3,tag=mg.flw] run damage @s 20 minecraft:explosion

kill @n[tag=boss_sh_honeybomb_arrow,type=arrow,distance=0..]
