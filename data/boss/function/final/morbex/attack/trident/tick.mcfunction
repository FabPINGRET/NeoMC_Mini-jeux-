execute as @e[tag=morbex_trident_spawner,distance=0..] at @s run tp @s ^ ^ ^0.75
execute as @e[tag=morbex_trident_spawner,distance=0..] at @s if block ~ ~ ~ black_concrete run kill @s
execute as @e[tag=morbex_trident_spawner,distance=0..] at @s if block ~ ~ ~ sculk run kill @s
execute if score morbex_trident_timer Value matches ..0 as @e[tag=morbex_trident_spawner,distance=0..] at @s positioned ~ ~8 ~ run function boss:final/morbex/attack/trident/trident 
execute if score morbex_trident_timer Value matches ..0 run scoreboard players set morbex_trident_timer Value 1
scoreboard players remove morbex_trident_timer Value 1
