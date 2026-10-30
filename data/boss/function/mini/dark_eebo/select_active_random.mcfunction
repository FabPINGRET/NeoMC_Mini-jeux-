tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active
function boss:mini/dark_eebo/reset_marker_rotation

summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","1","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","2","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","3","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","4","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","5","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","6","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","7","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_active_temp","8","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=deebo_active_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=deebo_active_temp,tag=exclude,distance=0..]

execute if entity @e[tag=deebo_active_temp,tag=1,distance=0..] run tag @n[tag=deebo,tag=1,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=1,distance=0..] run tag @n[tag=deebo_marker,tag=1,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=1,distance=0..] run scoreboard players set deebo_painting Value 1
execute if entity @e[tag=deebo_active_temp,tag=2,distance=0..] run tag @n[tag=deebo,tag=2,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=2,distance=0..] run tag @n[tag=deebo_marker,tag=2,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=2,distance=0..] run scoreboard players set deebo_painting Value 2
execute if entity @e[tag=deebo_active_temp,tag=3,distance=0..] run tag @n[tag=deebo,tag=3,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=3,distance=0..] run tag @n[tag=deebo_marker,tag=3,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=3,distance=0..] run scoreboard players set deebo_painting Value 3
execute if entity @e[tag=deebo_active_temp,tag=4,distance=0..] run tag @n[tag=deebo,tag=4,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=4,distance=0..] run tag @n[tag=deebo_marker,tag=4,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=4,distance=0..] run scoreboard players set deebo_painting Value 4
execute if entity @e[tag=deebo_active_temp,tag=5,distance=0..] run tag @n[tag=deebo,tag=5,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=5,distance=0..] run tag @n[tag=deebo_marker,tag=5,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=5,distance=0..] run scoreboard players set deebo_painting Value 5
execute if entity @e[tag=deebo_active_temp,tag=6,distance=0..] run tag @n[tag=deebo,tag=6,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=6,distance=0..] run tag @n[tag=deebo_marker,tag=6,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=6,distance=0..] run scoreboard players set deebo_painting Value 6
execute if entity @e[tag=deebo_active_temp,tag=7,distance=0..] run tag @n[tag=deebo,tag=7,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=7,distance=0..] run tag @n[tag=deebo_marker,tag=7,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=7,distance=0..] run scoreboard players set deebo_painting Value 7
execute if entity @e[tag=deebo_active_temp,tag=8,distance=0..] run tag @n[tag=deebo,tag=8,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=8,distance=0..] run tag @n[tag=deebo_marker,tag=8,distance=0..] add active
execute if entity @e[tag=deebo_active_temp,tag=8,distance=0..] run scoreboard players set deebo_painting Value 8

kill @e[type=minecraft:area_effect_cloud,tag=deebo_active_temp,distance=0..]
