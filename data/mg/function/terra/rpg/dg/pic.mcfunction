# Pic du Nid : chaque seconde pendant le combat
execute positioned 228.5 114 24.5 run bossbar set mg:trdg1 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg1 value run data get entity @e[tag=mg.trdg_pic,limit=1] Health
execute positioned 228.5 114 24.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trdr1 mg.st 1
execute positioned 228.5 114 24.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trdr1 mg.st 0
execute if score $trdr1 mg.st matches 20.. run function mg:terra/rpg/dg/pic_reset
