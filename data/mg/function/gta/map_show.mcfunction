# @s tient la carte : plan de la ville, sa position (rouge), l'objectif de sa mission (or)
execute unless score $rp mg.st matches 1 run return run title @s actionbar [{"text":"🗺 Carte : active le resource pack (/function mg:rp_on)","color":"gray"}]
execute unless data storage mg:gta dots run function mg:gta/dots_init
scoreboard players set #30 mg.st 30
scoreboard players set #177 mg.st 177
execute store result score $gmi mg.st run data get entity @s Pos[0]
execute store result score $gmj mg.st run data get entity @s Pos[2]
scoreboard players add $gmi mg.st 88
scoreboard players remove $gmj mg.st 32312
scoreboard players operation $gmi mg.st *= #30 mg.st
scoreboard players operation $gmi mg.st /= #177 mg.st
scoreboard players operation $gmj mg.st *= #30 mg.st
scoreboard players operation $gmj mg.st /= #177 mg.st
execute if score $gmi mg.st matches ..-1 run scoreboard players set $gmi mg.st 0
execute if score $gmi mg.st matches 30.. run scoreboard players set $gmi mg.st 29
execute if score $gmj mg.st matches ..-1 run scoreboard players set $gmj mg.st 0
execute if score $gmj mg.st matches 30.. run scoreboard players set $gmj mg.st 29
scoreboard players operation $gmj mg.st *= #30 mg.st
scoreboard players operation $gmj mg.st += $gmi mg.st
execute store result storage mg:gta mi.p int 1 run scoreboard players get $gmj mg.st
function mg:gta/map_pick_p with storage mg:gta mi
data modify storage mg:gta mp.t set value ""
scoreboard players operation $gb mg.st = @s mg.bid
tag @e remove mg.gmine
execute as @e[tag=mg.gmo] if score @s mg.bid = $gb mg.st run tag @s add mg.gmine
execute if entity @e[tag=mg.gmine] run function mg:gta/map_target
data modify storage mg:gta mp.o set value [{"text":""}]
tag @s add mg.gme
execute as @a[tag=mg.gtw,tag=!mg.gme,gamemode=!spectator] run function mg:gta/map_other
tag @s remove mg.gme
title @s times 0 6 2
scoreboard players set @s mg.gal 6
title @s actionbar [{"text":"● ","color":"red"},{"text":"toi  ","color":"gray"},{"text":"● ","color":"#3FA9FF"},{"text":"potes  ","color":"gray"},{"text":"● ","color":"gold"},{"text":"mission  ","color":"gray"},{"text":"■ ","color":"#9646C8"},{"text":"concession ","color":"gray"},{"text":"■ ","color":"#C82828"},{"text":"armurerie ","color":"gray"},{"text":"■ ","color":"#E8BA24"},{"text":"banque ","color":"gray"},{"text":"■ ","color":"#F58C1E"},{"text":"commerces","color":"gray"}]
function mg:gta/map_title with storage mg:gta mp
