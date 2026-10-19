# Première victoire sur : Sorcière des marais (bestiaire)
scoreboard players operation @s mg.olbs += #p14 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Sorcière des marais","color":"dark_purple","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:22}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
