# @s pose une bombe (position : centre de sa case, au niveau des pieds)
execute unless block ~ ~ ~ minecraft:air run return 0
execute if entity @e[type=minecraft:marker,tag=mg.yb,distance=..0.5] run return 0
execute if score @s mg.yu >= @s mg.yn run return run title @s actionbar [{"text":"💣 Toutes tes bombes sont posées (","color":"gray"},{"score":{"name":"@s","objective":"mg.yn"},"color":"yellow"},{"text":" max)","color":"gray"}]
scoreboard players add @s mg.yu 1
summon minecraft:marker ~ ~ ~ {Tags:["mg.yb","mg.ynw"]}
scoreboard players operation @e[type=minecraft:marker,tag=mg.ynw] mg.yo = @s mg.yid
scoreboard players operation @e[type=minecraft:marker,tag=mg.ynw] mg.yr = @s mg.yr
scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yt 50
tag @e[tag=mg.ynw] remove mg.ynw
function mg:bman/bomb_show
playsound minecraft:entity.tnt.primed master @a ~ ~ ~ 0.8 1.2
