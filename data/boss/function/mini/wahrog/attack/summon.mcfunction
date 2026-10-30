execute at @n[tag=wahrog_stand,distance=0..] as @a[gamemode=!spectator,tag=mg.flw] run function summon:crackling_parasite
execute at @n[tag=wahrog_stand,distance=0..] run playsound minecraft:block.conduit.attack.target hostile @a[tag=mg.flw] ~ ~ ~ 3 2
execute at @n[tag=wahrog_stand,distance=0..] run particle electric_spark ~ ~1 ~ 0.2 0.6 0.2 0.5 80
