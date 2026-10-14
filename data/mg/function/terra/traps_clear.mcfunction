# @s part : ses pièges disparaissent
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[tag=mg.tvtrap] if score @s mg.tvo = $own mg.st run kill @s
execute as @e[tag=mg.tvtrapd] if score @s mg.tvo = $own mg.st run kill @s
