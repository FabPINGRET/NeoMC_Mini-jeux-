# Dé double (@s) : deux dés pour ce lancer
execute unless score @s mg.mid matches 1.. run return run function mg:party/no_item
scoreboard players remove @s mg.mid 1
scoreboard players set $mdn mg.st 2
scoreboard players set $mpw mg.st 0
tellraw @a[tag=mg.mpp] [{"selector":"@s","color":"yellow"},{"text":" utilise un ","color":"gray"},{"text":"🎲🎲 DÉ DOUBLE","color":"aqua","bold":true},{"text":" !","color":"gray"}]
