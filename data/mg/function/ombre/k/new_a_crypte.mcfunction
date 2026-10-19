# Première victoire sur : Seigneur des cryptes (bestiaire)
scoreboard players operation @s mg.olbs2 += #p9 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Seigneur des cryptes","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:150}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
