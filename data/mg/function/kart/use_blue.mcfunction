# Carapace bleue : s'envole et file sur le premier, explose sur lui et ses voisins
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run summon minecraft:item_display ~ ~3 ~ {Tags:["mg.kblue","mg.knew","mg.fx"],teleport_duration:1,Glowing:1b,glow_color_override:3364351,item:{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":3364351}},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.3f,1.3f,1.3f]}}
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.t 400
tag @e[type=minecraft:item_display,tag=mg.knew] remove mg.knew
tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" lance une ","color":"gray"},{"text":"carapace bleue 🔵","color":"blue","bold":true}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.elder_guardian.curse master @s ~ ~ ~ 0.4 1.6
