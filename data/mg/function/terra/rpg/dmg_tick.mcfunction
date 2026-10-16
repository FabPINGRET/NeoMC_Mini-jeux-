# Chiffres de dégâts : montée puis disparition
scoreboard players remove @e[type=minecraft:text_display,tag=mg.trdmg] mg.tvst 1
execute as @e[type=minecraft:text_display,tag=mg.trdmg,scores={mg.tvst=11}] at @s run tp @s ~ ~0.9 ~
kill @e[type=minecraft:text_display,tag=mg.trdmg,scores={mg.tvst=..0}]
