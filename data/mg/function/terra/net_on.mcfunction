# @s (dinosaure) : pris dans un filet (5 s, carnotaure 2,5 s, brachiosaure 3 s)
scoreboard players set @s mg.tvst 100
execute if entity @s[tag=mg.tvcarno] run scoreboard players set @s mg.tvst 50
execute if entity @s[tag=mg.tvbig] run scoreboard players set @s mg.tvst 60
data merge entity @s {NoAI:1b}
tag @s add mg.tvnetted
scoreboard players operation $tvi mg.st = @s mg.tvid
execute as @e[type=minecraft:block_display,tag=mg.tvnetd] if score @s mg.tvid = $tvi mg.st run kill @s
execute unless entity @s[tag=mg.tvcarno] unless entity @s[tag=mg.tvbig] run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvp","mg.tvnetd","mg.tvn","mg.tvok"],block_state:{Name:"minecraft:cobweb"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.8f,0f,-0.8f],scale:[1.6f,1.8f,1.6f]}}
execute if entity @s[tag=mg.tvcarno] run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvp","mg.tvnetd","mg.tvn","mg.tvok"],block_state:{Name:"minecraft:cobweb"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-1.4f,0f,-1.4f],scale:[2.8f,3.4f,2.8f]}}
execute if entity @s[tag=mg.tvbig] run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvp","mg.tvnetd","mg.tvn","mg.tvok"],block_state:{Name:"minecraft:cobweb"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-2.0f,0f,-2.0f],scale:[4.0f,5.0f,4.0f]}}
scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvi mg.st
tag @e[tag=mg.tvn] remove mg.tvn
playsound minecraft:block.wool.place hostile @a ~ ~ ~ 1 0.6
particle minecraft:block{block_state:"minecraft:cobweb"} ~ ~1 ~ 0.5 0.6 0.5 0 25
