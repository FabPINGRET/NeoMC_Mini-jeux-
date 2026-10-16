# Tube de lave : chaque seconde pendant le combat
execute positioned -23.5 90 186.5 run bossbar set mg:trdg3 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg3 value run data get entity @e[tag=mg.trdg_tube,limit=1] Health
execute positioned -23.5 90 186.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trdr3 mg.st 1
execute positioned -23.5 90 186.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trdr3 mg.st 0
execute if score $trdr3 mg.st matches 20.. run function mg:terra/rpg/dg/tube_reset
