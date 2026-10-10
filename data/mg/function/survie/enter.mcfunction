# Aller en survie (@s)
execute unless score $setup mg.st matches 1 run return run tellraw @s [{"text":"⚠ Installation manquante : un OP doit d'abord lancer /function mg:setup","color":"red"}]
execute if entity @s[tag=mg.surv] run return run tellraw @s [{"text":"Tu es déjà en survie.","color":"gray"}]
execute if entity @s[tag=mg.play] run return run tellraw @s [{"text":"⚠ Tu participes à la partie en cours : la survie sera accessible après.","color":"red"}]
execute if entity @s[tag=mg.out] run return run tellraw @s [{"text":"⚠ Partie en cours : la survie sera accessible après.","color":"red"}]
execute if entity @s[tag=mg.mpp] run return run tellraw @s [{"text":"⚠ Tu participes à la Mini Party : la survie sera accessible après.","color":"red"}]
function mg:lobkart/leave
execute unless score @s mg.svid matches 1.. run function mg:survie/assign
execute unless score @s mg.svid matches 1.. run return 0

# Quitte proprement le lobby (parkour, plot créatif)
function mg:parkour/quit
tag @s remove mg.inplot
tag @s remove mg.plabel
tag @s remove mg.visit
tag @s add mg.surv
# Son vote éventuel ne compte plus (exclu du décompte en survie)
execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
team leave @s
effect clear @s
clear @s
xp set @s 0 levels
xp set @s 0 points
gamemode survival @s
function mg:core/attr_reset
attribute @s minecraft:fall_damage_multiplier base set 1

execute store result storage mg:survie id.id int 1 run scoreboard players get @s mg.svid
execute store result storage mg:survie id.x int 1 run scoreboard players get @s mg.svvx
function mg:survie/enter_m with storage mg:survie id
# Soin complet à l'arrivée en survie
function mg:core/heal
