execute as @n[tag=wahrog_stand,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 2 1
#execute as @n[tag=wahrog_stand] at @s run particle minecraft:ominous_spawning ~ ~1 ~ 0.2 0.6 0.2 1 200

tp @n[tag=wahrog_boss,distance=0..] @n[tag=wahrog_stand,distance=0..]
tp @n[tag=wahrog_stand,distance=0..] -11146 18 332
data modify entity @n[tag=wahrog_boss,distance=0..] last_hurt_by_player set from entity @n[tag=targeted,distance=0..] UUID
data modify entity @n[tag=wahrog_boss,distance=0..] last_hurt_by_player_memory_time set value 100
