execute as @e[tag=ck_fireball,distance=0..] at @s facing entity @p[tag=ck_fireball_target,tag=mg.flw] feet run tp @s ~ ~ ~ ~ ~
execute as @e[tag=ck_fireball,distance=0..] at @s run tp @s ^ ^ ^0.3
execute as @e[tag=ck_fireball,distance=0..] at @s run particle minecraft:small_flame ~ ~1.75 ~ 0.3 0.3 0.3 0 2 force
execute as @e[tag=ck_fireball,distance=0..] at @s run particle minecraft:lava ~ ~1.75 ~ 0.2 0.2 0.2 0 1 force

execute as @e[tag=ck_fireball,distance=0..] at @s unless block ~ ~1.5 ~ #hb_passthrough run function boss:2/fireball_explode_block

execute as @e[tag=ck_fireball,distance=0..] at @s unless block ~0.5 ~1.5 ~ #hb_passthrough run function boss:2/fireball_explode_block
execute as @e[tag=ck_fireball,distance=0..] at @s unless block ~-0.5 ~1.5 ~ #hb_passthrough run function boss:2/fireball_explode_block
execute as @e[tag=ck_fireball,distance=0..] at @s unless block ~ ~1.5 ~0.5 #hb_passthrough run function boss:2/fireball_explode_block
execute as @e[tag=ck_fireball,distance=0..] at @s unless block ~ ~1.5 ~-0.5 #hb_passthrough run function boss:2/fireball_explode_block

execute as @e[tag=ck_fireball,distance=0..] at @s positioned ~ ~1.5 ~ if entity @a[gamemode=!spectator,dx=0.1,dy=0.1,dz=0.1,tag=mg.flw] run function boss:2/fireball_explode

execute if entity @a[tag=ck_fireball_target,tag=!bossroom,tag=mg.flw] run function boss:2/fireball_explode
