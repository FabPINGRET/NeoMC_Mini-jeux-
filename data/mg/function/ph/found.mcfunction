# @s (cacheur) trouvé : devient chercheur
scoreboard players set @s mg.deaths 0
scoreboard players operation $pid mg.st = @s mg.pid
execute as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run kill @s
execute as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run kill @s
tag @s remove mg.phh
tag @s add mg.phs
team join mg_red @s
function mg:ph/seeker_kit
spreadplayers 0 23600 1 4 under 85 false @s
tellraw @a[tag=mg.play] [{"text":"🎭 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a été trouvé et rejoint les chercheurs !","color":"gray"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.item.break master @s ~ ~ ~ 0.8 0.7
