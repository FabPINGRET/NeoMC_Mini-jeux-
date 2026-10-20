# Tube de lave : vague de la salle 2 / 3 (raptor, compy)
scoreboard players set $trds3 mg.st 3
scoreboard players set $trdr3 mg.st 0
execute positioned -23.5 90 186.5 store result score $trwn mg.st if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44]
scoreboard players add $trwn mg.st 3
execute if score $trwn mg.st matches 7.. run scoreboard players set $trwn mg.st 6
tag @e[tag=mg.tvlast] remove mg.tvlast
execute if score $trwn mg.st matches 1.. positioned -43.5 89 182.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 2.. positioned -41.5 89 183.5 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 3.. positioned -39.5 89 184.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 4.. positioned -43.5 89 182.5 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 5.. positioned -41.5 89 183.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 6.. positioned -39.5 89 184.5 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trnew
tag @e[tag=mg.trnew] add mg.trr
tag @e[tag=mg.trnew] add mg.trdw3
execute as @e[tag=mg.trnew,tag=mg.tvraptor] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]
execute as @e[tag=mg.trnew,tag=mg.tvcompy] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]
function mg:terra/rpg/zone/s
tag @e[tag=mg.trnew] remove mg.trnew
execute positioned -23.5 90 186.5 run title @a[tag=mg.tvw,distance=..44] actionbar {"text":"⚔ Tube de lave : salle 2 / 3","color":"red","bold":true}
execute positioned -23.5 90 186.5 run scoreboard players set @a[tag=mg.tvw,distance=..44] mg.tval 30
execute positioned -42 90 183 run playsound minecraft:event.raid.horn hostile @a[tag=mg.tvw,distance=..44] ~ ~ ~ 0.6 1.4
