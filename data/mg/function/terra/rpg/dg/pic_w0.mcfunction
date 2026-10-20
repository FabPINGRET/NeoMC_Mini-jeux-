# Pic du Nid : vague de la salle 1 / 3 (raptor)
scoreboard players set $trds1 mg.st 1
scoreboard players set $trdr1 mg.st 0
execute positioned 228.5 114 24.5 store result score $trwn mg.st if entity @a[tag=mg.tvw,gamemode=adventure,distance=..53]
scoreboard players add $trwn mg.st 2
execute if score $trwn mg.st matches 7.. run scoreboard players set $trwn mg.st 6
tag @e[tag=mg.tvlast] remove mg.tvlast
execute if score $trwn mg.st matches 1.. positioned 225.5 68 21.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 2.. positioned 225.5 68 27.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 3.. positioned 228.5 68 29.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 4.. positioned 225.5 68 21.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 5.. positioned 225.5 68 27.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
execute if score $trwn mg.st matches 6.. positioned 228.5 68 29.5 run function mg:terra/dino/raptor
tag @e[tag=mg.tvlast] add mg.trnew
tag @e[tag=mg.trnew] add mg.trr
tag @e[tag=mg.trnew] add mg.trdw1
execute as @e[tag=mg.trnew,tag=mg.tvraptor] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]
function mg:terra/rpg/zone/e
tag @e[tag=mg.trnew] remove mg.trnew
execute positioned 228.5 114 24.5 run title @a[tag=mg.tvw,distance=..53] actionbar {"text":"⚔ Pic du Nid : salle 1 / 3","color":"red","bold":true}
execute positioned 228.5 114 24.5 run scoreboard players set @a[tag=mg.tvw,distance=..53] mg.tval 30
execute positioned 228 70 24 run playsound minecraft:event.raid.horn hostile @a[tag=mg.tvw,distance=..53] ~ ~ ~ 0.6 1.4
