# @s = joueur qui franchit l'anneau d'arrivée en solo (appelé en 1re ligne de elyrace/finish) : annonce, records, phase 3
# temps = chrono du joueur moins le bonus de ses anneaux d'or (elyrace/bonus : #xgs = secondes retirées)
scoreboard players operation #xrt mg.st = @s mg.xst
function mg:elyrace/bonus
scoreboard players operation #s mg.st = #xrt mg.st
scoreboard players operation #s mg.st /= #k20 mg.st
tellraw @s [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" passe la ligne d'arrivée (","color":"gray"},{"score":{"name":"#s","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]
execute if score @s mg.xu matches 1.. run tellraw @s [{"text":"   ★ dont ","color":"gold"},{"score":{"name":"#xgs","objective":"mg.st"},"color":"white"},{"text":" s de bonus d'or","color":"gray"}]
title @s subtitle ""
title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
execute at @s run particle minecraft:firework ~ ~1 ~ 1 1 1 0.2 60
# records : le temps est lu dans #xrt, personnel puis serveur, selon son parcours (mg.xcr)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/record
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/record
# phase 3 : le chrono repart à 0 pour compter 30 ticks, puis solo/choice (le temps de l'arrivée est déjà enregistré)
scoreboard players set @s mg.xph 3
scoreboard players set @s mg.xst 0
