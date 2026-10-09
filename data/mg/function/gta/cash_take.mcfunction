# @s : liasse ramassée par le joueur le plus proche (montant mg.gpc)
scoreboard players operation $gcv mg.st = @s mg.gpc
execute as @p[tag=mg.gtw] run function mg:gta/cash_gain
execute at @s run playsound minecraft:entity.player.levelup player @a ~ ~ ~ 0.8 1.4
kill @s
