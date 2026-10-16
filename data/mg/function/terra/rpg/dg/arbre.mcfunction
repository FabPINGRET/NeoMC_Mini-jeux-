# Cœur de l'Arbre-Mère : chaque seconde pendant le combat
execute positioned 55.5 102 -177.5 run bossbar set mg:trdg0 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg0 value run data get entity @e[tag=mg.trdg_arbre,limit=1] Health
execute positioned 55.5 102 -177.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trdr0 mg.st 1
execute positioned 55.5 102 -177.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trdr0 mg.st 0
execute if score $trdr0 mg.st matches 20.. run function mg:terra/rpg/dg/arbre_reset
