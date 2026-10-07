$execute at @s run summon minecraft:item_display ~ ~ ~ {Tags:["mg.korb","$(t)","mg.korbn","mg.fx"],teleport_duration:2,item:$(item),transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[$(s),$(s),$(s)]}}
scoreboard players operation @e[type=minecraft:item_display,tag=mg.korbn] mg.ri = @s mg.ri
$scoreboard players set @e[type=minecraft:item_display,tag=mg.korbn] mg.kdd $(i)
tag @e[tag=mg.korbn] remove mg.korbn
