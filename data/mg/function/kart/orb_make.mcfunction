# 3 objets autour du kart : carapaces en orbite (9, 10) ou bananes en file derrière (8)
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st run kill @s
execute if score @s mg.kit matches 8 run function mg:kart/orb_summon {i:0,t:"mg.korbb",item:'{id:"minecraft:yellow_dye"}',s:1.1f}
execute if score @s mg.kit matches 8 run function mg:kart/orb_summon {i:1,t:"mg.korbb",item:'{id:"minecraft:yellow_dye"}',s:1.1f}
execute if score @s mg.kit matches 8 run function mg:kart/orb_summon {i:2,t:"mg.korbb",item:'{id:"minecraft:yellow_dye"}',s:1.1f}
execute if score @s mg.kit matches 9 run function mg:kart/orb_summon {i:0,t:"mg.korbs",item:'{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":3381555}}',s:0.6f}
execute if score @s mg.kit matches 9 run function mg:kart/orb_summon {i:1,t:"mg.korbs",item:'{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":3381555}}',s:0.6f}
execute if score @s mg.kit matches 9 run function mg:kart/orb_summon {i:2,t:"mg.korbs",item:'{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":3381555}}',s:0.6f}
execute if score @s mg.kit matches 10 run function mg:kart/orb_summon {i:0,t:"mg.korbs",item:'{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":13382451}}',s:0.6f}
execute if score @s mg.kit matches 10 run function mg:kart/orb_summon {i:1,t:"mg.korbs",item:'{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":13382451}}',s:0.6f}
execute if score @s mg.kit matches 10 run function mg:kart/orb_summon {i:2,t:"mg.korbs",item:'{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":13382451}}',s:0.6f}
