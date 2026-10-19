# Première victoire sur : Brute calcinée (bestiaire)
scoreboard players operation @s mg.olbs += #p27 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Brute calcinée","color":"dark_red","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:48}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
