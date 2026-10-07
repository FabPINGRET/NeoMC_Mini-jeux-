# Bill Balle : vers le prochain point de passage, vite, sans gravité ; renverse les karts touchés
scoreboard players operation $ki mg.st = @s mg.kcp
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run function mg:kart/bill_step
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s on passengers unless entity @s[type=minecraft:player] run rotate @s ~ 0
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^2.6 ^-5.5 rotated ~ 16 run tp @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] ~ ~ ~ ~ ~
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^0.6 ^-1.6 run particle minecraft:flame ~ ~ ~ 0.2 0.2 0.2 0.05 8
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^0.6 ^-2 run particle minecraft:large_smoke ~ ~ ~ 0.2 0.2 0.2 0.02 3
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s as @e[type=minecraft:block_display,tag=mg.kart,tag=!mg.kk,distance=..2.4] run function mg:kart/owner_hit
execute store result score @s mg.khd run data get entity @e[type=minecraft:block_display,tag=mg.kk,limit=1] Rotation[0] 10
scoreboard players set @s mg.ksp 100
scoreboard players set @s mg.kvy 0
