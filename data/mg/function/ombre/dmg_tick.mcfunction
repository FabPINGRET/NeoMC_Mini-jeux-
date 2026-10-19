# Chiffres de dégâts : montée puis disparition
scoreboard players remove @e[type=minecraft:text_display,tag=mg.oldmg] mg.olst 1
execute as @e[type=minecraft:text_display,tag=mg.oldmg,scores={mg.olst=11}] at @s run tp @s ~ ~0.9 ~
kill @e[type=minecraft:text_display,tag=mg.oldmg,scores={mg.olst=..0}]
