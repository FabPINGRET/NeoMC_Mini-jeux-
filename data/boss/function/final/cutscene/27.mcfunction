function music:boss_intro

execute as @n[tag=wv_model_crown,tag=origin,distance=0..] at @s run tp @s ~ ~1.5 ~
execute as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~1.5 ~
execute as @n[tag=wv_model_smallarm,tag=origin,distance=0..] at @s run tp @s ~ ~1.5 ~
execute as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s run tp @s ~ ~1.5 ~

schedule function floaty:sched/boss/final/cutscene/28 10t replace

#","color":"white"},{"text":"
