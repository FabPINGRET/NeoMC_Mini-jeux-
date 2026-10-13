# 🎄 Noël : habillage resource pack (@s = animal, position = animal)
summon minecraft:item_display ~ ~ ~ {Tags:["mg.thm","mg.thrid","mg.thnew"],item_display:"head",teleport_duration:3,item:{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/antlers"}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0.35f,0.95f],scale:[0.9f,0.9f,0.9f]}}
ride @e[type=minecraft:item_display,tag=mg.thnew,limit=1] mount @s
tag @e[tag=mg.thnew] remove mg.thnew
