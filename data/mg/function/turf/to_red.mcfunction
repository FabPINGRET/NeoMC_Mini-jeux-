# Macro : x — colonne x passe au rouge
$execute if score c$(x) mg.tw matches 2 run scoreboard players remove $nb mg.st 1
scoreboard players add $nr mg.st 1
$scoreboard players set c$(x) mg.tw 1
$fill $(x) 80 6988 $(x) 80 7012 minecraft:red_concrete
$particle minecraft:flame $(x).5 82 7000.0 0.2 1 12 0.02 120
$playsound minecraft:block.beacon.activate master @a $(x) 81 7000 1 1.4
function mg:turf/show
