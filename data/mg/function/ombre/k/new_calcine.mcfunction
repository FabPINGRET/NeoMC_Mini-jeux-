# Première victoire sur : Chevalier calciné (bestiaire)
scoreboard players operation @s mg.olbs += #p28 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Chevalier calciné","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:47}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
