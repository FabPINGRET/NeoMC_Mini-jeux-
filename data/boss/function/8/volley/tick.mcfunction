execute as @n[tag=frostbyte_volley_pos,distance=0..] at @s run tp @n[tag=frostbyte_volley,distance=0..] ~ ~ ~

execute unless score boss:fs BossHealth matches 0..4 as @n[tag=frostbyte_volley_pos,tag=beam,distance=0..] at @s run tp @s ^ ^ ^0.5
execute if score boss:fs BossHealth matches 0..4 as @n[tag=frostbyte_volley_pos,tag=beam,distance=0..] at @s run tp @s ^ ^ ^0.35

execute unless score boss:fs BossHealth matches 0..4 as @n[tag=frostbyte_volley_pos,tag=unpowered,distance=0..] at @s run tp @s ^ ^ ^0.35
execute if score boss:fs BossHealth matches 0..4 as @n[tag=frostbyte_volley_pos,tag=unpowered,distance=0..] at @s run tp @s ^ ^ ^0.2
execute as @n[tag=frostbyte_volley_pos,tag=powered,distance=0..] at @s facing entity @n[tag=frostbyte_head,distance=0..] eyes run tp @s ^ ^ ^1

execute as @n[tag=frostbyte_volley_pos,tag=beam,distance=0..] at @s unless entity @n[tag=frostbyte_head,distance=..15] run function boss:8/volley/unpowered

execute as @n[tag=frostbyte_volley_pos,tag=unpowered,distance=0..] at @s unless block ~ ~ ~ air unless block ~ ~ ~ light run function boss:8/volley/failed
execute as @n[tag=frostbyte_volley_pos,tag=unpowered,distance=0..] at @s positioned ~ ~-1 ~ if entity @n[type=lightning_bolt,distance=..2] run function boss:8/volley/powered

execute as @n[tag=frostbyte_volley_pos,tag=powered,distance=0..] at @s if entity @n[tag=frostbyte_head,distance=..2] run function boss:8/volley/returned

execute as @n[tag=frostbyte_volley_pos,distance=0..] at @s run particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:1,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.1 0.1 0.1 0 1
execute as @n[tag=frostbyte_volley_pos,tag=beam,distance=0..] at @s run particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:2,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.2 0.2 0.2 0 1
