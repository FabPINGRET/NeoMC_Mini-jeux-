# Macro {b, y1, y2} : un bloc jackpot (2 à 4 collés) à une position au hasard du chunk
$execute store result storage mg:filon p.y int 1 run random value $(y1)..$(y2)
execute store result storage mg:filon p.x int 1 run random value 1..13
execute store result storage mg:filon p.z int 1 run random value 46001..46013
$data modify storage mg:filon p.f set value "$(b)"
function mg:filon/set with storage mg:filon p
