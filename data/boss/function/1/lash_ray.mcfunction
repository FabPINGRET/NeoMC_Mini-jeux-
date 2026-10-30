fill ~ ~ ~ ~ ~ ~ flowering_azalea_leaves[persistent=true] replace air

execute if block ^ ^ ^ sculk run playsound minecraft:block.azalea.break hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1 1
execute if block ^ ^ ^ sculk run playsound minecraft:block.bamboo.break hostile @a[tag=mg.flw] ~ ~ ~ 1 1 1

execute unless block ^ ^ ^ sculk positioned ^ ^ ^0.1 run function boss:1/lash_ray
