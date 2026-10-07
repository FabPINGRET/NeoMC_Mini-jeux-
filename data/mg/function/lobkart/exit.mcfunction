# @s descend du kart : retour au garage
execute unless entity @s[tag=mg.lk] run return 0
function mg:lobkart/remove
tag @s add mg.lkz
tp @s 0.5 64 51.5 180 0
function mg:core/give_menu
title @s actionbar [{"text":"🏎 Kart rangé. À bientôt sur le circuit !","color":"gold"}]
