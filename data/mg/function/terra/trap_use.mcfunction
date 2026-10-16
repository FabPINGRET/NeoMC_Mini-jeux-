# @s : pose un piège à ses pieds (hors de la colonie, 4 actifs au plus)
execute if score @s mg.tvtr matches ..0 run return run function mg:terra/no_trap
execute unless entity @s[tag=mg.tvout] run return run function mg:terra/trap_here
execute if block ~ ~-0.3 ~ #mg:tv_pass run return run function mg:terra/trap_air
scoreboard players operation $own mg.st = @s mg.tvpid
scoreboard players set $tvn mg.st 0
execute as @e[type=minecraft:marker,tag=mg.tvtrap] if score @s mg.tvo = $own mg.st run scoreboard players add $tvn mg.st 1
execute if score $tvn mg.st matches 4.. unless score @s mg.trcl matches 4 run return run function mg:terra/trap_max
execute if score $tvn mg.st matches 8.. run return run function mg:terra/trap_max
scoreboard players remove @s mg.tvtr 1
execute align xyz positioned ~0.5 ~ ~0.5 run function mg:terra/trap_new
