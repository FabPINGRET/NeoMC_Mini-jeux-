# Temps écoulé : les survivants gagnent
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🧪 Fin de l'entraînement.","color":"yellow"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
tellraw @a {"text":"🧪 Les survivants ont tenu 3 minutes !","color":"aqua","bold":true}
function mg:core/win_blue
