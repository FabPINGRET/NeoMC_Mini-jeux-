# @s : marqueur — attente du service (robot : 1,5 s ; joueur : clic droit, ou service automatique après 10 s)
scoreboard players add @s mg.tnt 1
scoreboard players operation $tnside mg.st = @s mg.tnl
execute if score @s mg.tnt matches 30.. as @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] if score @s mg.tns = $tnside mg.st at @s run return run function mg:tennis/toss
execute if score @s mg.tnt matches 200.. as @a[tag=mg.tnk] if score @s mg.tns = $tnside mg.st at @s run return run function mg:tennis/toss
