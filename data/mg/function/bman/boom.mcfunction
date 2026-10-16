# @s (bombe) explose : croix de flammes de portée mg.yr
tag @s add mg.yx
setblock ~ ~ ~ minecraft:air
setblock ~ ~1 ~ minecraft:air
kill @e[type=minecraft:item_display,tag=mg.yd,distance=..0.6]
scoreboard players operation $yo mg.st = @s mg.yo
execute as @a if score @s mg.yid = $yo mg.st if score @s mg.yu matches 1.. run scoreboard players remove @s mg.yu 1
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 1 1.1
function mg:bman/flame
scoreboard players operation $yk mg.st = @s mg.yr
execute positioned ~1 ~ ~ run function mg:bman/ray_px
scoreboard players operation $yk mg.st = @s mg.yr
execute positioned ~-1 ~ ~ run function mg:bman/ray_nx
scoreboard players operation $yk mg.st = @s mg.yr
execute positioned ~ ~ ~1 run function mg:bman/ray_pz
scoreboard players operation $yk mg.st = @s mg.yr
execute positioned ~ ~ ~-1 run function mg:bman/ray_nz
kill @s
