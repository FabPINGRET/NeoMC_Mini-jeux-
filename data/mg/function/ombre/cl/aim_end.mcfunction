# fin du rayon de visée : zone de pluie (4 volées)
execute align xyz positioned ~0.5 ~1 ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olrain","mg.olnn"]}
scoreboard players set @e[tag=mg.olnn] mg.olst 4
scoreboard players operation @e[tag=mg.olnn] mg.olo = $own mg.st
execute store result score @e[tag=mg.olnn] mg.olpw run scoreboard players get $d mg.st
tag @e[tag=mg.olnn] remove mg.olnn
