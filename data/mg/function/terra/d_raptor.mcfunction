# Slasher de vague (ici) lancé sur le colon le plus proche
function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.tvwave
execute as @e[tag=mg.tvlast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..60]
