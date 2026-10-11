summon minecraft:marker 0 64 0 {Tags:["mg.evx","mg.evp"]}
spreadplayers 0 0 0 40 under 85 false @e[type=minecraft:marker,tag=mg.evp]
execute store result score $evr mg.st run random value 1..8
execute at @e[type=minecraft:marker,tag=mg.evp] if score $evr mg.st matches 1 run summon minecraft:item ~ ~14 ~ {Tags:["mg.evx","mg.keep"],Glowing:1b,Item:{id:"minecraft:gold_ingot",count:1,components:{"minecraft:custom_data":{mg_ev:1b},"minecraft:item_name":{"text":"Gros lingot (5)","color":"gold"}}}}
execute at @e[type=minecraft:marker,tag=mg.evp] unless score $evr mg.st matches 1 run summon minecraft:item ~ ~14 ~ {Tags:["mg.evx","mg.keep"],Item:{id:"minecraft:gold_nugget",count:1,components:{"minecraft:custom_data":{mg_ev:1b},"minecraft:item_name":{"text":"Pièce (1)","color":"gold"}}}}
execute at @e[type=minecraft:marker,tag=mg.evp] run particle minecraft:wax_on ~ ~14 ~ 0.3 0.3 0.3 0 5
kill @e[type=minecraft:marker,tag=mg.evp]
