# Première victoire sur : Ours des glaces (bestiaire)
scoreboard players operation @s mg.olbs += #p11 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Ours des glaces","color":"white","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:20}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
