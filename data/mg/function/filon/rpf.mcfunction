# Macro {f, y1, y2} : un filon (place feature) à une position au hasard du chunk
$execute store result storage mg:filon p.y int 1 run random value $(y1)..$(y2)
execute store result storage mg:filon p.x int 1 run random value 1..14
execute store result storage mg:filon p.z int 1 run random value 46001..46014
$data modify storage mg:filon p.f set value "$(f)"
function mg:filon/pf with storage mg:filon p
