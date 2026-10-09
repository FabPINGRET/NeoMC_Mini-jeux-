# 🚚 Convoi — préparation ($cvm : 0 attaque/défense, 1 coop)
scoreboard players set $cvm mg.st 0
execute if score $game mg.st matches 90 run scoreboard players set $cvm mg.st 1
function mg:convoy/build
function mg:convoy/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 21200
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
execute if score $cvm mg.st matches 0 run scoreboard players set $nt mg.st 2
execute if score $cvm mg.st matches 0 run function mg:core/assign_teams
execute if score $cvm mg.st matches 1 run team join mg_green @a[tag=mg.play]
scoreboard players set $cvr mg.st 1
scoreboard players set $cvo mg.st 0
function mg:convoy/reset_cart
execute as @a[tag=mg.play] run function mg:convoy/spawn
