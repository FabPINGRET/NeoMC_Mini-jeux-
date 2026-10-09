# @s : zone touchable d'un caméléon touchée par le tir
scoreboard players operation $cmv mg.st = @s mg.cmid
execute as @a[tag=mg.cmh,tag=!mg.cmout] if score @s mg.cmid = $cmv mg.st run function mg:cham/found
