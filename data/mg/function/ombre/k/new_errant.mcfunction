# Première victoire sur : Ombre errante (bestiaire)
scoreboard players operation @s mg.olbs2 += #p7 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Ombre errante","color":"dark_purple","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:70}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
