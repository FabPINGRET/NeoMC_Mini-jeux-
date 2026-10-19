# Piliers : rallumés au bout de 30 s
scoreboard players remove @e[tag=mg.olpill,scores={mg.olst=1..}] mg.olst 1
execute as @e[tag=mg.olpill,scores={mg.olst=0}] at @s if block ~ ~4 ~ minecraft:black_stained_glass run setblock ~ ~4 ~ minecraft:light_blue_stained_glass
