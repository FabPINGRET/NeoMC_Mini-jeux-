# @s perd un ballon (touché, tombé) ; plus de ballon = éliminé
execute if score @s mg.kbl matches ..0 run return 0
scoreboard players remove @s mg.kbl 1
scoreboard players operation $me mg.st = @s mg.ri
scoreboard players operation $kbs mg.st = @s mg.kbl
scoreboard players add $kbs mg.st 1
execute as @e[type=minecraft:item_display,tag=mg.kbal] if score @s mg.ri = $me mg.st run function mg:kart/bat_burst
title @s subtitle [{"text":"🎈 Ballon crevé ! ","color":"red"},{"score":{"name":"@s","objective":"mg.kbl"},"color":"white","bold":true},{"text":" restant(s)","color":"gray"}]
title @s title ""
execute if score @s mg.kbl matches ..0 run function mg:kart/bat_out
