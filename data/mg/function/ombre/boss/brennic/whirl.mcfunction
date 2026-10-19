# Brennic, seigneur des brigands : whirl
particle minecraft:sweep_attack ~ ~1 ~ 2.5 0.4 2.5 0 20
playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 2 0.5
scoreboard players set @s mg.olat 10
execute as @a[tag=mg.olw,gamemode=adventure,distance=..4.5] run damage @s 8 minecraft:mob_attack by @e[tag=mg.olb_brennic,limit=1]
