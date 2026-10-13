# Appelé à la fin de lobby/deco : rhabille les entités du décor selon le thème actif
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/reskin
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/reskin
function mg:lobby/food_skin
