# Touche un plafond en montant
scoreboard players operation @s mg.gfy -= $gfd mg.st
execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy
scoreboard players set @s mg.gfv 0
