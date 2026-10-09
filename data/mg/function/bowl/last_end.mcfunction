# @s : partie finie pour ce joueur (le cumul du dernier frame est écrit)
scoreboard players operation @s mg.bcu += @s mg.bfs
scoreboard players set @s mg.bfs 0
execute store result storage mg:bowl q.f int 1 run scoreboard players get @s mg.bfr
execute store result storage mg:bowl q.v int 1 run scoreboard players get @s mg.bcu
function mg:bowl/cw with storage mg:bowl q
scoreboard players set @s mg.brl 4
tellraw @a[tag=mg.play] [{"text":"🎳 ","color":"light_purple"},{"selector":"@s","color":"yellow"},{"text":" termine avec ","color":"gray"},{"score":{"name":"@s","objective":"mg.bcu"},"color":"gold","bold":true},{"text":" points.","color":"gray"}]
