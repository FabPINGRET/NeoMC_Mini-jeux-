# Première victoire sur : Nain renégat (bestiaire)
scoreboard players operation @s mg.olbs += #p29 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Nain renégat","color":"gray","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:55}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
