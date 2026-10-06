# Dé triple (@s) : trois dés pour ce lancer
execute unless score @s mg.mit matches 1.. run return run function mg:party/no_item
scoreboard players remove @s mg.mit 1
scoreboard players set $mdn mg.st 3
scoreboard players set $mpw mg.st 0
tellraw @a[tag=mg.mpp] [{"selector":"@s","color":"yellow"},{"text":" utilise un ","color":"gray"},{"text":"🎲🎲🎲 DÉ TRIPLE","color":"light_purple","bold":true},{"text":" !","color":"gray"}]
