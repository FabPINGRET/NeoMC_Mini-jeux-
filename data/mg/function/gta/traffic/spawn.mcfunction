# Une voiture PNJ à ce carrefour (contexte : marqueur mg.gix) : modèle au hasard, direction au hasard
scoreboard players add $gvid mg.st 1
summon minecraft:marker ~ ~ ~ {Tags:["mg.gta","mg.gtraf","mg.gvn","mg.gtnew"]}
execute store result score $gr mg.st run random value 1..10
scoreboard players operation @e[type=minecraft:marker,tag=mg.gtnew] mg.gtmod = $gr mg.st
execute if score $gr mg.st matches 1 run function mg:gta/traffic/body_1
execute if score $gr mg.st matches 2 run function mg:gta/traffic/body_2
execute if score $gr mg.st matches 3 run function mg:gta/traffic/body_3
execute if score $gr mg.st matches 4 run function mg:gta/traffic/body_4
execute if score $gr mg.st matches 5 run function mg:gta/traffic/body_5
execute if score $gr mg.st matches 6 run function mg:gta/traffic/body_6
execute if score $gr mg.st matches 7 run function mg:gta/traffic/body_7
execute if score $gr mg.st matches 8 run function mg:gta/traffic/body_8
execute if score $gr mg.st matches 9 run function mg:gta/traffic/body_9
execute if score $gr mg.st matches 10 run function mg:gta/traffic/body_10
scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st
tag @e[tag=mg.gvn] remove mg.gvn
scoreboard players set @e[type=minecraft:marker,tag=mg.gtnew] mg.gtw8 0
execute as @e[type=minecraft:marker,tag=mg.gtnew] run function mg:gta/traffic/start
tag @e[tag=mg.gtnew] remove mg.gtnew
