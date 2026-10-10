# Fin : dernier en piste, sinon le plus de coups restants (puis de points)
execute unless score $state mg.st matches 2 run return 0
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] {"text":"🚗 Fin de l'entraînement.","color":"yellow"}
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
scoreboard players set $bl mg.st -1
scoreboard players operation $bl mg.st > @a[tag=mg.play] mg.atl
tag @a remove mg.atw
execute as @a[tag=mg.play] if score @s mg.atl = $bl mg.st run tag @s add mg.atw
scoreboard players set $bp mg.st -1
scoreboard players operation $bp mg.st > @a[tag=mg.atw] mg.atp
execute as @a[tag=mg.atw] unless score @s mg.atp = $bp mg.st run tag @s remove mg.atw
execute store result score $c mg.st if entity @a[tag=mg.atw]
execute if score $c mg.st matches 1 as @a[tag=mg.atw,limit=1] run return run function mg:core/win_player
function mg:core/draw
