# Première victoire sur : Vase putride (bestiaire)
scoreboard players operation @s mg.olbs += #p17 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Vase putride","color":"green","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:18}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
