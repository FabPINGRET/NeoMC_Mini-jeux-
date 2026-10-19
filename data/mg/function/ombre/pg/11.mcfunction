# @s lit la page 12 du grimoire
scoreboard players operation $b mg.st = @s mg.olpg
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpg += #p11 mg.st
tellraw @s [{"text":"📕 Grimoire de Malveth, ","color":"dark_purple","bold":true},{"text":"Page XII : Si quelqu'un lit ces lignes, c'est que je suis tombé. Pardonne-moi, Liora. Tu avais raison.","color":"gray","italic":true}]
function mg:ombre/xp {n:300}
execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8
