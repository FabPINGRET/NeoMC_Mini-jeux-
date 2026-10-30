execute as @n[tag=lord_morbex_stand,distance=0..] at @s positioned ^ ^ ^4 run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["morbex_trident_spawner","new"]}
execute as @n[tag=morbex_trident_spawner,tag=new,distance=0..] at @s rotated as @n[tag=lord_morbex_stand,distance=0..] run tp @s ~ ~ ~ ~ 0
tag @e[tag=morbex_trident_spawner,distance=0..] remove new
