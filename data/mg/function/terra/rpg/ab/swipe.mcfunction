# @s (herbivore défensif) : coup de queue / de cornes sur la cible qui le provoque
tag @a remove mg.trtg
execute on target if entity @s[tag=mg.tvw] run tag @s add mg.trtg
execute unless entity @a[tag=mg.trtg,distance=..4.5] run return 0
scoreboard players set @s mg.tvat 10
damage @p[tag=mg.trtg] 6 minecraft:mob_attack by @s
playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 1 0.6
particle minecraft:sweep_attack ~ ~1 ~ 1 0.4 1 0 4
tag @a remove mg.trtg
