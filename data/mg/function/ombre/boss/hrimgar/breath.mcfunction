# Hrimgar, le géant du givre : breath
playsound minecraft:entity.breeze.wind_burst hostile @a ~ ~ ~ 2 0.5
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^2 run particle minecraft:snowflake ^ ^ ^5.0 1 0.6 3.3 0.04 120 force
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^5.0 as @a[tag=mg.olw,gamemode=adventure,distance=..6.0] run damage @s 8 minecraft:mob_attack by @e[tag=mg.olb_hrimgar,limit=1]
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^5.0 run effect give @a[tag=mg.olw,gamemode=adventure,distance=..6.0] minecraft:slowness 4 2
