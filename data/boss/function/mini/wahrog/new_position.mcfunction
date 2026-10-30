execute as @n[tag=wahrog_stand,distance=0..] at @s run particle minecraft:ominous_spawning ~ ~1 ~ 0.2 0.6 0.2 1 200
execute as @n[tag=wahrog_stand,distance=0..] at @s run playsound minecraft:block.conduit.attack.target hostile @a[tag=mg.flw] ~ ~ ~ 3 2

function boss:mini/wahrog/rand
execute as @e[tag=wahrog_rand,limit=1,sort=random,distance=0..] at @s run tp @n[tag=wahrog_stand,distance=0..] ~ 69 ~
