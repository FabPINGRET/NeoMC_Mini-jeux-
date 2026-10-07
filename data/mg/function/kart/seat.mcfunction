# Installe le pilote selon sa vue : 1re personne assis dans le kart, 3e personne spectateur de sa caméra
execute if score @s mg.kvm matches 1 run return run function mg:kart/seat_ride
function mg:kart/seat_cam
