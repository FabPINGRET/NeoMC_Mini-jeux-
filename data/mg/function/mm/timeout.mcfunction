# Fin du temps : les survivants gagnent (seul : fin de l'entraînement)
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🔪 Fin de l'entraînement.","color":"yellow"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
tellraw @a [{"text":"⏳ Le temps est écoulé : les innocents ont survécu !","color":"green"}]
function mg:mm/innocents_win
