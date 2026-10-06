# Macro : x — colonne x passe au bleu
$execute if score c$(x) mg.tw matches 1 run scoreboard players remove $nr mg.st 1
scoreboard players add $nb mg.st 1
$scoreboard players set c$(x) mg.tw 2
$fill $(x) 80 6988 $(x) 80 7012 minecraft:blue_concrete
$particle minecraft:soul_fire_flame $(x).5 82 7000.0 0.2 1 12 0.02 120
$playsound minecraft:block.beacon.activate master @a $(x) 81 7000 1 1.4
function mg:turf/show
