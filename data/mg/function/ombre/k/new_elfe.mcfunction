# Première victoire sur : Elfe noir (bestiaire)
scoreboard players operation @s mg.olbs += #p8 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Elfe noir","color":"dark_purple","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:13}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
