# Meute de 2 ou 3 slashers ici, lancée sur le colon le plus proche hors de la colonie
tag @e[tag=mg.tvpk] remove mg.tvpk
execute store result score $tvn mg.st run random value 2..4
function mg:terra/pack_one
execute as @e[tag=mg.tvpk] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvout,gamemode=adventure,distance=..70]
tag @e[tag=mg.tvpk] remove mg.tvpk
