# La reine appelle ses petits (compys) et un dilophosaure
scoreboard players set $trs3 mg.st 22
execute positioned 16 65 -196 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trr
execute positioned 4 65 -196 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trr
execute positioned 10 65 -190 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trr
execute positioned 10 65 -202 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trr
execute positioned 10 65 -196 run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 1.2
