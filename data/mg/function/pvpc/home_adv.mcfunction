advancement revoke @s only mg:pvpc_home
tag @s add mg.pgw
execute unless entity @s[tag=mg.pvpc] run return 0
execute if score @s mg.phc matches 1.. run return 0
scoreboard players set @s mg.phc 100
scoreboard players set @s mg.pdt 0
tellraw @s {"text":"🏠 Retour au spawn dans 5 s… ne prends pas de coup !","color":"yellow"}
