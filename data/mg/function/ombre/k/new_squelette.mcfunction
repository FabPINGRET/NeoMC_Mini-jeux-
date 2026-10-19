# Première victoire sur : Squelette (bestiaire)
scoreboard players operation @s mg.olbs += #p4 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Squelette","color":"white","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:10}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
