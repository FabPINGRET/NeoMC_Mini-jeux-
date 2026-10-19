# Première victoire sur : Noyé (bestiaire)
scoreboard players operation @s mg.olbs += #p15 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Noyé","color":"dark_aqua","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:21}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
