# Première victoire sur : Scorpion des sables (bestiaire)
scoreboard players operation @s mg.olbs += #p20 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Scorpion des sables","color":"gold","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:30}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
