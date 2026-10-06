# Chute (@s = coureur) : retour au dernier checkpoint
scoreboard players add @s mg.ppf 1
scoreboard players operation $ck mg.st = @s mg.ppc
tag @s add mg.pkx
execute as @e[type=minecraft:marker,tag=mg.pkc] if score @s mg.t = $ck mg.st at @s run tp @a[tag=mg.pkx,limit=1] ~ ~ ~ -90 0
tag @s remove mg.pkx
title @s actionbar [{"text":"↺ Retour au checkpoint","color":"yellow"}]
execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.6 1.2
function mg:core/fall_heal
