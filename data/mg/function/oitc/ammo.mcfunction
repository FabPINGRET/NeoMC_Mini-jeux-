# Recharge automatique (@s = joueur) : sans aucune flèche pendant 5 s, une flèche est offerte
execute if items entity @s container.* minecraft:arrow run return run scoreboard players set @s mg.cd 0
execute if items entity @s weapon.offhand minecraft:arrow run return run scoreboard players set @s mg.cd 0
scoreboard players add @s mg.cd 1
execute if score @s mg.cd matches 1 run title @s actionbar [{"text":"➶ Plus de flèche : rechargement dans 5 s","color":"gray"}]
execute if score @s mg.cd matches 20 run title @s actionbar [{"text":"➶ Rechargement dans 4 s","color":"gray"}]
execute if score @s mg.cd matches 40 run title @s actionbar [{"text":"➶ Rechargement dans 3 s","color":"gray"}]
execute if score @s mg.cd matches 60 run title @s actionbar [{"text":"➶ Rechargement dans 2 s","color":"gray"}]
execute if score @s mg.cd matches 80 run title @s actionbar [{"text":"➶ Rechargement dans 1 s","color":"yellow"}]
execute if score @s mg.cd matches 100.. run function mg:oitc/reload
