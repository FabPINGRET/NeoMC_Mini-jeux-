# @s lit la page 14 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p13 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page XIV : Trois coffres par région, avait dit le vieux roi, pour que les braves ne manquent jamais de rien.","color":"gray","italic":true}]
function mg:ombre/xp {n:340}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
