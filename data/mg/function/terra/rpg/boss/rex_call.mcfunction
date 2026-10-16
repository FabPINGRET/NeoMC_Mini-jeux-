# Le Roi appelle deux slashers
scoreboard players set $trr4 mg.st 25
execute positioned 8 99 186 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trr
execute positioned -8 99 186 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trr
execute positioned 0 99 186 as @e[tag=mg.tvraptor,distance=..12] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure]
