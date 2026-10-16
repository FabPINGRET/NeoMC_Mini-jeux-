# Chaque seconde (Spinosaure en vie) : barre, laisse, phases, attaques
execute positioned 10 65 -196 run bossbar set mg:trspino players @a[tag=mg.tvw,distance=..56]
execute store result bossbar mg:trspino value run data get entity @e[tag=mg.tvspino,limit=1] Health
execute positioned 10 65 -196 unless entity @e[tag=mg.tvspino,distance=..30] run tp @e[tag=mg.tvspino] 10.5 65 -195.5
execute positioned 10 65 -196 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trsr mg.st 1
execute positioned 10 65 -196 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trsr mg.st 0
execute if score $trsr mg.st matches 15.. run return run function mg:terra/rpg/boss/spino_reset
execute as @e[tag=mg.tvspino] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..160 as @e[tag=mg.tvspino,tag=!mg.trp3] at @s run function mg:terra/rpg/boss/spino_p3
scoreboard players remove $trs1 mg.st 1
scoreboard players remove $trs2 mg.st 1
scoreboard players remove $trs3 mg.st 1
execute if score $trs1 mg.st matches ..0 as @e[tag=mg.tvspino] at @s run function mg:terra/rpg/boss/spino_sweep
execute if score $hp mg.st matches ..390 if score $trs2 mg.st matches ..0 as @e[tag=mg.tvspino] run function mg:terra/rpg/boss/spino_dive
execute if score $hp mg.st matches ..390 if score $trs3 mg.st matches ..0 run function mg:terra/rpg/boss/spino_call
