execute as @n[tag=cob_boss_cutscene,distance=0..] at @s run playsound minecraft:entity.skeleton.hurt neutral @a[tag=mg.flw] ~ ~ ~ 3 0.7
execute at @e[tag=cob_boss_cutscene,distance=0..] positioned ~ ~1 ~ run particle minecraft:block{block_state:"bone_block"} ~ ~ ~ 1 1 1 1 200 force
kill @e[tag=cob_boss_cutscene,distance=0..]
playsound minecraft:entity.ender_dragon.hurt hostile @a[tag=mg.flw] -10155 158 -31 1 0.1 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bone Nexus","color":"gray"},{"text":"> Wakey, wakey!","color":"white"}]
setblock -10128 138 -39 minecraft:redstone_block
setblock -10151 138 -15 minecraft:redstone_block

# FIGHT START!
