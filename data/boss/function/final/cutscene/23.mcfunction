playsound minecraft:entity.wither.death hostile @a[tag=mg.flw] -12384 123 355 5 0.5

kill @e[tag=wv_morbex_tumor,distance=0..]
#Stop transforming tick
setblock -12346 43 344 air

execute at @n[tag=lord_morbex_stand,distance=0..] run function boss:final/virus/model/cutscene_sword
execute at @n[tag=wv_model_sword,tag=origin,distance=0..] run particle minecraft:soul_fire_flame ~ ~4 ~ 0.3 2 0.3 0.7 750

execute as @n[tag=lord_morbex_stand,distance=0..] at @s run tp @s ~ 60 ~

schedule function floaty:sched/boss/final/cutscene/24 5s replace

#","color":"white"},{"text":"
