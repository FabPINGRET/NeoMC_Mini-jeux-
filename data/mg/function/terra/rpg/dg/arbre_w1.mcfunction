# Cœur de l'Arbre-Mère : vague de la salle 2 / 3 (dilo, raptor)
scoreboard players set $trds0 mg.st 3
scoreboard players set $trdr0 mg.st 0
execute positioned 55.5 102 -177.5 store result score $trwn mg.st if entity @a[tag=mg.tvw,gamemode=adventure,distance=..45]
scoreboard players add $trwn mg.st 3
execute if score $trwn mg.st matches 7.. run scoreboard players set $trwn mg.st 6
tag @e[tag=mg.tvlast] remove mg.tvlast
execute if score $trwn mg.st matches 1.. positioned 53.5 76 -177.5 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 2.. positioned 54.5 76 -175.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 3.. positioned 54.5 76 -178.5 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 4.. positioned 53.5 76 -177.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 5.. positioned 54.5 76 -175.5 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 6.. positioned 54.5 76 -178.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
tag @e[tag=mg.trnew] add mg.trr
tag @e[tag=mg.trnew] add mg.trdw0
execute as @e[tag=mg.trnew,tag=mg.tvraptor] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]
function mg:terra/rpg/zone/n
tag @e[tag=mg.trnew] remove mg.trnew
execute positioned 55.5 102 -177.5 run title @a[tag=mg.tvw,distance=..45] actionbar {"text":"⚔ Cœur de l'Arbre-Mère : salle 2 / 3","color":"red","bold":true}
execute positioned 55.5 102 -177.5 run scoreboard players set @a[tag=mg.tvw,distance=..45] mg.tval 30
execute positioned 54 77 -178 run playsound minecraft:event.raid.horn hostile @a[tag=mg.tvw,distance=..45] ~ ~ ~ 0.6 1.4
