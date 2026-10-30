# @s : kit de sa classe (mg.pcl) + boutique + retour (+ menu) ; les élytres libres du spawn (fusées + résistance toutes les 2 s) s'arrêtent
execute if entity @s[tag=mg.elyf] run function mg:elytra/free_stop
execute if entity @s[tag=mg.ely] run function mg:elytra/stop_quiet
clear @s
effect clear @s
function mg:core/attr_reset
execute if score @s mg.pcl matches 1 run function mg:pvpc/kit_1
execute if score @s mg.pcl matches 2 run function mg:pvpc/kit_2
execute if score @s mg.pcl matches 3 run function mg:pvpc/kit_3
execute if score @s mg.pcl matches 4 run function mg:pvpc/kit_4
function mg:pvpc/items
function mg:core/give_menu
function mg:core/heal
