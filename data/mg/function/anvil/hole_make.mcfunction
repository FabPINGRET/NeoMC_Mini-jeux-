# Prépare un trou 3x3 (position d'exécution = centre) : avertissement rouge 2 s, ouvert 6 s, puis le sol se referme
summon minecraft:marker ~ 81 ~ {Tags:["mg.hl","mg.hln"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.hln] mg.t 220
tag @e[type=minecraft:marker,tag=mg.hln] remove mg.hln
fill ~-1 80 ~-1 ~1 80 ~1 minecraft:red_concrete replace minecraft:smooth_stone
playsound minecraft:block.note_block.bass master @a ~ 81 ~ 1 0.5
