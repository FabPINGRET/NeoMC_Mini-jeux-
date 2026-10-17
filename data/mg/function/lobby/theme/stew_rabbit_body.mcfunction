# 🎃 Lapin du ragoût : un vrai lapin figé, appelé par stew_rabbit et stew_rabbit_keep (@s = joueur) ; id du joueur conservé (mg.thbn)
execute unless score @s mg.thbn matches 1.. run scoreboard players add $thbn mg.st 1
execute unless score @s mg.thbn matches 1.. run scoreboard players operation @s mg.thbn = $thbn mg.st
execute at @s run summon minecraft:rabbit ~ ~ ~ {Tags:["mg.thbun","mg.thbnew"],NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,DeathLootTable:"minecraft:empty",attributes:[{id:"minecraft:scale",base:0.8}]}
scoreboard players operation @e[type=minecraft:rabbit,tag=mg.thbnew] mg.thbn = @s mg.thbn
team join mg_thbun @e[type=minecraft:rabbit,tag=mg.thbnew]
tag @e[type=minecraft:rabbit,tag=mg.thbnew] remove mg.thbnew
