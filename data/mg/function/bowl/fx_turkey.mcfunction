function mg:bowl/fx_strike
title @s title {"text":"🦃 TURKEY !","color":"gold","bold":true}
title @s subtitle [{"score":{"name":"@s","objective":"mg.bxs"},"color":"yellow"},{"text":" strikes d'affilée !","color":"yellow"}]
execute at @s run playsound minecraft:entity.turtle.egg_hatch master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 0.6
