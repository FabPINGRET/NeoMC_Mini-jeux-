# Habille @s (nouvelle entité du kart) avec le modèle du resource pack
tag @s add mg.rps
execute if entity @s[tag=mg.kart] run return run function mg:kart/rp_kart
execute if entity @s[type=minecraft:block_display,tag=mg.kp1] run return run data modify entity @s block_state.Name set value "minecraft:air"
execute if entity @s[type=minecraft:block_display,tag=mg.kp2] run return run data modify entity @s block_state.Name set value "minecraft:air"
execute if entity @s[type=minecraft:block_display,tag=mg.kp3] run return run data modify entity @s block_state.Name set value "minecraft:air"
execute if entity @s[type=minecraft:block_display,tag=mg.kp4] run return run data modify entity @s block_state.Name set value "minecraft:air"
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:yellow_dye run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:banana"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:leather_helmet[minecraft:dyed_color=3381555] run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:shell_green"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:leather_helmet[minecraft:dyed_color=13382451] run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:shell_red"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:leather_helmet[minecraft:dyed_color=3364351] run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:shell_blue"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:black_concrete run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:bobomb"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:yellow_stained_glass run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:item_box"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:chiseled_stone_bricks run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:thwomp"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:red_mushroom_block run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:piranha"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:brown_mushroom_block run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:goomba"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:cactus run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:pokey"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:coal_block run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:chomp"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:tropical_fish run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:cheep"}}
execute if entity @s[type=minecraft:item_display] if items entity @s contents minecraft:fire_charge run return run item modify entity @s contents {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:podoboo"}}
