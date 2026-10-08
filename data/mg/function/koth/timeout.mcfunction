# 5 min écoulées : le plus de points gagne (égalité = match nul)
execute if score $khm mg.st matches 1 if score Rouge mg.kh > Bleu mg.kh run return run function mg:core/win_red
execute if score $khm mg.st matches 1 if score Bleu mg.kh > Rouge mg.kh run return run function mg:core/win_blue
execute if score $khm mg.st matches 1 run return run function mg:core/draw
scoreboard players set $khx mg.st 0
scoreboard players operation $khx mg.st > @a[tag=mg.play] mg.kh
scoreboard players set $khc mg.st 0
execute as @a[tag=mg.play] if score @s mg.kh = $khx mg.st run scoreboard players add $khc mg.st 1
execute if score $khx mg.st matches 0 run return run function mg:core/draw
execute if score $khc mg.st matches 2.. run return run function mg:core/draw
execute as @a[tag=mg.play] if score @s mg.kh = $khx mg.st run function mg:core/win_player
