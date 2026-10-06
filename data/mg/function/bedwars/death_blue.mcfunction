# Mort d'un BLEU (@s) — perd tout son inventaire
scoreboard players set @s mg.deaths 0
clear @s
# Respawn forcé : le spawn d'équipe est réimposé à CHAQUE mort (un clic sur un lit ou un lit cassé ne le change plus)
execute if score $bed_blue mg.st matches 1 run spawnpoint @s 31 64 1200
execute if score $bed_blue mg.st matches 0 run spawnpoint @s 0 85 1200
tag @s add mg.rsp
execute if score $bed_blue mg.st matches 1 run tp @s 31.5 64 1200.5 facing 0 64 1200
execute if score $bed_blue mg.st matches 1 run function mg:bedwars/kit_blue
execute if score $bed_blue mg.st matches 1 run effect give @s minecraft:resistance 3 4 true
execute if score $bed_blue mg.st matches 1 run title @s actionbar [{"text":"Ton lit te ramène — ressources et achats perdus !","color":"yellow"}]
execute if score $bed_blue mg.st matches 0 run function mg:core/eliminate
execute if score $bed_blue mg.st matches 0 unless entity @a[team=mg_blue,tag=mg.play] run tellraw @a [{"text":"☠ L'équipe ","color":"gray"},{"text":"BLEUE","color":"blue","bold":true},{"text":" est éliminée !","color":"gray"}]
