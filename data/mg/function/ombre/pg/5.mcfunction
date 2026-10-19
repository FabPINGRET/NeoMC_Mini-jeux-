# @s lit la page 6 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p5 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page VI : Sous la pyramide dort Sethkar. Je lui ai rendu la vie. Il me doit l'éternité.","color":"gray","italic":true}]
function mg:ombre/xp {n:180}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
