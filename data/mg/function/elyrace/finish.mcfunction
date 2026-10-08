# @s = joueur qui franchit l'anneau d'arrivée
scoreboard players add $xf mg.st 1
scoreboard players operation @s mg.xf = $xf mg.st
scoreboard players operation #s mg.st = $xt mg.st
scoreboard players operation #s mg.st /= #k20 mg.st
tellraw @a[tag=mg.play] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" passe la ligne d'arrivée en position ","color":"gray"},{"score":{"name":"@s","objective":"mg.xf"},"color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"#s","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]
title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
execute at @s run particle minecraft:firework ~ ~1 ~ 1 1 1 0.2 60
# premier arrivé : la course s'arrête dans 20 s au plus, le temps que les autres terminent
execute if score $xf mg.st matches 1 run scoreboard players set $xw mg.st 1
execute if score $xf mg.st matches 1 run scoreboard players set $xe mg.st 400
execute if score $xf mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🪽 Les autres ont 20 secondes pour terminer et se classer.","color":"gold"}]
# arrivé : mis en sécurité au perchoir de départ (la zone construite s'arrête après l'arrivée), en spectateur
execute store result storage mg:c x int 1 run scoreboard players get $px mg.st
execute store result storage mg:c y int 1 run scoreboard players get $py mg.st
execute store result storage mg:c z int 1 run scoreboard players get $pz mg.st
function mg:core/tp_perch with storage mg:c
gamemode spectator @s
