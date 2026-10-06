# Mort d'un JAUNE (@s) — perd tout son inventaire
scoreboard players set @s mg.deaths 0
clear @s
# Respawn forcé : le spawn d'équipe est réimposé à CHAQUE mort (un clic sur un lit ou un lit cassé ne le change plus)
execute if score $bed_yellow mg.st matches 1 run spawnpoint @s 0 64 1232
execute if score $bed_yellow mg.st matches 0 run spawnpoint @s 0 85 1200
tag @s add mg.rsp
execute if score $bed_yellow mg.st matches 1 run tp @s 0.5 64 1232.5 facing 0 64 1200
execute if score $bed_yellow mg.st matches 1 run function mg:bedwars/kit_yellow
execute if score $bed_yellow mg.st matches 1 run effect give @s minecraft:resistance 3 4 true
execute if score $bed_yellow mg.st matches 1 run title @s actionbar [{"text":"Ton lit te ramène — ressources et achats perdus !","color":"yellow"}]
execute if score $bed_yellow mg.st matches 0 run function mg:core/eliminate
execute if score $bed_yellow mg.st matches 0 unless entity @a[team=mg_yellow,tag=mg.play] run tellraw @a [{"text":"☠ L'équipe ","color":"gray"},{"text":"JAUNE","color":"yellow","bold":true},{"text":" est éliminée !","color":"gray"}]
