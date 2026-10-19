# Première victoire sur : Embourbé (bestiaire)
scoreboard players operation @s mg.olbs += #p16 mg.st
tellraw @s [{"text":"📖 Bestiaire : ","color":"aqua"},{"text":"Embourbé","color":"dark_green","bold":true},{"text":" ajouté (+XP)","color":"gray"}]
function mg:ombre/xp {n:21}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1.3
