tag @n[tag=frostbyte_volley_pos,distance=0..] remove unpowered
tag @n[tag=frostbyte_volley_pos,distance=0..] add powered

execute as @e[tag=frostbyte_volley,distance=0..] run data modify entity @s block_state.Name set value "minecraft:lapis_ore"

execute as @e[tag=frostbyte_volley,distance=0..] at @s run playsound minecraft:block.respawn_anchor.charge master @a[tag=mg.flw] ~ ~ ~ 2 1
