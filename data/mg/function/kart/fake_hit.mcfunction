function mg:kart/owner_hit
execute at @e[type=minecraft:item_display,tag=mg.kcur,limit=1] run kill @e[type=minecraft:text_display,tag=mg.kfakeq,distance=..1.5]
execute at @e[type=minecraft:item_display,tag=mg.kcur,limit=1] run particle minecraft:wax_off ~ ~0.5 ~ 0.4 0.4 0.4 0 15
kill @e[type=minecraft:item_display,tag=mg.kcur]
