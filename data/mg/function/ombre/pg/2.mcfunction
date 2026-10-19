# @s lit la page 3 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p2 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page III : Les elfes de Sylvanor m'ont chassé de leurs bois. Ils ont senti l'ombre en moi avant moi-même.","color":"gray","italic":true}]
function mg:ombre/xp {n:120}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
