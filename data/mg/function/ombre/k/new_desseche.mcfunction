# Première victoire sur : Archer desséché (bestiaire)
scoreboard players operation @s mg.olbs += #p21 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Archer desséché","color":"yellow","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:29}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
