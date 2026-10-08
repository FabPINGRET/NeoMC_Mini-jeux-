$tp @s $(x).5 65 $(z).5 0 15
gamemode creative @s
$execute if score $tp mg.st matches 1 run title @s title [{"text":"✎ ","color":"gold"},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"yellow","bold":true}]
$execute if score $tp mg.st matches 3 run title @s title [{"text":"✎ ","color":"gold"},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"yellow","bold":true}]
title @s subtitle {"text":"Construis-le en 2 min 30 (sans écrire de texte !)","color":"gray"}
$execute if score $tp mg.st matches 1 run tellraw @s [{"text":"\n✎ À CONSTRUIRE : ","color":"gold","bold":true},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"yellow","bold":true},{"text":"  (2 min 30, reste sur ta parcelle)","color":"gray"}]
$execute if score $tp mg.st matches 3 run tellraw @s [{"text":"\n✎ À CONSTRUIRE : ","color":"gold","bold":true},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"yellow","bold":true},{"text":"  (2 min 30, reste sur ta parcelle)","color":"gray"}]
