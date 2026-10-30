#LORDS --------------
execute as @n[tag=wv_lord_pivot,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~0.5 ~
execute as @n[tag=wv_lord_pivot,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-0.5 ~
execute as @n[tag=wv_lord_pivot,tag=1,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^28 run tp @n[tag=wv_lord,tag=flame,tag=!override,distance=0..] ~ 140 ~
execute as @n[tag=wv_lord_pivot,tag=1,distance=0..] at @s rotated ~90 0 positioned ^ ^ ^28 run tp @n[tag=wv_lord,tag=forest,tag=!override,distance=0..] ~ 139.5 ~
execute as @n[tag=wv_lord_pivot,tag=1,distance=0..] at @s rotated ~180 0 positioned ^ ^ ^28 run tp @n[tag=wv_lord,tag=spores,tag=!override,distance=0..] ~ 140 ~
execute as @n[tag=wv_lord_pivot,tag=1,distance=0..] at @s rotated ~270 0 positioned ^ ^ ^28 run tp @n[tag=wv_lord,tag=stone,tag=!override,distance=0..] ~ 139 ~

execute as @n[tag=wv_lord_pivot,tag=2,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^26 run tp @n[tag=wv_lord,tag=ice,tag=!override,distance=0..] ~ 138 ~
execute as @n[tag=wv_lord_pivot,tag=2,distance=0..] at @s rotated ~120 0 positioned ^ ^ ^26 run tp @n[tag=wv_lord,tag=water,tag=!override,distance=0..] ~ 138 ~
execute as @n[tag=wv_lord_pivot,tag=2,distance=0..] at @s rotated ~240 0 positioned ^ ^ ^26 run tp @n[tag=wv_lord,tag=valor,tag=!override,distance=0..] ~ 138 ~

execute as @e[tag=wv_lord,distance=0..] at @s facing entity @n[tag=wv_lord_pivot,tag=1,distance=0..] eyes run tp @s ~ ~ ~ ~ 0


execute as @n[tag=wv_lordsword,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_lord,tag=override,distance=0..] ~ ~2.5 ~



#TIMER ---------------

execute if score wv_alive bool matches 1 if score wv_lord_timer Value matches 0 run function boss:final/virus/sword_summon

execute if score wv_alive bool matches 1 if score wv_lord_timer Value matches 0.. run scoreboard players remove wv_lord_timer Value 1
