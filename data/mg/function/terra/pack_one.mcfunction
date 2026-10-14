function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.tvpk
scoreboard players remove $tvn mg.st 1
execute if score $tvn mg.st matches 1.. run function mg:terra/pack_one
