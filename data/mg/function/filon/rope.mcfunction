# 🪢 Corde de remontée (recharge 120 s)
execute if score @s mg.fncd matches 1.. run return run title @s actionbar [{"text":"🪢 Corde en recharge : ","color":"gray"},{"score":{"name":"@s","objective":"mg.fncd"},"color":"yellow"},{"text":" s","color":"gray"}]
execute unless entity @s[tag=mg.fnin] run return run title @s actionbar {"text":"Tu es déjà à la surface.","color":"gray"}
function mg:filon/to_surface
scoreboard players set @s mg.fncd 120
execute at @s run playsound minecraft:entity.leash_knot.place master @s ~ ~ ~ 1 0.8
title @s actionbar {"text":"🪢 Remonté à la surface !","color":"gold"}
