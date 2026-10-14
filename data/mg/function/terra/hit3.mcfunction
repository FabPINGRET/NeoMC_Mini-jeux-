# @s (dinosaure) touché par une impulsion
damage @s 7 minecraft:player_attack by @a[tag=mg.tvsh,limit=1]
particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.3 10
execute as @a[tag=mg.tvsh] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.4 1.5
