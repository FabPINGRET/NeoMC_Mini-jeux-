# Fin : meilleur total (barre latérale) ; égalité = match nul ; seul = résultat sans victoire
scoreboard players set $bx mg.st -1
scoreboard players operation $bx mg.st > @a[tag=mg.play] mg.bsc
scoreboard players set $bc mg.st 0
execute as @a[tag=mg.play] if score @s mg.bsc = $bx mg.st run scoreboard players add $bc mg.st 1
tellraw @a[tag=mg.play] [{"text":"🎳 Meilleur score : ","color":"light_purple"},{"score":{"name":"$bx","objective":"mg.st"},"color":"gold","bold":true}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
execute if score $bc mg.st matches 2.. run return run function mg:core/draw
execute as @a[tag=mg.play] if score @s mg.bsc = $bx mg.st run return run function mg:core/win_player
function mg:core/draw
