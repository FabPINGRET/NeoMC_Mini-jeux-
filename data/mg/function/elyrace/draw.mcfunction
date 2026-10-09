# Fin sans vainqueur de la Course d'élytres (plus de participant, partie annulée) : en solo, fin du contre-la-montre ; sinon le match nul habituel
execute if score $xs mg.st matches 1 run return run function mg:elyrace/solo/end
function mg:core/draw
