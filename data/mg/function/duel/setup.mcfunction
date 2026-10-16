# Prépare un duelliste (@s ; $dli = arène) : pause mémorisée (mg.dlpz), inventaire, kit, départ
tag @s remove mg.dlpz
execute if entity @s[tag=mg.spectate] run tag @s add mg.dlpz
tag @s add mg.dl
tag @s add mg.spectate
scoreboard players operation @s mg.dli = $dli mg.st
scoreboard players set @s mg.dlr 0
scoreboard players reset @s mg.dlto
tag @s remove mg.dlrq
# son vote éventuel ne compte plus (comme elyrace/solo/start)
scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
gamemode adventure @s
effect clear @s
effect give @s minecraft:saturation infinite 0 true
# pas de mort hors tir : résistance maximale (coups de poing), pas de dégâts de chute (portique du Canyon)
effect give @s minecraft:resistance infinite 4 true
attribute @s minecraft:fall_damage_multiplier base set 0
function mg:core/heal
clear @s
function mg:duel/kit
function mg:duel/spawn
