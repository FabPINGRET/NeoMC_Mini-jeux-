# Chaque seconde (Roi Tyran en vie) : barre, laisse, phases, attaques
execute positioned 0 99 186 run bossbar set mg:trrex players @a[tag=mg.tvw,distance=..60]
execute store result bossbar mg:trrex value run data get entity @e[tag=mg.tvrex,limit=1] Health
execute positioned 0 99 186 unless entity @e[tag=mg.tvrex,distance=..16] run tp @e[tag=mg.tvrex] 0.5 99 186.5
execute positioned 0 99 186 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..40] run scoreboard players add $trrr mg.st 1
execute positioned 0 99 186 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..40] run scoreboard players set $trrr mg.st 0
execute if score $trrr mg.st matches 15.. run return run function mg:terra/rpg/boss/rex_reset
execute as @e[tag=mg.tvrex] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..180 as @e[tag=mg.tvrex,tag=!mg.trp3] at @s run function mg:terra/rpg/boss/rex_p3
scoreboard players remove $trr1 mg.st 1
scoreboard players remove $trr2 mg.st 1
scoreboard players remove $trr3 mg.st 1
scoreboard players remove $trr4 mg.st 1
execute if score $trr1 mg.st matches ..0 as @e[tag=mg.tvrex] at @s run function mg:terra/rpg/boss/rex_stomp
execute if score $trr2 mg.st matches ..0 as @e[tag=mg.tvrex] at @s run function mg:terra/rpg/boss/rex_roar
execute if score $hp mg.st matches ..450 if score $trr3 mg.st matches ..0 run function mg:terra/rpg/boss/rex_geysers
execute if score $hp mg.st matches ..450 if score $trr4 mg.st matches ..0 run function mg:terra/rpg/boss/rex_call
execute as @e[type=minecraft:marker,tag=mg.trgey] at @s run function mg:terra/rpg/boss/gey_tick
