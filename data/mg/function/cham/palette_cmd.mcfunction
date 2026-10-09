# @s a choisi dans la palette (mg.cmp = partie × 100 + matière)
scoreboard players operation $cmv mg.st = @s mg.cmp
scoreboard players reset @s mg.cmp
scoreboard players enable @s mg.cmp
scoreboard players set #100 mg.st 100
scoreboard players operation $cmm mg.st = $cmv mg.st
scoreboard players operation $cmm mg.st %= #100 mg.st
scoreboard players operation $cmpp mg.st = $cmv mg.st
scoreboard players operation $cmpp mg.st /= #100 mg.st
execute unless score $cmpp mg.st matches 1..5 run return 0
scoreboard players operation @s mg.cmpt = $cmpp mg.st
execute if score $cmm mg.st matches 0 run return run function mg:cham/hud
execute if score $cmm mg.st matches 1..75 run function mg:cham/paint_do
