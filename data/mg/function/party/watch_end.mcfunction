# Temps écoulé : One in the Chamber → le meilleur tueur gagne ; sinon fin sans vainqueur
tellraw @a[tag=!mg.surv] [{"text":"★ ","color":"gold"},{"text":"Temps écoulé pour ce mini-jeu !","color":"gray"}]
execute if score $game mg.st matches 26 run return run function mg:party/watch_oitc
function mg:core/draw
