# Passe partielle : la vague est rejouée, on ne garde que $mex quarts des nouveaux monstres (tirés au sort)
tag @e[tag=mg.mob] add mg.mb0
function mg:mobarena/wave with storage mg:mw
execute store result score $mnc mg.st if entity @e[tag=mg.mob,tag=!mg.mb0]
# à retirer = nouveaux − nouveaux × $mex / 4
scoreboard players operation $mnk mg.st = $mnc mg.st
scoreboard players operation $mnk mg.st *= $mex mg.st
scoreboard players set #4 mg.st 4
scoreboard players operation $mnk mg.st /= #4 mg.st
scoreboard players operation $mnc mg.st -= $mnk mg.st
function mg:mobarena/scale_cull
