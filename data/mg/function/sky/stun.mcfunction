# Rival touché (@s = victime ; tireur tagué mg.skak s'il est connu) : élytres retirées 1,5 s
execute if entity @s[tag=mg.skstun] run return 0
execute if entity @s[tag=mg.skf] run return 0
tag @s add mg.skstun
scoreboard players set @s mg.skst 30
item replace entity @s armor.chest with minecraft:air
execute if entity @a[tag=mg.skak] run tellraw @a[tag=!mg.surv] [{"text":"🏹 ","color":"red"},{"selector":"@a[tag=mg.skak,limit=1]","color":"yellow"},{"text":" a abattu ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" !","color":"gray"}]
execute unless entity @a[tag=mg.skak] run tellraw @a[tag=!mg.surv] [{"text":"🏹 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" est abattu !","color":"gray"}]
title @s subtitle [{"text":"Tes élytres reviennent dans 1,5 s","color":"gray"}]
title @s title [{"text":"💫 Sonné !","color":"red","bold":true}]
playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8
execute at @s run particle minecraft:crit ~ ~1 ~ 0.4 0.6 0.4 0.3 25 force @a
execute as @a[tag=mg.skak] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1
