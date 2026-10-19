# @s : sifflet : son destrier apparaît et il monte dessus
execute if score @s mg.olhorse matches ..0 run return 0
execute if entity @s[tag=mg.olboss_in] run return run tellraw @s {"text":"Pas de destrier pendant un combat de boss.","color":"red"}
function mg:ombre/horse_gone
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:horse ~ ~ ~ {Tags:["mg.ol","mg.olmount","mg.ollast"],Tame:1b,PersistenceRequired:1b,Variant:515,equipment:{saddle:{id:"minecraft:saddle",count:1},body:{id:"minecraft:iron_horse_armor",count:1}},attributes:[{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:jump_strength",base:0.9},{id:"minecraft:max_health",base:40},{id:"minecraft:step_height",base:1.2}]}
data modify entity @e[tag=mg.ollast,limit=1] Owner set from entity @s UUID
scoreboard players operation @e[tag=mg.ollast] mg.olo = @s mg.olpid
ride @s mount @e[tag=mg.ollast,limit=1]
execute at @s run playsound minecraft:entity.horse.gallop player @a ~ ~ ~ 1 1
