# @s = joueur : sa moto (cheval rapide, sans saut, increvable)
summon minecraft:horse ~ ~ ~ {Tags:["mg.trh","mg.trnew","mg.npc"],Tame:1b,PersistenceRequired:1b,Invulnerable:1b,Silent:1b,equipment:{saddle:{id:"minecraft:saddle",count:1}},attributes:[{id:"minecraft:movement_speed",base:0.32d},{id:"minecraft:jump_strength",base:0.0d},{id:"minecraft:step_height",base:0.0d}]}
scoreboard players operation @e[tag=mg.trnew,limit=1] mg.trc = @s mg.trc
ride @s mount @e[tag=mg.trnew,limit=1]
tag @e[tag=mg.trnew] remove mg.trnew
