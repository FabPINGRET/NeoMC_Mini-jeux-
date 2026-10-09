# @s : jauge qui oscille 0 → 100 → 0 (bois : 3 %/tick, putter : 2 %/tick)
scoreboard players set $gfgs mg.st 3
execute if score $gfclub mg.st matches 2 run scoreboard players set $gfgs mg.st 2
scoreboard players operation $gfgs mg.st *= @s mg.gfq
scoreboard players operation @s mg.gfp += $gfgs mg.st
execute if score @s mg.gfp matches 100.. run scoreboard players set @s mg.gfq -1
execute if score @s mg.gfp matches 100.. run scoreboard players set @s mg.gfp 100
execute if score @s mg.gfp matches ..0 run scoreboard players set @s mg.gfq 1
execute if score @s mg.gfp matches ..0 run scoreboard players set @s mg.gfp 0
