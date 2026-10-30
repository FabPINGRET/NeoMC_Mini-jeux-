function boss:5/bare_anim
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run fill ~-1 ~ ~-1 ~1 ~5 ~1 air
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run clone -10183 72 457 -10181 79 459 ~-1 ~ ~-1
schedule function floaty:sched/boss/5/tail_poison_attack 1.5s replace
