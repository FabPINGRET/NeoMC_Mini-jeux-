summon minecraft:item_display ~ ~0.25 ~ {Tags:["mg.zent","mg.zmk","mg.zmkn"],Glowing:1b,glow_color_override:16755200,item:{id:"minecraft:note_block",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
scoreboard players operation @e[tag=mg.zmkn] mg.zmo = @s mg.zmo
scoreboard players set @e[tag=mg.zmkn] mg.zmc 0
tag @e[tag=mg.zmkn] remove mg.zmkn
kill @s
