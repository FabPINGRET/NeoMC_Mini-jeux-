# Dès que la zone est chargée (vérifié toutes les 0,5 s) : portillon, boîtes à objets, un kart sous chaque pilote
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute unless function mg:kart/loaded_all run return run schedule function mg:kart/place_all 10t
function mg:kart/gate_on
function mg:kart/boxes
execute as @a[tag=mg.play] at @s run function mg:kart/kart_new
