# @s : un morceau du corps, recopié en leurre
summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmdd","mg.cmnew"]}
data modify entity @e[tag=mg.cmnew,limit=1] block_state set from entity @s block_state
data modify entity @e[tag=mg.cmnew,limit=1] transformation set from entity @s transformation
data modify entity @e[tag=mg.cmnew,limit=1] Rotation set from entity @s Rotation
scoreboard players operation @e[tag=mg.cmnew] mg.cmdn = $cmdc mg.st
tag @e[tag=mg.cmnew] remove mg.cmnew
