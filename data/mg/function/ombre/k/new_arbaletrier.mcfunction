# Première victoire sur : Arbalétrier nain (bestiaire)
scoreboard players operation @s mg.olbs2 += #p0 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Arbalétrier nain","color":"gray","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:52}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
