# 5 minutes : le plus haut gagne
tellraw @a[tag=mg.play] [{"text":"🌪 Temps écoulé : le plus haut l'emporte !","color":"gold"}]
effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
scoreboard players set $skmx mg.st -9999
execute as @a[tag=mg.play] run scoreboard players operation $skmx mg.st > @s mg.t
tag @a remove mg.skw
execute as @a[tag=mg.play] if score @s mg.t = $skmx mg.st run tag @s add mg.skw
execute as @a[tag=mg.skw,sort=random,limit=1] run function mg:core/win_player
tag @a remove mg.skw
