fill ~-1 ~ ~-1 ~ ~9 ~ barrier replace air
playsound minecraft:item.mace.smash_ground master @a[tag=mg.flw] ~ ~ ~ 3 1
particle minecraft:block{block_state:"snow"} ~ ~0.5 ~ 1.5 0.5 1.5 0 200 normal
tag @s add grounded
execute positioned ~ ~10 ~ run function summon:mooneye
execute as @a[distance=..4,tag=mg.flw] run damage @s 55 minecraft:falling_anvil
