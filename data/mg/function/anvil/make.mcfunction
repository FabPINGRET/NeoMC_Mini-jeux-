# Crée l'ombre au sol puis l'enclume (position d'exécution = cible)
summon minecraft:marker ~ 81 ~ {Tags:["mg.sh","mg.shn"]}
execute if block ~ 80 ~ minecraft:smooth_stone run setblock ~ 80 ~ minecraft:black_concrete
summon minecraft:falling_block ~ 106 ~ {BlockState:{Name:"minecraft:anvil"},Time:1,HurtEntities:1b,FallHurtAmount:20.0f,FallHurtMax:200,DropItem:0b,Tags:["mg.anv"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.shn] mg.t 45
tag @e[type=minecraft:marker,tag=mg.shn] remove mg.shn
