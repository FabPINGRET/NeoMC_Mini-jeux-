# Minimap : carte de base, un point par pilote à la couleur de son kart, puis les 15 lignes du tableau
data modify storage mg:kart mm set from storage mg:kart base
execute as @a[tag=mg.play] run function mg:kart/mm_dot
function mg:kart/mm_show with storage mg:kart mm
