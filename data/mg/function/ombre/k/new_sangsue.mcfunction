# Première victoire sur : Sangsue géante (bestiaire)
scoreboard players operation @s mg.olbs += #p18 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Sangsue géante","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:18}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
