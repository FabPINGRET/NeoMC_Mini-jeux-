# @s lit la page 10 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p9 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page X : Nyxar est né de l'éclat que j'ai gardé. Un dragon fait de nuit. Mon enfant.","color":"gray","italic":true}]
function mg:ombre/xp {n:260}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
