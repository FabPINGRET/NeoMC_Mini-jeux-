# Voiture de police pilotée par un policier (contexte : carrefour) : elle poursuit le joueur recherché
function mg:gta/car/spawn_5
scoreboard players operation $gpv mg.st = $gvid mg.st
execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gpv mg.st run tag @s add mg.gpcar
execute if score $rp mg.st matches 1 run summon minecraft:skeleton ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcop","mg.npc","mg.gcopn"],PersistenceRequired:1b,CustomName:{"text":"Policier","color":"blue"},equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":1981031}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1981031}},feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":1315860}},mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{"minecraft:item_model":"mg:gun_pistol"}}},drop_chances:{head:0f,chest:0f,legs:0f,feet:0f,mainhand:0f},attributes:[{id:"minecraft:movement_speed",base:0.28}]}
execute unless score $rp mg.st matches 1 run summon minecraft:skeleton ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcop","mg.npc","mg.gcopn"],PersistenceRequired:1b,CustomName:{"text":"Policier","color":"blue"},equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":1981031}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1981031}},feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":1315860}},mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{"minecraft:item_model":"minecraft:crossbow"}}},drop_chances:{head:0f,chest:0f,legs:0f,feet:0f,mainhand:0f},attributes:[{id:"minecraft:movement_speed",base:0.28}]}
team join mg_gciv @e[tag=mg.gcopn]
execute as @e[tag=mg.gcopn] run ride @s mount @e[type=minecraft:horse,tag=mg.gpcar,tag=!mg.gpcarr,limit=1,sort=nearest]
tag @e[tag=mg.gpcar] add mg.gpcarr
tag @e[tag=mg.gcopn] remove mg.gcopn
playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 2 1.4
