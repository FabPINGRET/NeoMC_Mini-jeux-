# @s tient une arme mg_gun (lobby, Neo GTA) : barre de durabilité pendant la recharge, puis pendant la cadence du Sniper
# La recharge est celle de l'arme en main seulement (mg.grt) ; gcd est partagé en Neo GTA : la cadence du Sniper n'est montrée que s'il n'y a pas de recharge
scoreboard players set $gbt mg.st 0
execute if score @s mg.grl matches 1.. run scoreboard players operation $gbr mg.st = @s mg.grl
execute unless score @s mg.grl matches 1.. if score @s mg.gcd matches 1.. run scoreboard players operation $gbr mg.st = @s mg.gcd
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 1 if items entity @s weapon.mainhand *[custom_data~{gun:1}] run scoreboard players set $gbt mg.st 30
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 2 if items entity @s weapon.mainhand *[custom_data~{gun:2}] run scoreboard players set $gbt mg.st 40
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 3 if items entity @s weapon.mainhand *[custom_data~{gun:3}] run scoreboard players set $gbt mg.st 50
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 4 if items entity @s weapon.mainhand *[custom_data~{gun:4}] run scoreboard players set $gbt mg.st 40
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 5 if items entity @s weapon.mainhand *[custom_data~{gun:5}] run scoreboard players set $gbt mg.st 60
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 6 if items entity @s weapon.mainhand *[custom_data~{gun:6}] run scoreboard players set $gbt mg.st 50
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 7 if items entity @s weapon.mainhand *[custom_data~{gun:7}] run scoreboard players set $gbt mg.st 80
execute if score @s mg.grl matches 1.. if score @s mg.grt matches 8 if items entity @s weapon.mainhand *[custom_data~{gun:8}] run scoreboard players set $gbt mg.st 40
execute unless score @s mg.grl matches 1.. if score @s mg.gcd matches 1.. if items entity @s weapon.mainhand *[custom_data~{gun:5}] run scoreboard players set $gbt mg.st 30
execute if score $gbt mg.st matches 1.. run return run function mg:gun/bar_set
# Rien à montrer : on remet à zéro toute arme restée avec une barre (celle qui vient de finir sa recharge comprise)
function mg:gun/bar_clear
