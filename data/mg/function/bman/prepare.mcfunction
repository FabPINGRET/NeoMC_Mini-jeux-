# 💣 Bomberman — préparation ($ym : 0 chacun pour soi, 1 équipes)
scoreboard players set $ym mg.st 0
execute if score $game mg.st matches 240 run scoreboard players set $ym mg.st 1
function mg:bman/build
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 76
scoreboard players set $pz mg.st 40700
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.yn 1
scoreboard players set @a[tag=mg.play] mg.yr 2
scoreboard players set @a[tag=mg.play] mg.yv 0
scoreboard players set @a[tag=mg.play] mg.yu 0
scoreboard players set @a[tag=mg.play] mg.yh 0
execute if score $ym mg.st matches 1 run scoreboard players set $nt mg.st 2
execute if score $ym mg.st matches 1 run function mg:core/assign_teams
execute if score $ym mg.st matches 0 run team join mg_sq @a[tag=mg.play]
scoreboard players set $yk mg.st 0
scoreboard players set $ykx mg.st 0
scoreboard players set $ykr mg.st 0
scoreboard players set $ykb mg.st 0
execute as @a[tag=mg.play] run function mg:bman/spawn
execute as @a[tag=mg.play] run function mg:bman/give
tellraw @a[tag=mg.play] [{"text":"💣 BOMBERMAN : ","color":"red","bold":true},{"text":"clic droit avec la bombe pour la poser. L'explosion part en croix et casse les briques ; les flammes éliminent. Ramasse les bonus : 💣 +1 bombe, 🔥 +1 portée, ⚡ vitesse. Attention à tes propres bombes !","color":"gray"}]
