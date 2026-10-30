clone -12493 183 -193 -12450 183 -149 -12493 180 -193
fill -12493 180 -193 -12450 180 -149 minecraft:redstone_block replace minecraft:red_concrete
fill -12493 180 -193 -12450 180 -149 minecraft:redstone_block replace minecraft:blue_concrete
fill -12450 183 -149 -12493 183 -193 minecraft:red_stained_glass replace minecraft:red_concrete
fill -12450 183 -149 -12493 183 -193 minecraft:blue_stained_glass replace minecraft:blue_concrete

execute if block -12466 183 -171 minecraft:red_stained_glass run schedule function floaty:sched/boss/secret/attack/floor_reset_red 10t
execute if block -12471 183 -171 minecraft:blue_stained_glass run schedule function floaty:sched/boss/secret/attack/floor_reset_blue 10t

execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if block ~ 183 ~ red_stained_glass run damage @s 20 minecraft:dragon_breath by @n[tag=sc_boss_name,distance=0..]
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if block ~ 183 ~ blue_stained_glass run damage @s 20 minecraft:dragon_breath by @n[tag=sc_boss_name,distance=0..]

execute at @n[tag=sc_boss_pos,distance=0..] run playsound minecraft:block.respawn_anchor.deplete hostile @a[tag=mg.flw] ~ ~ ~ 5 1
