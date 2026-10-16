# Joueur touché (@s = victime ; le tireur porte mg.dlsh ; $dld = dégâts). La fin de manche est traitée par duel/shoot
scoreboard players operation @s mg.dlhp -= $dld mg.st
tag @s add mg.dlvc
execute at @s run particle minecraft:crit ~ ~1.2 ~ 0.3 0.4 0.3 0.2 25
execute at @s run playsound minecraft:entity.player.hurt master @a ~ ~ ~ 1 1
execute as @a[tag=mg.dlsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.5
execute if score $dld mg.st matches 2.. as @a[tag=mg.dlsh,limit=1] run title @s actionbar [{"text":"🎯 TÊTE !","color":"gold","bold":true}]
execute if score $dld mg.st matches ..1 if score @s mg.dlhp matches 1.. as @a[tag=mg.dlsh,limit=1] run title @s actionbar [{"text":"🎯 Touché au corps : encore une touche !","color":"aqua"}]
execute if score $dld mg.st matches ..1 if score @s mg.dlhp matches 1.. run title @s actionbar [{"text":"💥 Touché ! Encore une touche et tu perds la manche.","color":"red"}]
