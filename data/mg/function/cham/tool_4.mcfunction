# Leurre : une copie du corps, là où on est
execute unless score @s mg.cmdl matches 1.. run return run title @s actionbar {"text":"👥 Plus de leurre pour cette manche","color":"gray"}
scoreboard players remove @s mg.cmdl 1
scoreboard players add $cmdc mg.st 1
scoreboard players operation $cmid mg.st = @s mg.cmid
execute as @e[type=minecraft:block_display,tag=mg.cmd] if score @s mg.cmid = $cmid mg.st at @s run function mg:cham/decoy_part
execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.cmdi","mg.cmnew"],width:0.9f,height:1.6f}
scoreboard players operation @e[tag=mg.cmnew] mg.cmdn = $cmdc mg.st
tag @e[tag=mg.cmnew] remove mg.cmnew
title @s actionbar [{"text":"👥 Leurre posé ! Reste : ","color":"light_purple"},{"score":{"name":"@s","objective":"mg.cmdl"},"color":"white"}]
execute at @s run particle minecraft:poof ~ ~1 ~ 0.3 0.5 0.3 0.02 12
execute at @s run playsound minecraft:entity.illusioner.mirror_move player @s ~ ~ ~ 0.8 1.2
