# @s = joueur : marqueurs « bloc courant » (mg.trm) et « dernier mur posé » (mg.trp)
execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.trm","mg.trnew"]}
execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.trp","mg.trnew"]}
scoreboard players operation @e[tag=mg.trnew] mg.trc = @s mg.trc
tag @e[tag=mg.trnew] remove mg.trnew
scoreboard players set @s mg.trs 0
