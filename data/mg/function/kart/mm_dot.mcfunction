# Case du kart de @s sur la minimap
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.kdot] remove mg.kdot
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st run tag @s add mg.kdot
execute unless entity @e[tag=mg.kdot] run return 0
execute store result score $mx mg.st run data get entity @e[tag=mg.kdot,limit=1] Pos[0]
execute store result score $mz mg.st run data get entity @e[tag=mg.kdot,limit=1] Pos[2]
scoreboard players operation $mx mg.st += #kmx0 mg.st
scoreboard players operation $mx mg.st *= #kmc mg.st
scoreboard players operation $mx mg.st /= #kmw mg.st
scoreboard players operation $mz mg.st -= #kmz0 mg.st
scoreboard players operation $mz mg.st *= #kmr mg.st
scoreboard players operation $mz mg.st /= #kmh mg.st
execute if score $mx mg.st matches ..-1 run scoreboard players set $mx mg.st 0
execute if score $mz mg.st matches ..-1 run scoreboard players set $mz mg.st 0
execute if score $mx mg.st >= #kmc mg.st run scoreboard players operation $mx mg.st = #kmc mg.st
execute if score $mx mg.st >= #kmc mg.st run scoreboard players remove $mx mg.st 1
execute if score $mz mg.st >= #kmr mg.st run scoreboard players operation $mz mg.st = #kmr mg.st
execute if score $mz mg.st >= #kmr mg.st run scoreboard players remove $mz mg.st 1
execute store result storage mg:kart dot.c int 1 run scoreboard players get $mx mg.st
execute store result storage mg:kart dot.r int 1 run scoreboard players get $mz mg.st
scoreboard players operation $kc mg.st = @e[tag=mg.kdot,limit=1] mg.kcol
execute if score $kc mg.st matches 1 run data modify storage mg:kart dot.col set value "red"
execute if score $kc mg.st matches 2 run data modify storage mg:kart dot.col set value "blue"
execute if score $kc mg.st matches 3 run data modify storage mg:kart dot.col set value "green"
execute if score $kc mg.st matches 4 run data modify storage mg:kart dot.col set value "yellow"
execute if score $kc mg.st matches 5 run data modify storage mg:kart dot.col set value "dark_purple"
execute if score $kc mg.st matches 6 run data modify storage mg:kart dot.col set value "gold"
execute if score $kc mg.st matches 7 run data modify storage mg:kart dot.col set value "aqua"
execute if score $kc mg.st matches 8 run data modify storage mg:kart dot.col set value "light_purple"
function mg:kart/mm_dot_m with storage mg:kart dot
