function boss:secret/rand
execute as @e[tag=sc_boss_rand,limit=1,sort=random,distance=0..] at @s run tp @n[tag=sc_boss_dest,distance=0..] ~ 184 ~
