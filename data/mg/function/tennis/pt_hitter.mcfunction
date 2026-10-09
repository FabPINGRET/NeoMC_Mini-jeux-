# @s : balle — point au frappeur
scoreboard players operation $tnw mg.st = @s mg.tnl
execute as @e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1] run function mg:tennis/point
