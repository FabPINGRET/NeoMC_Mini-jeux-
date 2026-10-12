scoreboard players add $tht mg.st 1
execute if score $tht mg.st matches ..19 run return 0
scoreboard players set $tht mg.st 0
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/fx
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/fx
