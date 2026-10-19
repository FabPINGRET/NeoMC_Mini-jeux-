# Première victoire sur : Momie (bestiaire)
scoreboard players operation @s mg.olbs += #p19 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Momie","color":"gold","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:30}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
