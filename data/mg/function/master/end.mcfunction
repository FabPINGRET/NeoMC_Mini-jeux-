# Fin : dernier debout gagne ; sinon match nul
execute unless score $state mg.st matches 2 run return 0
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"👑 Fin de l'entraînement : ","color":"yellow"},{"score":{"name":"@p[tag=mg.play]","objective":"mg.msm"},"color":"red"},{"text":" erreur(s) sur 20 ordres.","color":"yellow"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
execute store result score $a mg.st if entity @a[tag=mg.play]
execute if score $a mg.st matches 1 as @a[tag=mg.play,limit=1] run return run function mg:core/win_player
function mg:core/draw
