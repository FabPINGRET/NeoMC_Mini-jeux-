execute as @n[tag=wahrog_boss,distance=0..] at @s run playsound minecraft:entity.drowned.hurt_water hostile @a[tag=mg.flw] ~ ~ ~ 2 1
execute as @n[tag=wahrog_boss,distance=0..] at @s run particle minecraft:ominous_spawning ~ ~1 ~ 0.2 0.6 0.2 1 200

tp @n[tag=wahrog_boss,distance=0..] -11146 18 332
function boss:mini/wahrog/new_position
