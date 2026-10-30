tag @e[tag=boss_skt_ectobeam_slime,limit=70,sort=random,distance=0..] add size_1
tag @e[tag=boss_skt_ectobeam_slime,limit=70,sort=random,tag=!size_1,distance=0..] add size_2

#execute as @e[tag=boss_skt_ectobeam_slime,tag=size_1] run data modify entity @s transformation.scale set value [0.6f,0.6f,0.6f]
#execute as @e[tag=boss_skt_ectobeam_slime,tag=size_2] run data modify entity @s transformation.scale set value [0.7f,0.7f,0.7f]

#execute as @e[tag=boss_skt_ectobeam_slime,tag=size_1] run data modify entity @s attributes[0].base set value 0.6d
#execute as @e[tag=boss_skt_ectobeam_slime,tag=size_2] run data modify entity @s attributes[0].base set value 0.7d
execute as @e[tag=boss_skt_ectobeam_slime,tag=size_1,distance=0..] at @s run tp @s ~-0.025 ~-0.025 ~-0.025
execute as @e[tag=boss_skt_ectobeam_slime,tag=size_2,distance=0..] at @s run tp @s ~-0.05 ~-0.05 ~-0.05
#execute as @e[tag=boss_skt_ectobeam_slime] at @s run tp @s ~ ~200 ~


execute as @n[tag=boss_skt_ecto_tele,distance=0..] at @s run tp @s ~ -200 ~
kill @n[tag=boss_skt_ecto_tele,distance=0..]

execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:white_stained_glass run data modify entity @s glow_color_override set value 16733525
execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:lime_stained_glass run data modify entity @s glow_color_override set value 16733525

execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:white_stained_glass run data modify entity @s block_state.Name set value "red_stained_glass"
execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:lime_stained_glass run data modify entity @s block_state.Name set value "red_stained_glass"

#execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:white_stained_glass run team join NoCollideRed @s
#execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:lime_stained_glass run team join NoCollideRed @s
