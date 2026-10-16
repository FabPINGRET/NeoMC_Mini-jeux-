# Mine abandonnée : chaque seconde pendant le combat
execute positioned -224.5 65 -54.5 run bossbar set mg:trdg2 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg2 value run data get entity @e[tag=mg.trdg_mine,limit=1] Health
execute positioned -224.5 65 -54.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trdr2 mg.st 1
execute positioned -224.5 65 -54.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trdr2 mg.st 0
execute if score $trdr2 mg.st matches 20.. run function mg:terra/rpg/dg/mine_reset
