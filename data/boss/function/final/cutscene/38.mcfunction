execute as @n[tag=wv_model_crown,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~
execute as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~
execute as @n[tag=wv_model_smallarm,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~
execute as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s run tp @s ~ ~1 ~

fill -12389 123 350 -12379 134 360 light[level=15]
clone -12389 24 350 -12379 27 360 -12389 123 350
function boss:final/arena/reset_light

schedule function floaty:sched/boss/final/cutscene/39 10t replace

#","color":"white"},{"text":"
