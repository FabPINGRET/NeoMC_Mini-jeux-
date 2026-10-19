# Première victoire sur : Gardien des âmes (bestiaire)
scoreboard players operation @s mg.olbs2 += #p16 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Gardien des âmes","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:700}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
