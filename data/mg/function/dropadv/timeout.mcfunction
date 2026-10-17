# Temps écoulé : classement aux niveaux réussis (voir k_rank)
execute unless score $state mg.st matches 2 run return 0
tellraw @a[tag=!mg.surv] [{"text":"⏱ Temps écoulé !","color":"gold"}]
function mg:dropadv/k_rank
