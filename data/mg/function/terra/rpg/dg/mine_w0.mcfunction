# Mine abandonnée : vague de la salle 1 / 3 (raptor, dilo)
scoreboard players set $trds2 mg.st 1
scoreboard players set $trdr2 mg.st 0
execute positioned -224.5 65 -54.5 store result score $trwn mg.st if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44]
scoreboard players add $trwn mg.st 2
execute if score $trwn mg.st matches 7.. run scoreboard players set $trwn mg.st 6
tag @e[tag=mg.tvlast] remove mg.tvlast
execute if score $trwn mg.st matches 1.. positioned -210.5 65 -55.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 2.. positioned -202.5 65 -53.5 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 3.. positioned -208.5 65 -53.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 4.. positioned -210.5 65 -55.5 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 5.. positioned -202.5 65 -53.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 6.. positioned -208.5 65 -53.5 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trnew
tag @e[tag=mg.trnew] add mg.trr
tag @e[tag=mg.trnew] add mg.trdw2
execute as @e[tag=mg.trnew,tag=mg.tvraptor] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]
function mg:terra/rpg/zone/w
tag @e[tag=mg.trnew] remove mg.trnew
execute positioned -224.5 65 -54.5 run title @a[tag=mg.tvw,distance=..44] actionbar {"text":"⚔ Mine abandonnée : salle 1 / 3","color":"red","bold":true}
execute positioned -224.5 65 -54.5 run scoreboard players set @a[tag=mg.tvw,distance=..44] mg.tval 30
execute positioned -207 66 -55 run playsound minecraft:event.raid.horn hostile @a[tag=mg.tvw,distance=..44] ~ ~ ~ 0.6 1.4
