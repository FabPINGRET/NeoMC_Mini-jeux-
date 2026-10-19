# Première victoire sur : Cube de magma (bestiaire)
scoreboard players operation @s mg.olbs += #p26 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Cube de magma","color":"red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:38}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
