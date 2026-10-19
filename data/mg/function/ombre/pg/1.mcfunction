# @s lit la page 2 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p1 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page II : La Pierre-Lune protège le royaume depuis mille ans. Pourquoi la garder sous verre, quand on pourrait en boire la lumière ?","color":"gray","italic":true}]
function mg:ombre/xp {n:100}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
