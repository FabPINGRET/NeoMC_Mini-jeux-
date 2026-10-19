# Première victoire sur : Forgeron calciné (bestiaire)
scoreboard players operation @s mg.olbs2 += #p14 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Forgeron calciné","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:525}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
