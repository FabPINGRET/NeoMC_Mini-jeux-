spreadplayers -9960 370 6 8 false @e[tag=mem_fight_spread,distance=0..]
execute as @a[gamemode=!spectator,tag=mg.flw] at @n[tag=mem_fight_spread,tag=2,distance=0..] positioned ~ 100 ~ run function summon:memory_monster
execute as @a[gamemode=!spectator,tag=mg.flw] at @n[tag=mem_fight_spread,tag=3,distance=0..] positioned ~ 100 ~ run function summon:memory_monster

function boss:mini/memory_contagion/hide_contagion
execute as @n[tag=mem_fight_spread,tag=1,distance=0..] at @s run tp @n[tag=mem_nexus,distance=0..] ~ 100 ~

execute at @n[tag=mem_nexus,distance=0..] run playsound minecraft:block.trial_spawner.spawn_mob hostile @a[tag=mg.flw] ~ ~ ~ 1 1
execute as @e[tag=mem_monster,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob hostile @a[tag=mg.flw] ~ ~ ~ 1 1


# paint tag on
setblock -9948 84 357 minecraft:redstone_block
