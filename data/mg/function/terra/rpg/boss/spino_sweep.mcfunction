# Coup de queue circulaire
scoreboard players set $trs1 mg.st 7
scoreboard players set @s mg.tvat 12
particle minecraft:sweep_attack ~ ~1 ~ 3 0.3 3 0 16
playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 2 0.5
execute as @a[tag=mg.tvw,gamemode=adventure,distance=..6] run damage @s 8 minecraft:mob_attack by @e[tag=mg.tvspino,limit=1]
