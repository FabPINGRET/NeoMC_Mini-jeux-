# Première victoire sur : Tisseuse (bestiaire)
scoreboard players operation @s mg.olbs += #p6 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Tisseuse","color":"dark_aqua","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:10}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
