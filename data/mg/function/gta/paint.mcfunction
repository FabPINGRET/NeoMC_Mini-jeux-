# @s : peinture aléatoire de la carrosserie de son véhicule (mg.gveh)
scoreboard players operation $gv mg.st = @s mg.gveh
execute unless score @s mg.gveh matches 1.. run return run title @s actionbar {"text":"🎨 Achète d'abord un véhicule (concession) ou sors-en un du garage","color":"red"}
execute store result score $gr mg.st run random value 0..11
execute if score $gr mg.st matches 0 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:red_concrete"}}
execute if score $gr mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:orange_concrete"}}
execute if score $gr mg.st matches 2 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:yellow_concrete"}}
execute if score $gr mg.st matches 3 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:lime_concrete"}}
execute if score $gr mg.st matches 4 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:cyan_concrete"}}
execute if score $gr mg.st matches 5 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:blue_concrete"}}
execute if score $gr mg.st matches 6 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:purple_concrete"}}
execute if score $gr mg.st matches 7 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:magenta_concrete"}}
execute if score $gr mg.st matches 8 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:black_concrete"}}
execute if score $gr mg.st matches 9 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:white_concrete"}}
execute if score $gr mg.st matches 10 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:pink_concrete"}}
execute if score $gr mg.st matches 11 as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {block_state:{Name:"minecraft:gray_concrete"}}
playsound minecraft:item.dye.use player @s ~ ~ ~ 1 1
title @s actionbar {"text":"🎨 Nouvelle peinture !","color":"light_purple","bold":true}
scoreboard players set @s mg.gal 30
