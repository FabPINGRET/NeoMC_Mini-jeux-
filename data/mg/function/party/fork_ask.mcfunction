# Embranchement : le joueur choisit sa route (15 s, sinon au hasard)
scoreboard players set $mph mg.st 6
scoreboard players set $mpw mg.st 300
title @s title [{"text":"⇆ EMBRANCHEMENT","color":"white","bold":true}]
title @s subtitle [{"text":"Clique sur ta route dans le chat","color":"yellow"}]
function mg:party/fork_info
execute at @s run playsound minecraft:block.note_block.chime master @a[tag=mg.mpp] ~ ~ ~ 1 1
