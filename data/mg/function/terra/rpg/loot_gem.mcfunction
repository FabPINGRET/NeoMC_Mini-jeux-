scoreboard players operation @s mg.trsp += $g mg.st
tellraw @s [{"text":"💎 Gemme d'ambre : +","color":"light_purple"},{"score":{"name":"$g","objective":"mg.st"},"color":"light_purple","bold":true},{"text":" point(s) de caractéristique à répartir (carnet, case 6)","color":"gray"}]
execute at @s run playsound minecraft:block.amethyst_block.chime player @s ~ ~ ~ 1 1.2
