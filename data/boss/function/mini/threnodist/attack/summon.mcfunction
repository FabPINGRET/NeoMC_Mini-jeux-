execute as @n[tag=threnodist_stand,distance=0..] at @s as @a[gamemode=!spectator,tag=mg.flw] positioned ~ ~4 ~ run function summon:dark_hymnodist
execute as @n[tag=threnodist_stand,distance=0..] at @s as @a[gamemode=!spectator,tag=mg.flw] positioned ~ ~4 ~ run function summon:dark_hymnodist
execute as @n[tag=threnodist_stand,distance=0..] at @s run particle minecraft:reverse_portal ~ ~1.5 ~ 0 0 0 0.5 200
execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7
