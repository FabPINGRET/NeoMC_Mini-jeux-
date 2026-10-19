# Première victoire sur : Rejeton (bestiaire)
scoreboard players operation @s mg.olbs2 += #p17 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Rejeton","color":"dark_green","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:10}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
