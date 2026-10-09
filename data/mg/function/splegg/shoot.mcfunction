# Tir (@s = joueur qui vient de lancer un œuf) : munitions rechargées + durée de vie de l'œuf ($sgl ticks, = $rs / 4)
function mg:splegg/give_egg
playsound minecraft:entity.chicken.egg master @a ~ ~ ~ 0.8 1.4
scoreboard players set $rs mg.st 160
execute if score $ar mg.st matches 1.. run scoreboard players operation $rs mg.st = $vrs mg.st
scoreboard players operation $sgl mg.st = $rs mg.st
scoreboard players set #k4 mg.st 4
scoreboard players operation $sgl mg.st /= #k4 mg.st
