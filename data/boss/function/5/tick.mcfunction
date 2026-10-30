execute as @e[tag=boss_5_debris,tag=!active,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=mg.flw] feet run tp @s ~ ~0.1 ~ ~ 0
execute as @e[tag=boss_5_debris,tag=active,distance=0..] at @s run tp @s ^ ^ ^0.5
execute as @e[tag=boss_5_debris,tag=!active,distance=0..] at @s if entity @s[y=94.5,dy=1] run tag @s add active
execute as @e[tag=boss_5_debris,distance=0..] at @s run particle dust_pillar{block_state:{Name:"minecraft:jungle_leaves",Properties:{distance:"1"}}} ~ 93 ~ 0.1 0 0.1 0.5 0 normal
execute as @e[tag=boss_5_debris,tag=active,distance=0..] at @s run playsound minecraft:block.moss.step hostile @a[distance=..15,tag=mg.flw] ~ ~ ~ 0.1 2

execute as @e[tag=boss_5_debris,tag=active,distance=0..] at @s unless block ~ ~1.5 ~ air unless block ~ ~1.5 ~ minecraft:tall_grass unless block ~ ~1.5 ~ minecraft:short_grass unless block ~ ~1.5 ~ minecraft:fern run function boss:5/debris_explode
execute as @e[tag=boss_5_debris,tag=active,distance=0..] at @s if entity @a[gamemode=!spectator,dx=0.1,dy=0.5,dz=0.1,tag=mg.flw] run function boss:5/debris_explode

execute as @e[tag=boss_skt_ecto_tele,distance=0..] at @s run tp @s ~ ~0.195 ~

execute as @e[tag=boss_skt_evoker,distance=0..] at @s if block ~ ~ ~ red_wool run kill @s
execute as @e[tag=boss_skt_evoker,distance=0..] at @s if block ~ ~ ~ iron_door run kill @s
execute as @e[tag=boss_skt_evoker,distance=0..] at @s if block ~ ~ ~ jungle_wood run kill @s

execute as @e[tag=boss_skt_evoker,distance=0..] at @s run summon evoker_fangs ^ ^ ^
#execute as @e[tag=boss_skt_evoker] at @s run summon evoker_fangs ^1.5 ^-0.05 ^-0.25
#execute as @e[tag=boss_skt_evoker] at @s run summon evoker_fangs ^-1.5 ^-0.05 ^-0.25
execute as @e[tag=boss_skt_evoker,distance=0..] at @s run summon evoker_fangs ^4 ^-0.1 ^-0.65
execute as @e[tag=boss_skt_evoker,distance=0..] at @s run summon evoker_fangs ^-4 ^-0.1 ^-0.65
execute as @e[tag=boss_skt_evoker,distance=0..] at @s run tp @s ^ ^ ^1
