# Aventure : plus personne en jeu (tous ont fini, avec des passes) : même résultat qu'au temps écoulé, scores figés
execute unless score $state mg.st matches 2 run return 0
tellraw @a[tag=!mg.surv] [{"text":"🏁 Tout le monde est arrivé au bout !","color":"gold"}]
function mg:dropadv/k_rank
