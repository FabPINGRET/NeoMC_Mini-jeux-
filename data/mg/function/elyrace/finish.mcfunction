# @s = joueur qui franchit l'anneau d'arrivée (course de groupe ; le solo a sa propre arrivée, qui fixe sa phase 3)
execute if entity @s[tag=mg.xso] run return run function mg:elyrace/solo/finish
scoreboard players add $xf mg.st 1
scoreboard players operation @s mg.xf = $xf mg.st
# temps de l'arrivée : le chrono du groupe moins le bonus des anneaux d'or (bonus : #xgs = secondes retirées)
scoreboard players operation #xrt mg.st = $xt mg.st
function mg:elyrace/bonus
# clé de classement de end : temps bonus déduit x 100 + place (la place départage deux temps égaux : le premier arrivé gagne)
scoreboard players operation @s mg.xft = #xrt mg.st
scoreboard players operation @s mg.xft *= #k100 mg.st
scoreboard players operation @s mg.xft += @s mg.xf
scoreboard players operation #s mg.st = #xrt mg.st
scoreboard players operation #s mg.st /= #k20 mg.st
tellraw @a[tag=mg.play] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" passe la ligne d'arrivée (","color":"gray"},{"score":{"name":"#s","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]
execute if score @s mg.xu matches 1.. run tellraw @a[tag=mg.play] [{"text":"   ★ dont ","color":"gold"},{"score":{"name":"#xgs","objective":"mg.st"},"color":"white"},{"text":" s de bonus d'or","color":"gray"}]
title @s subtitle ""
title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
execute at @s run particle minecraft:firework ~ ~1 ~ 1 1 1 0.2 60
# records : le temps est lu dans #xrt (chrono du groupe moins le bonus d'or), personnel puis serveur, selon le parcours du joueur (mg.xcr)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/record
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/record
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
