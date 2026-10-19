# @s lit la page 9 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p8 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page IX : Les nains de Khazgarde ont scellé leur porte. Mon colosse de runes gardera leurs trésors pour moi.","color":"gray","italic":true}]
function mg:ombre/xp {n:240}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
