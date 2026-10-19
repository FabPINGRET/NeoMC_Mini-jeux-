# Première victoire sur : Brigand (bestiaire)
scoreboard players operation @s mg.olbs += #p1 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Brigand","color":"red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:10}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
