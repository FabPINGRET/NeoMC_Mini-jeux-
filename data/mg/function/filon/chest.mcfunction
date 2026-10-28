# Coffre enfoui (butin au hasard : loot table mg:filon/treasure)
execute store result storage mg:filon p.y int 1 run random value 41..90
execute store result storage mg:filon p.x int 1 run random value 1..14
execute store result storage mg:filon p.z int 1 run random value 46001..46014
function mg:filon/chest_at with storage mg:filon p
