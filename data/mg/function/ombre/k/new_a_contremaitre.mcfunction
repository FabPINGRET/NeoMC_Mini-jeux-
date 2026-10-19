# Première victoire sur : Contremaître maudit (bestiaire)
scoreboard players operation @s mg.olbs2 += #p15 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Contremaître maudit","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:600}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
