# Pseudo du défieur (@s = défieur, à sa position) -> mg:duel inv.p : lu sur sa tête (loot mg:plot_head), comme kart/cam_new
summon minecraft:item_display ~ ~ ~ {Tags:["mg.dlnm"]}
loot replace entity @e[type=minecraft:item_display,tag=mg.dlnm,limit=1] contents loot mg:plot_head
data modify storage mg:duel inv.p set from entity @e[type=minecraft:item_display,tag=mg.dlnm,limit=1] item.components."minecraft:profile".name
kill @e[type=minecraft:item_display,tag=mg.dlnm]
