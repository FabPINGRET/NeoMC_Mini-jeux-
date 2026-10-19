# Première victoire sur : Vagabond gelé (bestiaire)
scoreboard players operation @s mg.olbs += #p10 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Vagabond gelé","color":"aqua","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:15}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
