# Ignarok, dragon de feu : tail
scoreboard players set @s mg.olat 8
particle minecraft:sweep_attack ~ ~1 ~ 3 0.4 3 0 20
playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 2 0.4
execute as @a[tag=mg.olw,gamemode=adventure,distance=..6] run damage @s 9 minecraft:mob_attack by @e[tag=mg.olb_ignarok,limit=1]
