# Charge de vent (@s) : explose au contact d'un rival (à 3,5 blocs)
execute unless entity @a[tag=mg.play,distance=..3.5] run return 0
tag @a remove mg.skak
execute on origin run tag @s add mg.skak
execute as @a[tag=mg.play,tag=!mg.skak,tag=!mg.skstun,distance=..3.5,sort=nearest,limit=1] run tag @s add mg.skv
execute unless entity @a[tag=mg.skv] run return run tag @a remove mg.skak
particle minecraft:gust_emitter_small ~ ~ ~ 0 0 0 0 1 force @a
playsound minecraft:entity.wind_charge.wind_burst master @a ~ ~ ~ 1.5 1
execute as @a[tag=mg.skv] run function mg:sky/stun
tag @a remove mg.skv
tag @a remove mg.skak
kill @s
