execute positioned ~0 ~ ~0 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute positioned ~2 ~ ~0 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute positioned ~0 ~ ~2 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
tag @e[tag=mg.trnew] add mg.trr_s
tag @e[tag=mg.trnew] add mg.trr
execute as @e[tag=mg.trnew] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]
function mg:terra/rpg/zone/s
tag @e[tag=mg.trnew] remove mg.trnew
