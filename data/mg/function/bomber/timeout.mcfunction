# Fin : le plus de dégâts gagne (égalité = match nul)
scoreboard players set $bx mg.st 0
scoreboard players operation $bx mg.st > @a[tag=mg.play] mg.bmb
scoreboard players set $bc mg.st 0
execute as @a[tag=mg.play] if score @s mg.bmb = $bx mg.st run scoreboard players add $bc mg.st 1
tellraw @a[tag=mg.play] [{"text":"🏙 La ville est détruite à ","color":"gray"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"red","bold":true},{"text":" %","color":"gray"}]
execute if score $bx mg.st matches 0 run return run function mg:core/draw
execute if score $bc mg.st matches 2.. run return run function mg:core/draw
execute as @a[tag=mg.play] if score @s mg.bmb = $bx mg.st run function mg:core/win_player
