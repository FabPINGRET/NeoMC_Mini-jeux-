# @s (marcheur) sur l'or : sa paire gagne
scoreboard players operation $p mg.st = @s mg.lbp
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] {"text":"🙈 Sortie trouvée ! (entraînement)","color":"yellow"}
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
function mg:core/win_player
execute as @a[tag=mg.lbg,tag=mg.play] if score @s mg.lbp = $p mg.st run function mg:lab/win_guide
