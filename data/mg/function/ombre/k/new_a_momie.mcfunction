# Première victoire sur : Momie royale (bestiaire)
scoreboard players operation @s mg.olbs2 += #p13 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Momie royale","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:450}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
