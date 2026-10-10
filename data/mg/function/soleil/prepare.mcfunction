# 🔴 1, 2, 3 Soleil — préparation
function mg:soleil/build
function mg:soleil/doll
kill @e[tag=mg.sqs]
summon minecraft:marker -18.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -16.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -14.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -12.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -10.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -8.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -6.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -4.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker -2.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 0.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 2.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 4.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 6.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 8.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 10.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 12.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 14.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 16.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
summon minecraft:marker 18.5 65 37002.5 {Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 86
scoreboard players set $pz mg.st 37045
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_sq @a[tag=mg.play]
tag @a[tag=mg.play] remove mg.sqf
tag @e remove mg.squ
execute as @a[tag=mg.play] run function mg:soleil/place
scoreboard players set $sqn mg.st 0
scoreboard players set $sqe mg.st 0
