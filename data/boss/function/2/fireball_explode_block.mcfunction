execute as @e[tag=ck_fireball,distance=0..] at @s run particle minecraft:explosion ~ ~2 ~ 1 1 1 0 10 force
execute as @e[tag=ck_fireball,distance=0..] at @s run particle minecraft:lava ~ ~2 ~ 1 1 1 0 20 force

execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_1,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/1
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_2,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/2
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_3,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/3
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_4,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/4
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_5,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/5
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_6,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/6
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_7,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/7
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_8,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/8
execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~-2 ~ ~-2 if entity @e[tag=tentacle_9,dx=4,dy=4,dz=4] run function boss:2/tentacle_hit/9

execute as @e[tag=ck_fireball,distance=0..] at @s run playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ ~ ~

kill @e[tag=ck_fireball,distance=0..]
tag @a[tag=mg.flw] remove ck_fireball_target

setblock -10124 138 -57 redstone_block
