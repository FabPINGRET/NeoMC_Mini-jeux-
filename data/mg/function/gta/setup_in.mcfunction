# Entités de la session (contexte : dimension mg:gta)
function mg:gta/clear
function mg:gta/walls
scoreboard players set $gvid mg.st 0
team add mg_gciv
team modify mg_gciv friendlyFire true
team modify mg_gciv seeFriendlyInvisibles false
team modify mg_gciv nametagVisibility always
team join mg_gciv @a[tag=mg.gtw,scores={mg.gwl=0}]
function mg:gta/bars
summon minecraft:marker -76 65 32322 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -76 65 32346 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -76 65 32370 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -76 65 32394 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -76 65 32418 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -76 65 32442 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -76 65 32466 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32322 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32346 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32370 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32394 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32418 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32442 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -44 65 32466 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -12 65 32322 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -12 65 32346 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -12 65 32370 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -12 65 32394 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -12 65 32418 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -12 65 32466 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32322 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32346 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32370 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32394 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32418 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32442 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 20 65 32466 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32322 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32346 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32370 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32394 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32418 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32442 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker 52 65 32466 {Tags:["mg.gta","mg.gix"]}
summon minecraft:marker -81 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32422 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32422 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32438 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32446 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32438 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32446 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32462 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32462 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -71 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32422 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32438 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32446 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32462 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -49 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -39 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -17 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -7 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32422 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32438 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32446 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 15 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32462 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 25 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32318 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32326 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32342 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32350 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32366 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32374 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32390 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32398 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32422 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32414 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32422 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32438 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32446 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32438 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32446 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32462 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 47 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32462 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker 57 65 32470 {Tags:["mg.gta","mg.gsw"]}
summon minecraft:marker -81 65 32318 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -81.5 65 32317.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -49 65 32342 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -49.5 65 32341.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -81 65 32438 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -81.5 65 32437.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 47 65 32462 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 46.5 65 32461.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 15 65 32390 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 14.5 65 32389.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -81 65 32462 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -81.5 65 32461.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -17 65 32462 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 52
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -17.5 65 32461.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -81 65 32390 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 53
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -81.5 65 32389.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -81 65 32342 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 54
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -81.5 65 32341.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 47 65 32318 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 52
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 46.5 65 32317.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -17 65 32342 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 53
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -17.5 65 32341.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -17 65 32318 {Tags:["mg.gta","mg.gpad","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 55
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -17.5 65 32317.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -21 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 2
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -21.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -19 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 3
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -19.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -17 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 4
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -17.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -15 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 5
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -15.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -13 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 6
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -13.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -11 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 7
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -11.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -9 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 8
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -9.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -7 66 32432 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 9
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -7.5 66 32431.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -38 66 32431 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 21
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -38.5 66 32430.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -35 66 32431 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 22
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -35.5 66 32430.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -32 66 32431 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 23
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -32.5 66 32430.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -29 66 32431 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 24
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -29.5 66 32430.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -26 66 32431 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 25
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -26.5 66 32430.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:text_display -31.5 71.5 32423.95 {Tags:["mg.gta"],Rotation:[0f,0f],text:{"text":"🏎 NEO MOTORS","color":"light_purple","bold":true},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]}}
summon minecraft:text_display 6.5 72.6 32422.9 {Tags:["mg.gta"],Rotation:[0f,0f],text:{"text":"🏦 BANQUE DE NEO CITY","color":"gold","bold":true},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}
summon minecraft:marker 6 66 32432 {Tags:["mg.gta","mg.gbank"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gbank] mg.gpc 0
summon minecraft:text_display 6.5 68.2 32432.5 {Tags:["mg.gta","mg.gbkl"],billboard:"center",text:{"text":"💰 Coffres : accroupi + arme pendant 15 s","color":"gold"},background:1073741824,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:marker 4 66 32454 {Tags:["mg.gta","mg.gair"]}
summon minecraft:marker -17 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 31
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -17.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -14 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 32
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -14.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -11 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 33
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -11.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -8 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 34
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -8.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -5 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 35
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -5.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 15 71 32255 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 42
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 14.5 71 32254.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 17 71 32255 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 43
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 16.5 71 32254.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 19 71 32255 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 44
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 18.5 71 32254.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 21 71 32255 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 45
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 20.5 71 32254.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 23 71 32255 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 46
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 22.5 71 32254.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 25 71 32255 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 47
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 24.5 71 32254.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 17 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 11
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 16.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 23 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 49
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display 22.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker -2 71 32273 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 60
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
summon minecraft:block_display -2.5 71 32272.5 {Tags:["mg.gta","mg.gpdb"],block_state:{Name:"minecraft:light_weighted_pressure_plate"}}
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 25 71 32265 {Tags:["mg.gta","mg.glup"]}
summon minecraft:marker 25 84 32265 {Tags:["mg.gta","mg.gldn"]}
summon minecraft:text_display 25.5 72.8 32265.5 {Tags:["mg.gta"],billboard:"center",text:{"text":"⬆ Toit-terrasse : jacuzzi et bar","color":"aqua"},background:1073741824,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:text_display 25.5 85.8 32265.5 {Tags:["mg.gta"],billboard:"center",text:{"text":"⬇ Descendre","color":"aqua"},background:1073741824,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}
summon minecraft:block_display 24.5 71 32264.5 {Tags:["mg.gta"],block_state:{Name:"minecraft:heavy_weighted_pressure_plate"}}
summon minecraft:block_display 24.5 84 32264.5 {Tags:["mg.gta"],block_state:{Name:"minecraft:heavy_weighted_pressure_plate"}}
summon minecraft:text_display 20.5 80.6 32299.6 {Tags:["mg.gta"],Rotation:[0f,0f],text:[{"text":"NEO HILLS","color":"gold","bold":true},{"text":"\nla villa des joueurs : tout ce qui a été acheté une fois est ici, gratuit","color":"gray"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}
summon minecraft:marker 28 66 32411 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 70
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 31 66 32411 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 70
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 34 66 32411 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 70
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 37 66 32411 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 70
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 40 66 32411 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 70
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 43 66 32411 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 70
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 36 66 32405 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 71
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
summon minecraft:marker 36 66 32409 {Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt 72
scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0
execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show
tag @e[tag=mg.gpn] remove mg.gpn
function mg:gta/places_setup
summon minecraft:villager -64.5 66 32332.5 {Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:farmer",type:"minecraft:plains",level:2},CustomName:{"text":"Caissier","color":"gray"},CustomNameVisible:0b}
summon minecraft:text_display -63.5 67.55 32330.65 {Tags:["mg.gta"],Rotation:[180f,0f],text:[{"text":"🔫 BRAQUAGE","color":"red","bold":true},{"text":"\nAccroupis-toi devant la caisse, arme en main (5 s)","color":"white"},{"text":"\n💰 200 à 450 $  ·  ★★ police","color":"gold"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:villager 4.5 66 32380.5 {Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:librarian",type:"minecraft:plains",level:2},CustomName:{"text":"Caissier","color":"gray"},CustomNameVisible:0b}
summon minecraft:text_display 4.5 67.55 32378.65 {Tags:["mg.gta"],Rotation:[180f,0f],text:[{"text":"🔫 BRAQUAGE","color":"red","bold":true},{"text":"\nAccroupis-toi devant la caisse, arme en main (5 s)","color":"white"},{"text":"\n💰 200 à 450 $  ·  ★★ police","color":"gold"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:villager -55.5 66 32404.5 {Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:mason",type:"minecraft:plains",level:2},CustomName:{"text":"Caissier","color":"gray"},CustomNameVisible:0b}
summon minecraft:text_display -54.5 67.55 32402.65 {Tags:["mg.gta"],Rotation:[180f,0f],text:[{"text":"🔫 BRAQUAGE","color":"red","bold":true},{"text":"\nAccroupis-toi devant la caisse, arme en main (5 s)","color":"white"},{"text":"\n💰 200 à 450 $  ·  ★★ police","color":"gold"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:villager -60.5 66 32476.5 {Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:butcher",type:"minecraft:plains",level:2},CustomName:{"text":"Caissier","color":"gray"},CustomNameVisible:0b}
summon minecraft:text_display -59.5 67.55 32474.65 {Tags:["mg.gta"],Rotation:[180f,0f],text:[{"text":"🔫 BRAQUAGE","color":"red","bold":true},{"text":"\nAccroupis-toi devant la caisse, arme en main (5 s)","color":"white"},{"text":"\n💰 200 à 450 $  ·  ★★ police","color":"gold"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:villager -32.5 66 32332.5 {Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:cleric",type:"minecraft:plains",level:2},CustomName:{"text":"Caissier","color":"gray"},CustomNameVisible:0b}
summon minecraft:text_display -31.5 67.55 32330.65 {Tags:["mg.gta"],Rotation:[180f,0f],text:[{"text":"🔫 BRAQUAGE","color":"red","bold":true},{"text":"\nAccroupis-toi devant la caisse, arme en main (5 s)","color":"white"},{"text":"\n💰 200 à 450 $  ·  ★★ police","color":"gold"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:villager -28.5 66 32404.5 {Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[180f,0f],VillagerData:{profession:"minecraft:cartographer",type:"minecraft:plains",level:2},CustomName:{"text":"Caissier","color":"gray"},CustomNameVisible:0b}
summon minecraft:text_display -27.5 67.55 32402.65 {Tags:["mg.gta"],Rotation:[180f,0f],text:[{"text":"🔫 BRAQUAGE","color":"red","bold":true},{"text":"\nAccroupis-toi devant la caisse, arme en main (5 s)","color":"white"},{"text":"\n💰 200 à 450 $  ·  ★★ police","color":"gold"}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
summon minecraft:marker -64 66 32330 {Tags:["mg.gta","mg.gshop"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-64,y=66,z=32330] mg.gsid 0
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-64,y=66,z=32330] mg.gpc 0
summon minecraft:text_display -63.5 70.4 32325.8 {Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:[{"text":"🛒 Supérette","color":"white","bold":true},{"text":"\nbraquable : accroupi + arme devant la caisse","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.1f,1.1f,1.1f]}}
scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x=-63.5,y=70.4,z=32325.8] mg.gsid 0
summon minecraft:marker 4 66 32378 {Tags:["mg.gta","mg.gshop"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=4,y=66,z=32378] mg.gsid 1
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=4,y=66,z=32378] mg.gpc 0
summon minecraft:text_display 4.5 70.4 32373.8 {Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:[{"text":"💎 Bijouterie","color":"white","bold":true},{"text":"\nbraquable : accroupi + arme devant la caisse","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.1f,1.1f,1.1f]}}
scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x=4.5,y=70.4,z=32373.8] mg.gsid 1
summon minecraft:marker -55 66 32402 {Tags:["mg.gta","mg.gshop"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-55,y=66,z=32402] mg.gsid 2
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-55,y=66,z=32402] mg.gpc 0
summon minecraft:text_display -54.5 70.4 32397.8 {Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:[{"text":"⛽ Station","color":"white","bold":true},{"text":"\nbraquable : accroupi + arme devant la caisse","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.1f,1.1f,1.1f]}}
scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x=-54.5,y=70.4,z=32397.8] mg.gsid 2
summon minecraft:marker -60 66 32474 {Tags:["mg.gta","mg.gshop"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-60,y=66,z=32474] mg.gsid 3
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-60,y=66,z=32474] mg.gpc 0
summon minecraft:text_display -59.5 70.4 32469.8 {Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:[{"text":"🍔 Burger","color":"white","bold":true},{"text":"\nbraquable : accroupi + arme devant la caisse","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.1f,1.1f,1.1f]}}
scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x=-59.5,y=70.4,z=32469.8] mg.gsid 3
summon minecraft:marker -32 66 32330 {Tags:["mg.gta","mg.gshop"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-32,y=66,z=32330] mg.gsid 4
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-32,y=66,z=32330] mg.gpc 0
summon minecraft:text_display -31.5 70.4 32325.8 {Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:[{"text":"💊 Pharmacie","color":"white","bold":true},{"text":"\nbraquable : accroupi + arme devant la caisse","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.1f,1.1f,1.1f]}}
scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x=-31.5,y=70.4,z=32325.8] mg.gsid 4
summon minecraft:marker -28 66 32402 {Tags:["mg.gta","mg.gshop"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-28,y=66,z=32402] mg.gsid 5
scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x=-28,y=66,z=32402] mg.gpc 0
summon minecraft:text_display -27.5 70.4 32397.8 {Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:[{"text":"📱 Téléphones","color":"white","bold":true},{"text":"\nbraquable : accroupi + arme devant la caisse","color":"gray","bold":false}],background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.1f,1.1f,1.1f]}}
scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x=-27.5,y=70.4,z=32397.8] mg.gsid 5
summon minecraft:text_display -13.5 70.5 32423.95 {Tags:["mg.gta"],Rotation:[0f,0f],text:{"text":"🔫 ARMURERIE","color":"white","bold":true},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -13.5 70.05 32423.95 {Tags:["mg.gta"],Rotation:[0f,0f],text:{"text":"Toutes les armes, en libre-service","color":"yellow"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
execute positioned -42 65 32370 run function mg:gta/car/spawn_1
execute positioned -42 65 32442 run function mg:gta/car/spawn_2
execute positioned 54 65 32394 run function mg:gta/car/spawn_3
execute positioned 22 65 32418 run function mg:gta/car/spawn_4
execute positioned -42 65 32466 run function mg:gta/car/spawn_5
execute positioned -42 65 32418 run function mg:gta/car/spawn_6
execute positioned -42 65 32322 run function mg:gta/car/spawn_7
execute positioned -10 65 32418 run function mg:gta/car/spawn_8
execute positioned 22 65 32346 run function mg:gta/car/spawn_9
execute positioned 54 65 32346 run function mg:gta/car/spawn_10
execute positioned 54 65 32418 run function mg:gta/car/spawn_1
execute positioned 22 65 32370 run function mg:gta/car/spawn_2
execute positioned -10 65 32370 run function mg:gta/car/spawn_3
execute positioned -42 65 32394 run function mg:gta/car/spawn_4
execute positioned 54 65 32370 run function mg:gta/car/spawn_5
execute positioned 54 65 32442 run function mg:gta/car/spawn_6
execute positioned -30 66 32430 run function mg:gta/heli_spawn {c:"red_concrete"}
execute positioned 0 66 32432 run function mg:gta/heli_spawn {c:"blue_concrete"}
execute positioned 52 66 32322 run function mg:gta/heli_spawn {c:"black_concrete"}
execute positioned -76 66 32466 run function mg:gta/heli_spawn {c:"white_concrete"}
summon minecraft:marker -17 65 32390 {Tags:["mg.gta","mg.gexit"]}
summon minecraft:block_display -17.5 65 32389.5 {Tags:["mg.gta"],block_state:{Name:"minecraft:heavy_weighted_pressure_plate"}}
summon minecraft:text_display -16.5 67.2 32390.5 {Tags:["mg.gta"],billboard:"center",text:{"text":"🚪 Retour au lobby","color":"gold","bold":true},background:1073741824,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.9f,0.9f,0.9f]}}
execute as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=40] at @s run function mg:gta/ped_spawn
scoreboard players set $gsu mg.st 2
function mg:gta/dots_init
