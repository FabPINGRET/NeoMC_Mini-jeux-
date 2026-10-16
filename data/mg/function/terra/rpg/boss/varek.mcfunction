# Chaque seconde (Varek en vie)
execute positioned -200 65 4 run bossbar set mg:trvarek players @a[tag=mg.tvw,distance=..48]
execute store result bossbar mg:trvarek value run data get entity @e[tag=mg.trvarek,limit=1] Health
execute positioned -200 65 4 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..56] run scoreboard players add $trvr mg.st 1
execute positioned -200 65 4 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..56] run scoreboard players set $trvr mg.st 0
execute if score $trvr mg.st matches 20.. run function mg:terra/rpg/boss/varek_reset
