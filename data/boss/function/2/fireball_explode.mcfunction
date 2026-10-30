execute as @e[tag=ck_fireball,distance=0..] at @s run particle minecraft:explosion ~ ~2 ~ 1 1 1 0 10 force
execute as @e[tag=ck_fireball,distance=0..] at @s run particle minecraft:lava ~ ~2 ~ 1 1 1 0 20 force

execute as @e[tag=ck_fireball,distance=0..] at @s run playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ ~ ~

execute as @e[tag=ck_fireball,distance=0..] at @s as @a[distance=..3,tag=mg.flw] run damage @s 8 minecraft:fireball by @e[tag=ck_fireball,limit=1,distance=0..]

kill @e[tag=ck_fireball,distance=0..]
tag @a[tag=mg.flw] remove ck_fireball_target

setblock -10124 138 -57 redstone_block
