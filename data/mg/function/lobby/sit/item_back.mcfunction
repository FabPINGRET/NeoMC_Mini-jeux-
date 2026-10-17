# @s : l'objet consommé lui est rendu (s'il le garde encore)
tag @s remove mg.lsg
execute if function mg:lobby/sit/item_keep run function mg:lobby/sit/item_check
