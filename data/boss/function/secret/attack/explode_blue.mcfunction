execute as @e[tag=sc_boss_bomb,tag=blue,distance=0..] at @s as @a[distance=..2.5,tag=mg.flw] run damage @s 24 minecraft:dragon_breath by @n[tag=sc_boss_name,distance=0..]
execute as @e[tag=sc_boss_bomb,tag=blue,distance=0..] at @s run particle dust{color:[0.000,0.000,1.000],scale:3} ~ ~1.8 ~ 0.5 0.5 0.5 0 25 normal
execute as @e[tag=sc_boss_bomb,tag=blue,distance=0..] at @s run particle explosion ~ ~1.8 ~ 1 1 1 0 5 normal
execute as @e[tag=sc_boss_bomb,tag=blue,distance=0..] at @s run playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ ~ ~ 1 1

kill @e[tag=sc_boss_bomb,tag=blue,distance=0..]
