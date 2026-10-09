# Pyramide : préparation (zone chargée par koth2/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -27 80 35273 run return run schedule function mg:koth2/prepare_b 20t
execute unless loaded 27 80 35327 run return run schedule function mg:koth2/prepare_b 20t
execute unless loaded 0 80 35300 run return run schedule function mg:koth2/prepare_b 20t
# 👑 King of the Hill — préparation ($khm : 0 solo, 1 équipes)
scoreboard players set $khm mg.st 0
execute if score $game mg.st matches 207 run scoreboard players set $khm mg.st 1
function mg:koth2/build
kill @e[type=minecraft:item,x=-30,y=60,z=35270,dx=60,dy=50,dz=60]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 35300
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.kh 0
scoreboard players reset Rouge mg.kh
scoreboard players reset Bleu mg.kh
execute if score $khm mg.st matches 1 run scoreboard players set $nt mg.st 2
execute if score $khm mg.st matches 1 run function mg:core/assign_teams
execute as @a[tag=mg.play] run function mg:koth2/spawn
