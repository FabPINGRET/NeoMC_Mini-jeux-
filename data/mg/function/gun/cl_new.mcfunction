# @s : tient une arme, pas encore de boîte (position = ses yeux)
summon minecraft:interaction ~ ~-1.3 ~ {Tags:["mg.gci","mg.gcin"],width:2.6f,height:2.6f,response:0b}
scoreboard players operation @e[type=minecraft:interaction,tag=mg.gcin] mg.gcid = @s mg.gcid
tag @e[tag=mg.gcin] remove mg.gcin
tag @s add mg.gchas
