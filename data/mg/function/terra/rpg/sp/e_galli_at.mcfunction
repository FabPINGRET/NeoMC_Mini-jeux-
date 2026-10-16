execute positioned ~0 ~ ~0 run function mg:terra/dino/galli
tag @e[tag=mg.tvlast] add mg.trnew
execute positioned ~2 ~ ~0 run function mg:terra/dino/galli
tag @e[tag=mg.tvlast] add mg.trnew
execute positioned ~0 ~ ~2 run function mg:terra/dino/galli
tag @e[tag=mg.tvlast] add mg.trnew
tag @e[tag=mg.trnew] add mg.trr_e
tag @e[tag=mg.trnew] add mg.trr
function mg:terra/rpg/zone/e
tag @e[tag=mg.trnew] remove mg.trnew
