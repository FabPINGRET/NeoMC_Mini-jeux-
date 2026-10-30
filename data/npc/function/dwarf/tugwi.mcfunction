execute positioned -286 58 -55 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -286 58 -55 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tugwi","color":"dark_aqua"},{"text":"> Judge, please, I'm not a bone monster! I barely even have bones, I think! I think, like, I've never even known about me having a bone before, honest! Whoa what's that, a bone in me? First time I noticed!","color":"white"}]
execute positioned -286 58 -55 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tugwi","color":"dark_aqua"},{"text":"> Aw, stop it haha, I admit I'm your secret admirer, ok Wumwug Bim? Aw you're too nice haha no it's ok I only spent like 6 hours on those cookies for you, it's not a big deaaaaallllll haha.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
