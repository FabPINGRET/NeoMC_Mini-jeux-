# 👑 King of the Hill — préparation ($khm : 0 solo, 1 équipes)
scoreboard players set $khm mg.st 0
execute if score $game mg.st matches 87 run scoreboard players set $khm mg.st 1
function mg:koth/build
kill @e[type=minecraft:item,x=-30,y=60,z=20370,dx=60,dy=50,dz=60]
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 100
scoreboard players set $pz mg.st 20400
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.kh 0
scoreboard players reset Rouge mg.kh
scoreboard players reset Bleu mg.kh
execute if score $khm mg.st matches 1 run scoreboard players set $nt mg.st 2
execute if score $khm mg.st matches 1 run function mg:core/assign_teams
execute as @a[tag=mg.play] run function mg:koth/spawn
