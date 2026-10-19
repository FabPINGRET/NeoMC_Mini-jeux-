# Première victoire sur : Cultiste de Malveth (bestiaire)
scoreboard players operation @s mg.olbs2 += #p8 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Cultiste de Malveth","color":"dark_purple","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:75}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
