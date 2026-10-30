scoreboard players operation sc_boss_toggle bool = sc_boss_color bool

execute if score sc_boss_toggle bool matches 0 run function boss:secret/blue_switch
execute if score sc_boss_toggle bool matches 1 run function boss:secret/red_switch

execute at @n[tag=sc_boss_pos,distance=0..] run playsound minecraft:block.vault.open_shutter hostile @a[tag=mg.flw] ~ ~ ~ 3 1.3

execute if block -12466 183 -171 minecraft:red_concrete run function boss:secret/attack/floor_erupt
execute if block -12471 183 -171 minecraft:blue_concrete run function boss:secret/attack/floor_erupt

execute if entity @e[tag=sc_boss_turret,distance=0..] run setblock -12475 161 -175 minecraft:redstone_block
