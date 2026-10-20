# Adversaire touché (@s = victime ; le tireur porte mg.tmsh ; $tmd = dégâts). Le frag est traité par tdm/shoot
scoreboard players operation @s mg.tmhp -= $tmd mg.st
tag @s add mg.tmvc
execute at @s run particle minecraft:crit ~ ~1.2 ~ 0.3 0.4 0.3 0.2 25
execute at @s run playsound minecraft:entity.player.hurt master @a ~ ~ ~ 1 1
execute as @a[tag=mg.tmsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.5
execute if score $tmd mg.st matches 2.. as @a[tag=mg.tmsh,limit=1] run title @s actionbar [{"text":"🎯 TÊTE !","color":"gold","bold":true}]
execute if score $tmd mg.st matches ..1 if score @s mg.tmhp matches 1.. as @a[tag=mg.tmsh,limit=1] run title @s actionbar [{"text":"🎯 Touché au corps : encore une touche !","color":"aqua"}]
execute if score $tmd mg.st matches ..1 if score @s mg.tmhp matches 1.. run title @s actionbar [{"text":"💥 Touché ! Encore une touche et tu perds une vie.","color":"red"}]
