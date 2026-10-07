# Tableau à droite : affichage suivant
execute if entity @a[scores={mg.wins=1..}] run scoreboard players set #any mg.wins 1
execute if entity @a[scores={mg.stp=1..}] run scoreboard players set #any mg.stp 1
execute if entity @a[scores={mg.stk=1..}] run scoreboard players set #any mg.stk 1
execute if score $vn mg.st matches 1.. unless score $rph mg.st matches 1 run return run function mg:hall/rot_votes
scoreboard players set $rph mg.st 0
scoreboard players set $hrt mg.st 160
scoreboard players set $rtry mg.st 0
function mg:hall/rot_next
