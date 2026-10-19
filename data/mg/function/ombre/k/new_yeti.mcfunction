# Première victoire sur : Yéti (bestiaire)
scoreboard players operation @s mg.olbs += #p13 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Yéti","color":"white","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:27}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
