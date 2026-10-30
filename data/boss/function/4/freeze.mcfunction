execute as @e[tag=boss_ed_fella,distance=0..] at @s run fill ~-3 116 ~-3 ~3 130 ~3 magma_block replace minecraft:red_glazed_terracotta
setblock -10071 95 -371 air
execute as @e[tag=boss_ed_fella,distance=0..] at @s run particle block{block_state:"minecraft:magma_block"} ~ ~2 ~ 2 2 2 0 200
execute as @e[tag=boss_ed_fella,distance=0..] at @s run playsound minecraft:entity.strider.eat hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7
execute as @e[tag=boss_ed_fella,distance=0..] at @s run playsound minecraft:entity.player.hurt_freeze hostile @a[tag=mg.flw] ~ ~ ~ 3 0.1
setblock ~ ~-1 ~ magma_block
setblock ~ ~ ~ magma_block
