# Première victoire sur : Wendigo des glaces (bestiaire)
scoreboard players operation @s mg.olbs2 += #p11 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Wendigo des glaces","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:300}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
