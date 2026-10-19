# @s lit la page 1 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p0 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page I : J'étais l'apprenti le plus doué de l'Académie de Havreclair. Ils disaient que mon talent était une bénédiction.","color":"gray","italic":true}]
function mg:ombre/xp {n:80}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
