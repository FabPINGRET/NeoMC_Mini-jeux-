# @s atteint la sortie
execute unless score $state mg.st matches 2 run return 0
scoreboard players operation $js mg.st = $jtm mg.st
scoreboard players operation $js mg.st /= #20 mg.st
tellraw @a [{"text":"🌀 ","color":"light_purple"},{"selector":"@s","color":"yellow","bold":true},{"text":" sort du labyrinthe en ","color":"gray"},{"score":{"name":"$js","objective":"mg.st"},"color":"gold","bold":true},{"text":" s !","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
function mg:core/win_player
