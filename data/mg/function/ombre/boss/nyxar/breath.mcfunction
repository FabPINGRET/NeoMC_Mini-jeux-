# Nyxar, dragon de la Lune Noire : breath
scoreboard players set @s mg.olat 14
playsound minecraft:entity.ender_dragon.shoot hostile @a ~ ~ ~ 2 0.5
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^2 run particle minecraft:dragon_breath ^ ^ ^6.0 1 0.6 4.0 0.04 120 force
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^6.0 as @a[tag=mg.olw,gamemode=adventure,distance=..7.0] run damage @s 14 minecraft:mob_attack by @e[tag=mg.olb_nyxar,limit=1]
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^6.0 run effect give @a[tag=mg.olw,gamemode=adventure,distance=..7.0] minecraft:wither 3 1
