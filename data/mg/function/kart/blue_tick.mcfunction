# Carapace bleue (@s) : vise le kart du premier (à travers tout), explose à son contact
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run kill @s
tag @e[tag=mg.ktgt] remove mg.ktgt
execute as @a[tag=mg.play,tag=!mg.kfin,scores={mg.krk=1},limit=1] run scoreboard players operation $ktg mg.st = @s mg.ri
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $ktg mg.st run tag @s add mg.ktgt
execute unless entity @e[tag=mg.ktgt] run return run kill @s
execute if entity @e[tag=mg.ktgt,distance=..2.2] run return run function mg:kart/blue_boom
execute facing entity @e[tag=mg.ktgt,limit=1] feet run tp @s ^ ^ ^1.8
particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0 3
