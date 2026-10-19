# @s lit la page 11 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p10 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page XI : On parle d'un Porteur de l'Aube. Une prophétie de vieille femme. Qu'il vienne.","color":"gray","italic":true}]
function mg:ombre/xp {n:280}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
