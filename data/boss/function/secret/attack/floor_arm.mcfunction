execute if score sc_boss_color bool matches 0 run fill -12493 183 -193 -12450 183 -149 minecraft:red_concrete replace minecraft:polished_diorite
execute if score sc_boss_color bool matches 1 run fill -12493 183 -193 -12450 183 -149 minecraft:blue_concrete replace minecraft:polished_blackstone

execute at @n[tag=sc_boss_pos,distance=0..] run playsound minecraft:block.respawn_anchor.set_spawn hostile @a[tag=mg.flw] ~ ~ ~ 5 2
