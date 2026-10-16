# @s ramasse l'œuf d'ambre 4
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.treg += #p3 mg.st
function mg:terra/rpg/xp {n:60}
title @s actionbar {"text":"🥚 Œuf d'ambre ramassé ! Rapporte-les au Dr Ossei","color":"gold","bold":true}
scoreboard players set @s mg.tval 60
execute at @s run playsound minecraft:entity.chicken.egg player @s ~ ~ ~ 1 0.6
