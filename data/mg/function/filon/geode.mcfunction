# Géode d'améthyste au milieu du chunk (assez loin des murs pour être posée)
execute store result storage mg:filon p.y int 1 run random value 48..82
execute store result storage mg:filon p.x int 1 run random value 6..9
execute store result storage mg:filon p.z int 1 run random value 46006..46009
data modify storage mg:filon p.f set value "amethyst_geode"
function mg:filon/pf with storage mg:filon p
