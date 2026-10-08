# 4 minutes écoulées : le plus avancé gagne
tellraw @a[tag=mg.play] [{"text":"🪽 Temps écoulé : le plus avancé l'emporte !","color":"gold"}]
effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
scoreboard players set $skmx mg.st -1
execute as @a[tag=mg.play] run scoreboard players operation $skmx mg.st > @s mg.skr
execute if score $skmx mg.st matches ..0 run return run function mg:core/draw
tag @a remove mg.skw
execute as @a[tag=mg.play] if score @s mg.skr = $skmx mg.st run tag @s add mg.skw
execute as @a[tag=mg.skw,sort=random,limit=1] run function mg:core/win_player
tag @a remove mg.skw
