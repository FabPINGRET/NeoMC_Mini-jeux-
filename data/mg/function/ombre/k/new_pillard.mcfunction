# Première victoire sur : Pillard du désert (bestiaire)
scoreboard players operation @s mg.olbs += #p23 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Pillard du désert","color":"gold","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:32}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
