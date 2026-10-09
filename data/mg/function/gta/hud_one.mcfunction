# @s : barre d'action (police verte du pack si $rp = 1) ; mission en cours en priorité
execute if score @s mg.gmt matches 1.. run return run function mg:gta/mis_hud
execute if score $rp mg.st matches 1 run return run function mg:gta/hud_rp
function mg:gta/hud_plain
