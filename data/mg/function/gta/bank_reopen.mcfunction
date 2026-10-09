# Les coffres sont de nouveau pleins
execute as @e[type=minecraft:text_display,tag=mg.gbkl] run data merge entity @s {text:{"text":"💰 Coffres : accroupi + arme pendant 15 s","color":"gold"}}
tellraw @a[tag=mg.gtw] {"text":"🏦 Les coffres de la banque sont de nouveau pleins…","color":"gold"}
