execute if entity @s[nbt={active_effects:[{id:"minecraft:slowness"}]}] run return 0
effect give @s minecraft:slowness 5 2 true
effect give @s minecraft:blindness 2 0 true
title @s actionbar {"text":"🕸 Piège : englué !","color":"red"}
playsound minecraft:block.honey_block.slide master @s ~ ~ ~ 1 0.6
