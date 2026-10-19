# Groupe de la région sw : une espèce tirée au sort, 1 à 3 individus
execute store result score $r mg.st run random value 0..4
execute store result score $g mg.st run random value 1..3
execute if score $r mg.st matches 0 run function mg:ombre/m/grp_one {k:"chevnoir"}
execute if score $r mg.st matches 1 run function mg:ombre/m/grp_one {k:"necro"}
execute if score $r mg.st matches 2 run function mg:ombre/m/grp_one {k:"spectre"}
execute if score $r mg.st matches 3 run function mg:ombre/m/grp_one {k:"errant"}
execute if score $r mg.st matches 4 run function mg:ombre/m/grp_one {k:"cultiste"}
tag @e[tag=mg.olnew] add mg.olr_sw
execute if predicate mg:tv_c10 as @e[tag=mg.olnew,sort=random,limit=1] run function mg:ombre/m/elite
execute as @e[tag=mg.olnew,tag=mg.olprov] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..64]
tag @e[tag=mg.olnew] remove mg.olnew
