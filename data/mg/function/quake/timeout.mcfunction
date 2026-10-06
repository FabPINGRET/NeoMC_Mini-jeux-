# Quakecraft — fin du temps : le meilleur score gagne, égalité = match nul
scoreboard players set $best mg.st 0
execute as @a[tag=mg.play] if score @s mg.qk > $best mg.st run scoreboard players operation $best mg.st = @s mg.qk
execute as @a[tag=mg.play] if score @s mg.qk = $best mg.st run tag @s add mg.top
execute store result score $ntop mg.st if entity @a[tag=mg.top]
execute if score $ntop mg.st matches 1 as @a[tag=mg.top,limit=1] run function mg:core/win_player
execute unless score $ntop mg.st matches 1 run function mg:core/draw
tag @a remove mg.top
