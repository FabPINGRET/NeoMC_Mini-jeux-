# Fenêtre de la boutique de @s, construite à la volée : pièces, taille du sac, objets trop chers grisés
execute store result storage mg:party sh.c int 1 run scoreboard players get @s mg.mpm
scoreboard players operation $tmp mg.st = @s mg.mid
scoreboard players operation $tmp mg.st += @s mg.mit
scoreboard players operation $tmp mg.st += @s mg.mip
execute store result storage mg:party sh.n int 1 run scoreboard players get $tmp mg.st
data modify storage mg:party sh.k1 set value "aqua"
data modify storage mg:party sh.k2 set value "light_purple"
data modify storage mg:party sh.k3 set value "yellow"
execute unless score @s mg.mpm matches 10.. run data modify storage mg:party sh.k1 set value "dark_gray"
execute unless score @s mg.mpm matches 18.. run data modify storage mg:party sh.k2 set value "dark_gray"
execute unless score @s mg.mpm matches 15.. run data modify storage mg:party sh.k3 set value "dark_gray"
function mg:party/shop_dialog_m with storage mg:party sh
